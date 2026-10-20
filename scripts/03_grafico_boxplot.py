"""Boxplot: distribuição salarial por departamento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_boxplot.csv")

deptos = ["TI", "Marketing", "RH", "Vendas"]
dados = [df.loc[df["departamento"] == d, "salario"] for d in deptos]

fig, ax = plt.subplots(figsize=(9, 6))
bp = ax.boxplot(dados, tick_labels=deptos, patch_artist=True, showmeans=True,
                flierprops=dict(marker="o", markerfacecolor="red", markersize=6))
for caixa, cor in zip(bp["boxes"], ["#4C72B0", "#55A868", "#C44E52", "#8172B2"]):
    caixa.set_facecolor(cor)
    caixa.set_alpha(0.7)
ax.set_title("Distribuição salarial por departamento")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.grid(axis="y", alpha=0.3)

fig.tight_layout()
saida = RAIZ / "graficos" / "03_boxplot.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
plt.show()
