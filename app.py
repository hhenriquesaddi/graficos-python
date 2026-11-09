import streamlit as st

# 1. Configuração Inicial da Página
st.set_page_config(
    page_title="Dashboard de Visualização de Dados",
    page_icon="📊",
    layout="wide"
)

# 2. Sidebar com as Informações do Aluno (Recolhível automaticamente pelo Streamlit)
with st.sidebar:
    st.header("📋 Identificação do Aluno")
    st.markdown("---")
    st.markdown("**Nome:** Henrique Saddi")
    st.markdown("**Número da Chamada:** _[Preencher nº]_")
    st.markdown("**Turma:** Banco de Dados II (BD2)")
    st.markdown("---")
    st.caption("Atividade 06 - Engenharia de Dados")

# 3. Título Central do Dashboard
st.title("📊 Dashboard Exploratório — Visualização de Dados")
st.subheader("Análise estática dos gráficos gerados na Atividade 06")
st.markdown("---")

# URL base do repositório para carregar as imagens diretamente do GitHub Raw
base_url = "https://githubusercontent.com"

# 4. Estrutura dos Gráficos e Suas Respectivas Análises
# Cada item contém: (Nome do arquivo de imagem, Título do Gráfico, Texto de Análise)
graficos_info = [
    (
        "01_grafico_frequencia.png", 
        "1. Frequência de Chamados", 
        "O gráfico de barras ilustra a distribuição volumétrica de chamados por tipo de ocorrência. Permite identificar gargalos operacionais e quais categorias demandam maior alocação de equipe de suporte técnico."
    ),
    (
        "02_grafico_dispersao.png", 
        "2. Dispersão Altura x Peso", 
        "A análise de dispersão segmentada por sexo demonstra a correlação física entre as duas variáveis. A distribuição dos pontos ajuda a identificar agrupamentos comportamentais e padrões antropomórficos distintos."
    ),
    (
        "03_grafico_boxplot.png", 
        "3. Boxplot de Salários", 
        "O diagrama de caixas (boxplot) mapeia a distribuição salarial por departamento. Evidencia a amplitude salarial, a mediana de cada setor e a presença de eventuais valores discrepantes (outliers) na folha de pagamento."
    ),
    (
        "04_grafico_barras.png", 
        "4. Categoria x Região", 
        "A disposição em barras agrupadas compara a penetração de categorias mercadológicas em diferentes regiões geográficas, sendo fundamental para direcionar estratégias de expansão e logística regional."
    ),
    (
        "05_grafico_regressao.png", 
        "5. Regressão Renda x Gasto", 
        "A linha de tendência ajustada sobre a dispersão confirma uma correlação linear positiva: à medida que a renda mensal aumenta, os gastos acompanham proporcionalmente, indicando elasticidade de consumo."
    ),
    (
        "06_grafico_pizza.png", 
        "6. Faturamento por Canal", 
        "O gráfico de setores (pizza) exibe a participação percentual de cada canal nas receitas totais da empresa. Ideal para identificar quais plataformas de venda são mais representativas no ecossistema de negócios."
    ),
    (
        "07_grafico_linhas.png", 
        "7. Vendas Diárias por Loja", 
        "O gráfico de linhas temporais monitora a evolução do volume de vendas diárias. A sobreposição das linhas permite comparar o desempenho histórico entre unidades e detectar padrões de sazonalidade semanal."
    ),
    (
        "08_grafico_heatmap.png", 
        "8. Mapa de Calor (Dia x Horário)", 
        "O gradiente de cores destaca visualmente as faixas de horário e dias da semana com maior densidade de acessos ou transações, servindo de base para o provisionamento de infraestrutura em horários de pico."
    ),
    (
        "09_grafico_distribuicao.png", 
        "9. Histograma de Idade", 
        "O histograma detalha a curva de distribuição etária da base de clientes. A análise do formato da curva revela se o público-alvo concentra-se em uma faixa jovem, adulta ou se possui distribuição uniforme."
    )
]

# 5. Renderização dos Gráficos em Matriz 3x3 (Três a Três)
# Divide a lista em blocos de 3 para iterar sobre as linhas do Streamlit
for i in range(0, len(graficos_info), 3):
    cols = st.columns(3) # Cria 3 colunas paralelas na interface
    
    for j in range(3):
        if i + j < len(graficos_info):
            img_file, titulo, analise = graficos_info[i + j]
            with cols[j]:
                st.markdown(f"### {titulo}")
                # Renderiza a imagem diretamente do repositório
                st.image(f"{base_url}{img_file}", use_container_width=True)
                # Exibe a análise logo abaixo do gráfico correspondente
                st.info(analise)
    
    st.markdown("---") # Linha divisória entre as fileiras de gráficos
