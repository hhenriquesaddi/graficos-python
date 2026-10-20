"""Gráfico de linhas: evolução diária das vendas por loja."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_linhas.csv", parse_dates=["data"])

fig, ax = plt.subplots(figsize=(11, 6))
for loja, grupo in df.groupby("loja"):
    ax.plot(grupo["data"], grupo["vendas"], marker="o", markersize=4, label=loja)
ax.set_title("Evolução diária das vendas por loja (1º trimestre de 2026)")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas (R$)")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax.legend(title="Loja")
ax.grid(alpha=0.3)
fig.autofmt_xdate()

fig.tight_layout()
saida = RAIZ / "graficos" / "07_linhas.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
plt.show()
