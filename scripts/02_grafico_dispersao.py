"""Gráfico de dispersão: altura x peso, colorido por sexo."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_dispersao.csv")

cores = {"Masculino": "#1f77b4", "Feminino": "#e377c2"}

fig, ax = plt.subplots(figsize=(9, 6))
for sexo, grupo in df.groupby("sexo"):
    ax.scatter(grupo["altura_cm"], grupo["peso_kg"], label=sexo,
               color=cores[sexo], alpha=0.75, edgecolor="white", s=55)
ax.set_title("Relação entre altura e peso")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Sexo")
ax.grid(alpha=0.3)

fig.tight_layout()
saida = RAIZ / "graficos" / "02_dispersao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
plt.show()
