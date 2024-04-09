# %%

import pandas as pd
import requests
import json
#%%
# PAGINA COM OS DADOS GERAIS
urlDados = "http://127.0.0.1:5001/dados"

response = requests.get(urlDados)

if response.status_code == 200:

  results = response.json()
  print("Requisição feita com sucesso!.")
else:
  print("Problema na requisição.")

results
# %%

# %%
df_dados = pd.read_json(results)

df_dados
# %%
