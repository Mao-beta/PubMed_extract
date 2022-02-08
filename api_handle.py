# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

from tqdm import tqdm
from Bio import Entrez
import pandas as pd

Entrez.email = pd.read_csv("ignore_files/account.csv")["email"][0]

pmids = [12345678,2345678]
handle = Entrez.efetch(db="pubmed", id=pmids,retmode="xml")
content = handle.read().decode()
handle.close()
print(content)