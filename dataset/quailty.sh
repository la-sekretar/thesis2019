#!/bin/bash
path='/tlbnas/mirror/pdb/data/structures/divided/pdb'
cat non_red_sampled_PDB.txt | cut -c 1-4 | \
while read line; do echo $path/$(echo $line | cut -c 2-3)/pdb$line.ent.gz; done 

#echo $filenames | while read line;
#do echo $line;
#done
