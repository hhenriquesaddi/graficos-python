"""Regressão linear simples: renda mensal x gasto mensal."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_regressao.csv")

x, y = df["renda_mensal"], df["gasto_mensal"]
a, b = np.polyfit(x, y, 1)          # y = a*x + b
r2 = np.corrcoef(x, y)[0, 1] ** 2
xs = np.linspace(x.min(), x.max(), 100)

fig, ax = plt.subplots(figsize=(9, 6))
ax.scatter(x, y, alpha=0.7, color="#4C72B0", edgecolor="white", label="Observações")
ax.plot(xs, a * xs + b, color="red", linewidth=2,
        label=f"Regressão: y = {a:.3f}x + {b:.1f}  (R² = {r2:.3f})")
ax.set_title("Regressão linear: renda mensal x gasto mensal")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()
saida = RAIZ / "graficos" / "05_regressao.png"
fig.savefig(saida, dpi=150)
print(f"y = {a:.4f}x + {b:.2f} | R² = {r2:.4f}")
print(f"Gráfico salvo em {saida}")
plt.show()
