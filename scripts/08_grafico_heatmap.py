"""Mapa de calor: movimento de clientes por dia da semana e horário."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "dados" / "dados_heatmap.csv")

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
horas = ["8:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
matriz = (df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
            .loc[dias, horas])

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(matriz, annot=True, fmt="d", cmap="YlOrRd", linewidths=0.5,
            cbar_kws={"label": "Nº de clientes"}, ax=ax)
ax.set_title("Movimento de clientes por dia da semana e horário")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")

fig.tight_layout()
saida = RAIZ / "graficos" / "08_heatmap.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
plt.show()
