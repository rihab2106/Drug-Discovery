import subprocess
import pandas as pd
from django.apps import AppConfig
import pathlib

def img_to_base64(image):
    import base64
    from io import BytesIO

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_base64

def get_result(smiles):
    from rdkit import Chem
    from rdkit.Chem import Draw

    # Read the file once it is available
    import pandas as pd
    df_retro = pd.read_csv("retrosynthesis/result/result1.csv")
    df_retro.columns = ["id","SMILES", "Predicted site", "Local reaction template", "Score", "Molecule"]
    print(df_retro.columns)

    df_retro_smiles_only_smiles = df_retro["SMILES"]
    # Iterate over the SMILES column and convert to images
    images = {}
    for i, smiles in enumerate(df_retro_smiles_only_smiles):
        molecule = Chem.MolFromSmiles(smiles)
        if molecule is not None:
            img = Draw.MolToImage(molecule)
            images[smiles] = [df_retro["Predicted site"][i], df_retro["Local reaction template"][i],
                              df_retro["Score"][i], img_to_base64(img)]
        else:
            print(f"Invalid SMILES: {smiles}")
    return images


def run(smiles: str):
    import subprocess
    smiles=f"{smiles}"
    # Run a Bash command
    commandRetro = f'docker exec -w /root/LocalRetro 86e78deda109f5e80be5ac131390ec8aa32f43f4ff0dee6e4aee4afbbab27aea python Retrosynthesis1.py --smiles "{smiles}"'
    commandCopy = r'docker cp 86e78deda109f5e80be5ac131390ec8aa32f43f4ff0dee6e4aee4afbbab27aea:root/LocalRetro/result1.csv C:\Users\aymen\OneDrive\Bureau\piDeployment\retrosynthesis\result'
    resultRetro = subprocess.run(commandRetro, shell=True, capture_output=True, text=True)
    resultCopy = subprocess.run(commandCopy, shell=True, capture_output=True, text=True)
    print(resultRetro)
    print(resultCopy)
    return get_result(smiles)



class RetrosynthesisConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "retrosynthesis"
    path ="retrosynthesis"



