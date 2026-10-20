"""Histograma: distribuição da idade dos clientes."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_distribuicao.csv")

media, mediana = df["idade"].mean(), df["idade"].median()

fig, ax = plt.subplots(figsize=(9, 6))
sns.histplot(df["idade"], bins=range(15, 75, 3), kde=True, color="#4C72B0",
             edgecolor="black", ax=ax)
ax.axvline(media, color="red", linestyle="--", label=f"Média: {media:.1f} anos")
ax.axvline(mediana, color="green", linestyle="-.", label=f"Mediana: {mediana:.1f} anos")
ax.set_title("Distribuição da idade dos clientes")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Frequência (nº de clientes)")
ax.legend()
ax.grid(axis="y", alpha=0.3)

fig.tight_layout()
saida = RAIZ / "graficos" / "09_distribuicao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
plt.show()
