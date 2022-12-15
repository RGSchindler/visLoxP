## visLoxP

Description
--------------------------------------
visLoxP allows the user to simulate a qPCR in a genome of interest by looking for specific pairs of primers.
Then the user have to provide the following files:
1. Query genome in fasta format and in a single line.
2. Set of forward primers in a .csv file format
3. Set of reverse primers in a .csv file format.

Usage
--------------------------------------------
The maximum amplicon size to be found in the query genome has to be define by the user.

Example:

python VisLoxp.py genome.fasta fwd_primers.csv rev_primers.csv 700

Output
-------------------------------------------------
The following output file will be written in a .txt file


----------

