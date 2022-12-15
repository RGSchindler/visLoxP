## visLoxP

Description
--------------------------------------
visLoxP allows the user to simulate a qPCR in a genome of interest by looking for specific pairs of primers.
The user have to provide the following files:
1. Query genome in fasta format and in a single line.
2. Set of forward primers in a .csv file format
3. Set of reverse primers in a .csv file format.
4. Maximum amplicon size

Usage
--------------------------------------------

python VisLoxP.py genome.fasta fwd_primers.csv rev_primers.csv 700

Output
-------------------------------------------------
The output file will be written in a .txt file


| Oligo_name | LU1 | LU2 | LU3 | LU4 |
|------------|-----|-----|-----|-----|
| Genome_01  | 0   | 1   | 0   | 0   |
| Genome_02  | 1   | 1   | 0   | 0   |
| Genome_03  | 1   | 1   | 0   | 0   |



