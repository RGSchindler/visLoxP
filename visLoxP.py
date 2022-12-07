#!usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ------------------------------
# Name: in silico qPCR Tagging - visLoxP -.
# Purpose:
# PCR - In silico qPCR tagging for synthetic chromosomes
# Author: Maria del Carmen Sanchez
# USAGE: python visLoxP.py genome.fasta list_fwd_primers.csv list_rve_primers.csv
# OUTPUT: file with values for negative and positive in silico amplifications.
# Created: October,2022
# ------------------------------
import sys
fasta_file=sys.argv[1]
file_forward=sys.argv[2] #csv file with forward primers
file_reverse=sys.argv[3] #csv file with reverse_complement primers
name_fasta_file=fasta_file.split('_')
name_fasta_file=name_fasta_file[0]

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
                    if line.find(str(list_forward[i]))  and line.find(str(list_reverse[j])) :
                        count=count+1
                        #print(list_forward[i],line.find(str(list_forward[i])),str(list_reverse[j]),line.find(str(list_reverse[j])))
                        amplicon_size=int(line.find(str(list_reverse[j])))-int(line.find(str(list_forward[i])))
                        if amplicon_size < 0:
                            list_values.append(0)
                            #print(0)
                        elif amplicon_size > 1000:
                            list_values.append(0)
                            #print(0)
                        elif amplicon_size == 0:
                            list_values.append(0)
                            #print(0)
                            #print(list_forward[i], line.find(str(list_forward[i])), str(list_reverse[j])line.find(str(list_reverse[j])))
                        else:
                            list_values.append(1)
                            #print(1)
                            #print(list_forward[i], line.find(str(list_forward[i])), str(list_reverse[j]),
                                  #line.find(str(list_reverse[j])))
                    else:
                        pass

with open("in_silico_pcr_output.txt",'a') as outfile:
    #outfile.write("Oligo_name"+"\t"+ ', '.join(map(str, list_oligo_names))+"\n")
    outfile.write(name_fasta_file+"\t"+', '.join(map(str,list_values))+"\n")
