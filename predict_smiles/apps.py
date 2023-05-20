from django.apps import AppConfig


class PredictSmilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "predict_smiles"


def img_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_base64


def parse_txt():
    import pandas as pd
    import time
    from rdkit import Chem
    from rdkit.Chem import Draw

    # Read the file once it is available
    import pandas as pd
    df_props_smiles = pd.read_csv("predict_smiles/result/result.csv", sep="\t")
    df_props_smiles.columns = ["smiles", "MW", "LogP", "TPSA"]

    df_props_smiles_only_smiles = df_props_smiles["smiles"]
    # Iterate over the SMILES column and convert to images
    images = {}
    for i, smiles in enumerate(df_props_smiles_only_smiles):
        molecule = Chem.MolFromSmiles(smiles)
        if molecule is not None:
            img = Draw.MolToImage(molecule)
            images[smiles] = [df_props_smiles["MW"][i], df_props_smiles["LogP"][i], df_props_smiles["TPSA"][i],
                              img_to_base64(img)]
        else:
            print(f"Invalid SMILES: {smiles}")

    return images


def get_smiles(prop1, prop2, prop3):
    import subprocess
    import numpy as np
    from scipy.spatial.distance import cosine

    target_props = f"{prop1} {prop2} {prop3}"
    commandRunProps = f'docker exec -w /root/CVA 7633e842ba2cf945c282df5e4b49869b60629996c684487634bf8da7dd35e9b8 /bin/bash -c "source activate props && python sample.py --prop_file=smiles_prop.txt --save_file=save/model_1.ckpt-1 --target_prop {target_props} --result_filename=result.csv"'
    commandCopy = r"docker cp 7633e842ba2cf945c282df5e4b49869b60629996c684487634bf8da7dd35e9b8:root/CVA/result.csv C:\Users\aymen\OneDrive\Bureau\piDeployment\predict_smiles\result"
    resultRunProps = subprocess.run(commandRunProps, shell=True, capture_output=True, text=True)
    resultCopy = subprocess.run(commandCopy, shell=True, capture_output=True, text=True)
    images = parse_txt()
    target_vector = np.array([prop1, prop2, prop3], dtype=np.float64)  # Convert the properties to float

    # Calculate the cosine distances between target vector and property vectors
    distances = {}
    for s, image in images.items():
        smiles = s  # Extract SMILES from the image
        image_props = np.array(image[0:3], dtype=np.float64)  # Convert the properties to float
        distance = cosine(target_vector, image_props)
        distances[smiles] = distance

    # Sort the images based on the distances in ascending order
    sorted_images = {smiles: image for smiles, _ in sorted(distances.items(), key=lambda x: x[1])}
    for s, v in images.items():
        sorted_images[s] = v
    print(sorted_images)

    # Return the sorted images
    return sorted_images

