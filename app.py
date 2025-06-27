import streamlit as st
import pandas as pd
import plotly.express as px

# Simulando o carregamento do CSV
data = {
    'id': [0, 1, 2, 3, 4],
    'name': [
        'Sapato vermelho', 
        'Bolsa mais que Velha', 
        'Calça', 
        'Camisa apertadinha', 
        'Vestido Super curto'
    ],
    'price': [96, 8000, 75, 170, 57],
    'category_id': [0, 0, 0, 0, 0]
}
df = pd.DataFrame(data)

st.title("📊 Dashboard de Produtos")

# Mostrar tabela
st.subheader("Tabela de Produtos")
st.dataframe(df)

# Estatísticas
st.subheader("📈 Estatísticas de Preço")
st.write(f"Preço médio: {df['price'].mean():.2f}")
st.write(f"Preço mínimo: {df['price'].min()}")
st.write(f"Preço máximo: {df['price'].max()}")

# Filtro
category_options = df['category_id'].unique()
selected_category = st.selectbox("Filtrar por Categoria", category_options)

df_filtered = df[df['category_id'] == selected_category]

st.subheader("Produtos Filtrados")
st.dataframe(df_filtered)

# Gráfico
st.subheader("Distribuição de Preços")
fig = px.histogram(df, x='price', nbins=10, title='Histograma de Preços')
st.plotly_chart(fig)
