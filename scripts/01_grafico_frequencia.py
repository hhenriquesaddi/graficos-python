"""Gráfico de frequência: quantidade de chamados por tipo de atendimento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_frequencia.csv")

freq = df["tipo_atendimento"].value_counts()

fig, ax = plt.subplots(figsize=(9, 5.5))
barras = ax.bar(freq.index, freq.values, color="#4C72B0", edgecolor="black")
ax.bar_label(barras, padding=3)
ax.set_title("Frequência de chamados por tipo de atendimento")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Frequência (nº de chamados)")
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)

fig.tight_layout()
saida = RAIZ / "graficos" / "01_frequencia.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
plt.show()
