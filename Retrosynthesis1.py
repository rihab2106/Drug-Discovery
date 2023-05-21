#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
from argparse import ArgumentParser
sys.path.append('scripts')
from Retrosynthesis import init_LocalRetro, retrosnythesis
import torch
torch.cuda.is_available()


# In[4]:


torch.version.cuda


# In[2]:


import torch
import sklearn
import torch.nn as nn

from utils import init_featurizer, mkdir_p, get_configure, load_model, load_dataloader, predict







# In[13]:




# In[14]:


default_args = {
    'gpu': 'cuda:0',
    'dataset': 'USPTO_50K_data',
    'config': 'default_config.json',
    'batch_size': 16,
    'num_epochs': 5,
    'patience': 5,
    'max_clip': 20,
    'learning_rate': 1e-4,
    'weight_decay': 1e-6,
    'schedule_step': 10,
    'num_workers': 0,
    'print_every': 20,
    'mode': 'train',
    'device': torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
}



# In[4]:




# In[2]:


# Load the model and necessary files for prediction decoding
dataset = 'USPTO_50K'
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
model_path = 'models/LocalRetro_%s.pth' % dataset
config_path = 'data/configs/default_config.json'
data_dir = 'data/%s' % dataset

args = {'data_dir': data_dir, 'model_path': model_path, 'config_path': config_path, 'device': device}
model, graph_function, atom_templates, bond_templates, template_infos = init_LocalRetro(args)


# In[3]:


target_smiles = {'Lenalidomide': 'O=C1NC(=O)CCC1N3C(=O)c2cccc(c2C3)N',
                 'Salmeterol': 'OCc1cc(ccc1O)[C@H](O)CNCCCCCCOCCCCc2ccccc2',
                 '5-HT6 receptor ligand': 'O=S(=O)(Nc4cc2CCC1(CCC1)Oc2c(N3CCNCC3)c4)c5ccccc5F', 
                 'DDR1_037': 'O=C(Nc4cccc(C(=O)N3CCN(c1ccnc2[nH]ccc12)C3)c4)c5cccc(C(F)(F)F)c5',
                 'DDR1_032': 'Cc3cc2[nH]c(c1cc(CN(C)C)cc(C(F)(F)F)c1)nc2cc3C#Cc4cncnc4'}


# In[5]:



# In[5]:

if __name__ == '__main__':
    parser=ArgumentParser("LocalRetro testing arguements")
    parser.add_argument('--smiles', type=str, default='O=C1NC(=O)CCC1N3C(=O)c2cccc(c2C3)N', help='The smiles of the target molecule')
    parser.add_argument('--model_path', type=str, default='models/LocalRetro_USPTO_50K_data.pth', help='The path of the model')
    parser.add_argument('--config_path', type=str, default='data/configs/default_config.json', help='The path of the config file')
    parser.add_argument('--data_dir', type=str, default='data/USPTO_50K_data', help='The path of the data directory')
    parser.add_argument('--device', type=str, default='cuda:0', help='The device to use')
    args = parser.parse_args()
    smiles = args.smiles
    rest=retrosnythesis(target_smiles["Lenalidomide"], model, graph_function, device, atom_templates, bond_templates, template_infos)
    print(rest)
    #write the result to a file
    with open("result.txt", "w") as f:
        f.write(rest)

