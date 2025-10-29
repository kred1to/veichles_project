import os
import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles.csv")

st.header("Análise Exploratória de Dados: Anúncios de Vendas de Carros")

st.write("Visualizando parte dos dados")
st.dataframe(car_data.head())

hist_button = st.button('Criar histograma')
if hist_button:
    st.write("Criando um histograma para o conjunto de dados de anúncios de vendas de carros")
    fig = px.histogram(car_data, x="odometer", nbins=50, title="Distribuição do Odômetro dos Veículos Anunciados")
    st.plotly_chart(fig, use_container_width=True)

scatter_check = st.checkbox('Criar gráfico de dispersão (Preço x Odômetro)')

if scatter_check:
    st.write("Criando um gráfico de dispersão: relação entre Preço e Odômetro")
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Preço x Odômetro")
    st.plotly_chart(fig_scatter, use_container_width=True)
