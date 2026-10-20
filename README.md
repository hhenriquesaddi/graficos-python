# Visualização de Dados — Gráficos em Python

Um script independente para cada gráfico, usando `pandas`, `matplotlib` e `seaborn`.

| # | Script | Dados | Gráfico |
|---|--------|-------|---------|
| 1 | `scripts/01_grafico_frequencia.py` | `dados_frequencia.csv` | Frequência de chamados por tipo (barras) |
| 2 | `scripts/02_grafico_dispersao.py` | `dados_dispersao.csv` | Dispersão altura x peso, por sexo |
| 3 | `scripts/03_grafico_boxplot.py` | `dados_boxplot.csv` | Boxplot de salários por departamento |
| 4 | `scripts/04_grafico_barras.py` | `dados_barras.csv` | Barras agrupadas: categoria x região |
| 5 | `scripts/05_grafico_regressao.py` | `dados_regressao.csv` | Regressão linear renda x gasto |
| 6 | `scripts/06_grafico_pizza.py` | `dados_pizza.csv` | Pizza: faturamento por canal |
| 7 | `scripts/07_grafico_linhas.py` | `dados_linhas.csv` | Linhas: vendas diárias por loja |
| 8 | `scripts/08_grafico_heatmap.py` | `dados_heatmap.csv` | Mapa de calor: dia x horário |
| 9 | `scripts/09_grafico_distribuicao.py` | `dados_distribuicao.csv` | Histograma da idade dos clientes |

## Como executar

```bash
pip install -r requirements.txt
python scripts/01_grafico_frequencia.py   # idem para os demais
```

Cada script lê o CSV em `dados/` e salva a imagem em `graficos/`.

## Observações

- Os PDFs reenviados (`*_1`, sufixos aleatórios) têm conteúdo idêntico aos anteriores; há um único CSV e script por conjunto de dados.
- Os dados foram convertidos dos PDFs fornecidos para CSV.
