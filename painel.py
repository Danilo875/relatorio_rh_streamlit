import streamlit as st
import pandas as pd
from datetime import datetime, date
from carregamento_dados import carregar_dados

df = carregar_dados('base.csv')

coluna1, coluna2, coluna3, coluna4 = st.columns([1,1,1,1])

# lang = st.session_state.get("lang", "Português")

# if lang == "Português":

def cria_cartoes(nome_medida, valor, coluna):
    container = coluna.container(border=True)
    with container:
        container.write(nome_medida)
        container.write(f'{valor:,}')
    return container

cont_func = df.shape[0]
cont_lider = len(df[df['lider']==1])
media_span_control = cont_func/cont_lider
custo_pessoas = df['custo_mensal'].sum()

st.write(f'{cont_func:,}')
st.write(f'{cont_lider:,}')
st.write(f'{media_span_control:,.2f}')
st.write(f'R$ {custo_pessoas:,.0f}')

cria_cartoes('Funcionarios', cont_func, coluna1)