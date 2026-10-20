"""Gráfico de barras agrupadas: vendas médias por categoria e região."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_barras.csv")

tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")
tabela = tabela.loc[df["categoria"].unique(), ["Norte", "Sul", "Leste", "Oeste"]]

ax = tabela.plot(kind="bar", figsize=(10, 6), width=0.8, edgecolor="black")
ax.set_title("Vendas médias por categoria e região")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias (R$)")
ax.legend(title="Região")
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)
plt.xticks(rotation=0)

plt.tight_layout()
saida = RAIZ / "graficos" / "04_barras.png"
plt.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
plt.show()
