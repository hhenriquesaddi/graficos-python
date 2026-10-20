"""Gráfico de pizza: participação de cada canal no faturamento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_pizza.csv")

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%",
       startangle=90, counterclock=False, pctdistance=0.8,
       colors=plt.cm.Set2.colors, wedgeprops=dict(edgecolor="white", linewidth=2))
ax.set_title("Faturamento por canal de venda")

fig.tight_layout()
saida = RAIZ / "graficos" / "06_pizza.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
plt.show()
