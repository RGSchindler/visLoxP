## visLoxP

Description
--------------------------------------
visLoxP allows the user to simulate a qPCR in a genome of interest by looking for specific pairs of primers.
The user have to provide the following files:
1. Query genome in fasta format in a single line.
2. Set of forward primers in .csv file format
3. Set of reverse primers in .csv file format.
4. Maximum amplicon size

Usage
--------------------------------------------

python VisLoxP.py genome.fasta fwd_primers.csv rev_primers.csv 700

Output
-------------------------------------------------
The output is generated as a .txt file


| Oligo_name | LU1 | LU2 | LU3 | LU4 |
|------------|-----|-----|-----|-----|
| Genome_01  | 0   | 1   | 0   | 0   |
| Genome_02  | 1   | 1   | 0   | 0   |
| Genome_03  | 1   | 1   | 0   | 0   |

License
-------------------------------------------------
This is a repository written under the [CC BY-NC 4.0 license](http://creativecommons.org/licenses/by-nc/4.0/)

Publication
------------------------------------------------------
Lindeboom, T. A., Sanchez Olmos, M. del C., Schulz, K., Brinkmann, C. K., Ramirez Rojas, A. A., Hochrein, L., & Schindler, D. (2022). L-SCRaMbLE creates large-scale genome rearrangements in synthetic Sc2.0 chromosomes. bioRxiv. https://doi.org/10.1101/2022.12.12.519280
