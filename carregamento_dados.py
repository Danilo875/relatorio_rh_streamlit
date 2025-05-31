import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados(base):
    df = pd.read_csv(base, sep=";")
    df = df.rename(columns={
        'area': 'Área',
        'posicao': 'Posição',
        'formacao': 'Formação',
        'genero': 'Gênero',
        'qtd_liderados': 'Qtd. Liderados',
        'nome': 'Nome'
    })
    return df