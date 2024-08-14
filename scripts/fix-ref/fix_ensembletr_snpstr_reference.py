#!/usr/bin/env python

"""
Script to clean up SNP/TR reference haplotype panels
"""

import argparse
import cyvcf2
import pyfaidx
import sys
import subprocess
import os


MAX_ALLOWED_DUPS = 1000

def IsTRRecord(record_id):
    return record_id is None or record_id.strip() == "."

def GetTRRecordID(record, allids):
    locid = "EnsTR:%s:%s"%(record.CHROM, record.POS)
    if locid not in allids:
        return locid
    for i in range(1, MAX_ALLOWED_DUPS):
        newlocid = "%s-%s"%(locid, i)
        if newlocid not in allids:
            sys.stderr.write("Adding duplicate locus %s\n"%newlocid)
            return newlocid
    raise ValueError("Error: too many duplicates of %s"%locid)

def CheckReference(record, refgenome):
    # REF in VCF should match what is in the reference genome
    refseq = refgenome[record.CHROM][record.POS-1:record.POS-1+len(record.REF)]
    return (refseq == record.REF)

def run():
    args = getargs()
    if args == None:
        sys.exit(1)
    else:
        retcode = main(args)
        sys.exit(retcode)

def getargs(): # pragma: no cover
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("--vcf", help="Input SNP/TR VCF file", type=str, required=True)
    parser.add_argument("--ref", help="Reference fasta file", type=str, required=True)
    parser.add_argument("--out", help="Prefix for output VCF file", type=str, required=True)
    parser.add_argument("--max-records", help="Quit after processing this many records (for debug)", \
        default=-1, type=int)
    args = parser.parse_args()
    return args

def main(args):
    # Set up VCF reader
    reader = cyvcf2.Reader(args.vcf)

    # Set up the reference
    refgenome = pyfaidx.Fasta(args.ref)

    # Set up writer, adding the missing header
    reader.add_to_header('##command=hipstr;note this is a dummy header line')
    reader.add_to_header('##INFO=<ID=VT,Number=1,Type=String,Description="Type of variant">')
    writer = cyvcf2.Writer(args.out + ".vcf", reader)

    # Go through each record
    # If SNP: just print it
    # if STR: filter records with incorrect reference,
    #   and modify ID
    allids = set()
    num_records_processed = 0
    for record in reader:
        num_records_processed += 1
        if args.max_records > 0 and num_records_processed > args.max_records:
            break # for debug
        if not IsTRRecord(record.ID):
            record.INFO["VT"] = "OTHER"
            writer.write_record(record)
        else:
    		# Check reference
            if not CheckReference(record, refgenome):
                continue # skip this record
    		# Modify ID
            record.ID = GetTRRecordID(record, allids)
            allids.add(record.ID)
            record.INFO["VT"] =  "TR"
    		# Write to file
            writer.write_record(record)

    reader.close()
    writer.close()

    # Run bash script to convert to bref3
    cmd = "bash convert_to_bref3.sh {filename}".format(filename=args.out)
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    print(output.decode("utf-8"))

if __name__ == "__main__":
    run()