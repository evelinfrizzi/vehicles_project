import pandas as pd
import plotly.express as px
import streamlit as st

# Título do aplicativo
st.header('Anúncios de Vendas de Carros - Explorador')

# Ler os dados (certifique-se de que o vehicles.csv está na raiz do projeto)
df = pd.read_csv('vehicles.csv')

# 1. Caixa de seleção para o histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer dos veículos')
    # Criar o histograma
    fig_hist = px.histogram(df, x='odometer')
    # Mostrar o gráfico interativo no Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# 2. Caixa de seleção para o gráfico de dispersão (exigência do projeto)
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write(
        'Criando um gráfico de dispersão para preço vs odómetro dos veículos'
    )
    # Criar o gráfico de dispersão (Preço vs Odómetro)
    fig_scatter = px.scatter(df, x='odometer', y='price')
    # Mostrar o gráfico interativo no Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
    