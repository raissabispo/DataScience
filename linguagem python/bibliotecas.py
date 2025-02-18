import pandas as pd
import numpy as np

df = pd.DataFrame({
  "ID": range(1,6),
  "IDADE": np.random.randint(20,40, size=5),
  "Salário": np.random.randint(2000,5000,size=5)
})

df.to_csv("dados.csv", index=False)
df_carregado = pd.read_csv("dados.csv")

print("Média salarial:", df_carregado["Salário"].mean())