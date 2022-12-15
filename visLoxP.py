#!usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ------------------------------
# Name: in silico qPCR Tagging - visLoxP -.
# Purpose:
# PCR - In silico qPCR tagging for synthetic chromosomes
# Author: Maria del Carmen Sanchez
# USAGE: python visLoxP.py genome.fasta fwd_primers.csv rve_primers.csv 700
# Created: October,2022
# ------------------------------
import sys
import regex
import re
import pandas as pd
fasta_file=sys.argv[1]
file_forward=sys.argv[2] #csv file with forward primers
file_reverse=sys.argv[3] #csv file with reverse_complement primers
maximum_amplicon_size=sys.argv[4]
name_fasta_file=fasta_file.split('_')
name_fasta_file=name_fasta_file[0]
print(name_fasta_file)
#Definition of the list
list_forward=[]
list_reverse=[]
list_oligo_names=[]
with open(file_forward,'r') as f1:
    for line in f1.readlines():
        line=line.strip()
        line=line.split(",")
        forward_oligo=line[2]
        name_fwd=line[0]
        list_oligo_names.append(name_fwd)
        list_forward.append(forward_oligo)
with open(file_reverse,'r') as f2:
    for line in f2.readlines():
        line=line.strip()
        line=line.split(",")
        reversec_oligo=line[2]
        list_reverse.append(reversec_oligo)
list_values=[]
count = 0

with open(fasta_file,'r') as input_file:
    for line in input_file.readlines():
        line=line.strip()
    for i in range(0,len(list_forward)):
        for j in range(0,len(list_reverse)):
                if i == j:
                    f_pattern_withoutcase = regex.compile(r'(%s){e<=2}'%list_forward[i], re.IGNORECASE)
                    r_pattern_withoutcase = regex.compile(r'(%s){e<=2}'%list_reverse[j], re.IGNORECASE)

                    if regex.search(f_pattern_withoutcase,line)  and regex.search(r_pattern_withoutcase,line):
                        count=count+1
                        amplicon_size=int(regex.search(r_pattern_withoutcase,line).span()[1])-int(regex.search(f_pattern_withoutcase,line).span()[0])

                        if amplicon_size < 0:
                            list_values.append(0)
                            print(0)
                        elif amplicon_size > int(maximum_amplicon_size):
                            list_values.append(0)
                            print(0)
                        elif amplicon_size == 0:
                            list_values.append(0)
                            print(0)
                        else:
                            list_values.append(1)
                            print(1)
                    else:
                        print(0)


with open("in_silico_pcr_output.txt",'a') as outfile:
    #outfile.write("Oligo_name"+"\t"+ ', '.join(map(str, list_oligo_names))+"\n")
    outfile.write(name_fasta_file+"\t"+', '.join(map(str,list_values))+"\n")
