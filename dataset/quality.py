import os
import gzip
import Bio.PDB as PDB
import csv
import warnings

warnings.filterwarnings('error')

path='/tlbnas/mirror/pdb/data/structures/divided/pdb'
print(os.getcwd())
with open('/home/al820/stabval/dataset/non_red_sampled_PDB.txt', 'r') as file:
    pdbs = list(map(lambda x: x.strip(), file.readlines())) 

file_list = list(map(lambda x: os.path.join(path, x[1:3], 'pdb' + x[0:4] + '.ent.gz'), pdbs))

for i in range(len(file_list)):
    print(pdbs[i])
    try:
        handle = gzip.open(file_list[i], 'rt')
    except FileNotFoundError:
        continue

    parser = PDB.PDBParser()
    try:
        structure = parser.get_structure(pdbs[0], handle)
    except Exception:
        continue
    chainID = pdbs[i][4]
    try:
        dat = {'res': structure.header['resolution'], 'mut':structure.header['compound']['1']['mutation']}
    except KeyError:
        dat = {'res': structure.header['resolution'], 'mut':'no'}

    chain = structure[0][chainID]

    het = {'het_aa': 0, 'het_lig': 0}
    for res in chain.get_residues():
        id = res.id
        if id[0] != ' ' and id[0] != 'W':
            if PDB.Polypeptide.is_aa(id[0].split('_')[1]):
                het['het_aa'] += 1
            else:
                het['het_lig'] +=1

    result_dic = {'name':pdbs[i], **het, **dat}

    print(result_dic)
    with open('quality.csv', 'a') as f:  
        w = csv.DictWriter(f, result_dic.keys())
        if i == 0: w.writeheader()
        w.writerow(result_dic)