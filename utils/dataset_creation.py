import numpy as np
import pandas as pd
import encryption
import time
from tqdm import tqdm
import string
import random

np.random.seed(30)


def createDataset(df, algorithm, name):
    """
    Args:
    df(DataFrame): Pandas DataFrame of plaintext files
    algorithm(function): A function of the form algorithm(string,key) that returns a tuple of the form (ciphertext,key)
    name(string): Name of the algorithm without .csv extension. This is what the created dataset will be stored as i.e. name.csv
    """
    # Convert all passwords to strings

    # Generate random seeds
    keys = 26
    randStrings = [randStr() for i in range(keys)]

    keyIsNum = (algorithm == encryption.caesar_cipher)

    start = time.time()
    df['Passwords'] = df['Passwords'].apply(lambda x: str(x))
    # Go to utils/encryption.py to make a function for a different encryption algorithm. Then, replace the
    print("Applying algorithm to passwords")
    if keyIsNum:
        results = df['Passwords'].progress_apply(lambda x: algorithm(
            x, np.random.randint(low=1, high=26))).values
    else:
        results = df['Passwords'].progress_apply(lambda x: algorithm(
            x, randStrings[np.random.randint(low=1, high=26)])).values
    results = list(zip(*results))
    ciphertext = list(results[0])
    keys = list(results[1])

    print(f"Generating the dataset and saving the file as data/{name}.csv")
    # Generating the dataset
    df['ciphertext'] = ciphertext
    df['key'] = keys
    df.to_csv(f'data/{name}.csv', index=False)
    end = time.time()
    print(f"Done in {end-start} seconds.")


def randStr(chars=string.ascii_uppercase + string.digits, N=8):
    return ''.join(random.choice(chars) for _ in range(N))


if __name__ == "__main__":
    tqdm.pandas()  # For progress bar

    # Reading in the text file of passwords
    df = pd.read_csv(
        './data/rockyou.txt',
        delimiter="\n",
        header=None,
        names=["Passwords"],
        encoding="ISO-8859-1",
    )

    maxRows = 200000
    df = df.sample(frac=1)[:maxRows]

    createDataset(df, encryption.caesar_cipher, 'Caesar')
    createDataset(df, encryption.vigenere_cipher, 'Vigenere')
    createDataset(df, encryption.des_encrypt, 'DES')
    createDataset(df, encryption.aes_encrypt, 'AES')
