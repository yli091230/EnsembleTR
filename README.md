# EnsembleTR

EnsembleTR is a tool for ensemble Tandem Repeat (TR) calling. It takes one or more VCF files with TR genotypes for a panel of samples and outputs a consensus set of genotypes.


## Installation

```
python3 setup.py install --user
```

Type `EnsembleTR`. You should see the help message appear.

## Usage

To run EnsembleTR, use the following command

```
EnsembleTR --out output.vcf
           --ref ref.fa
           --vcfs vcf1.vcf,vcf2.vcf,...
```
Required parameters:
* **`--vcfs <file.vcf,[file2.vcf]>`** Comma separated list of input VCF files
* **`--ref`** Refererence genome (.fa)
* **`--out`** Path to output VCF file

## File formats

### VCF (`--vcfs`)
Both zipped and unzipped VCF files are accepted as input. EnsembleTR can currently process VCF files generated by [hipSTR](https://github.com/tfwillems/HipSTR), [GangSTR](https://github.com/gymreklab/GangSTR), [adVNTR](https://advntr.readthedocs.io/en/latest/#), and [ExpansionHunter](https://github.com/Illumina/ExpansionHunter).

### FASTA Reference genome (`--ref`)
You must input a reference genome in FASTA format. This must be the same reference build used for TR calling in input files.

### VCF (`--out`)
For more information on VCF file format, see the [VCF spec](http://samtools.github.io/hts-specs/VCFv4.2.pdf). EnsembleTR output VCF file contains several fields that are described below.

#### INFO fields

INFO fields contain aggregated statistics about each TR. The following custom fields are added:

| **FIELD** | **DESCRIPTION** |
|-----------|------------------|
| START | Start position of the TR |
| END | End position of the TR |
| PERIOD | Length of the repeat unit |
| RU | Repeat motif | 
| METHODS| Methods that attempted to genotype this locus (AdVNTR, EH, HipSTR, GangSTR)| 

#### FORMAT fields
FORMAT fields contain information specific to each genotype call. The following custom fields are added:

| **FIELD** | **DESCRIPTION** |
|-----------|------------------|
| GT | Genotype |
| GB | Base pair difference from ref allele |
| NCOPY | Genotype given in number of copies of the repeat motif |
| EXP | Boolean showing if the genotype alleles were expanded |
| SCORE | Score of the consensus call |
| GTS | Method(s) that support the consensus call |
| ALS | Number of times each bp difference was seen across all calls |
| INPUTS | Raw calls | 

Score is calculated by aggregating quality information from calls that are getting merged at each locus.

## Using statSTR on EnsembleTR files

You can use [statSTR](https://trtools.readthedocs.io/en/latest/source/statSTR.html) from [TRTools](https://trtools.readthedocs.io/en/latest/index.html) to compute various per-locus statistics for EnsembleTR .VCF files.

For example, to compute per-locus allele frequency use the following command:

```
statSTR --vcf EnsembleTR_file.vcf.gz
        --vcftype hipstr
        --afreq
        --out EnsembleTR_per_locus_allele_frequency
```

## Version II of EnsembleTR calls on samples from 1000 Genomes Project and H3Africa

Chromosome 1 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr1_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr1_filtered.vcf.gz.tbi)

Chromosome 2 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr2_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr2_filtered.vcf.gz.tbi)

Chromosome 3 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr3_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr3_filtered.vcf.gz.tbi)

Chromosome 4 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr4_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr4_filtered.vcf.gz.tbi)

Chromosome 5 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr5_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr5_filtered.vcf.gz.tbi)

Chromosome 6 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr6_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr6_filtered.vcf.gz.tbi)

Chromosome 7 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr7_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr7_filtered.vcf.gz.tbi)

Chromosome 8 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr8_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr8_filtered.vcf.gz.tbi)

Chromosome 9 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr9_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr9_filtered.vcf.gz.tbi)

Chromosome 10 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr10_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr10_filtered.vcf.gz.tbi)

Chromosome 11 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr11_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr11_filtered.vcf.gz.tbi)

Chromosome 12 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr12_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr12_filtered.vcf.gz.tbi)

Chromosome 13 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr13_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr13_filtered.vcf.gz.tbi)

Chromosome 14 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr14_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr14_filtered.vcf.gz.tbi)

Chromosome 15 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr15_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr15_filtered.vcf.gz.tbi)

Chromosome 16 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr16_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr16_filtered.vcf.gz.tbi)

Chromosome 17 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr17_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr17_filtered.vcf.gz.tbi)

Chromosome 18 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr18_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr18_filtered.vcf.gz.tbi)

Chromosome 19 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr19_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr19_filtered.vcf.gz.tbi)

Chromosome 20 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr20_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr20_filtered.vcf.gz.tbi)

Chromosome 21 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr21_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr21_filtered.vcf.gz.tbi)

Chromosome 22 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr22_filtered.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/add-vntrs/ensemble_chr22_filtered.vcf.gz.tbi)

## Version II of reference SNP+TR haplotype panel for imputation of TR variants

### Dataset description

[Phased variants](http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20220422_3202_phased_SNV_INDEL_SV/) of 3,202 samples from the 1000 Genomes Project (1kGP).

TRs imputed from 3,202 1kGP samples.

Total 70,692,015 variants + 1,091,550 TR markers.

All the coordinates are based on the hg38 human reference genome.

### Availability

Chromosome 1 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr1_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr1_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 2 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr2_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr2_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 3 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr3_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr3_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 4 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr4_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr4_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 5 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr5_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr5_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 6 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr6_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr6_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 7 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr7_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr7_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 8 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr8_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr8_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 9 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr9_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr9_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 10 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr10_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr10_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 11 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr11_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr11_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 12 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr12_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr12_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 13 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr13_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr13_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 14 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr14_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr14_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 15 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr15_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr15_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 16 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr16_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr16_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 17 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr17_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr17_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 18 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr18_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr18_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 19 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr19_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr19_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 20 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr20_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr20_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 21 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr21_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr21_final_SNP_merged_additional_TRs.vcf.gz.tbi)

Chromosome 22 [VCF file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr22_final_SNP_merged_additional_TRs.vcf.gz) and [tbi file](https://ensemble-tr.s3.us-east-2.amazonaws.com/additional-phased-trs/chr22_final_SNP_merged_additional_TRs.vcf.gz.tbi)

### Usage

Use [Beagle](https://faculty.washington.edu/browning/beagle/beagle.html) to impute TRs into SNP data:

```
java -Xmx4g -jar beagle.version.jar \
            gt=SNPs.vcf.gz \
            ref=${chrom}_final_SNP_merged.vcf.gz \
            out=imputed_TR_SNPs
```

