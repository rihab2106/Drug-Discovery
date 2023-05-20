from rdkit.Chem.Descriptors import ExactMolWt
from rdkit.Chem.Crippen import MolLogP
from rdkit.Chem.rdMolDescriptors import CalcNumHBD
from rdkit.Chem.rdMolDescriptors import CalcNumHBA
from rdkit.Chem.rdMolDescriptors import CalcTPSA
from rdkit import Chem
from rdkit.Chem.Descriptors import ExactMolWt
from rdkit.Chem.Crippen import MolLogP
from rdkit.Chem.rdMolDescriptors import CalcTPSA

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_filename', help='filename for smiles', type=str, default='smiles.txt')
parser.add_argument('--output_filename', help='name of output file', type=str, default='smiles_prop.txt')
args = parser.parse_args()

def cal_prop(s):
    m = Chem.MolFromSmiles(s)
    if m is None : return None
    return Chem.MolToSmiles(m), ExactMolWt(m), MolLogP(m), CalcTPSA(m)
    #return Chem.MolToSmiles(m), ExactMolWt(m), MolLogP(m), CalcNumHBD(m), CalcNumHBA(m), CalcTPSA(m)

with open(args.input_filename) as f:
    smiles = f.read().split('\n')[:-1]

data = []
for s in smiles:
    d = cal_prop(s)
    if d is None:
        continue
    data.append(d)

with open(args.output_filename, 'w') as w:
    for d in data:
        w.write(d[0] + '\t' + str(d[1]) + '\t'+ str(d[2]) + '\t'+ str(d[3]) + '\n')
