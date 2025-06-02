import streamlit as st
import pandas as pd
from datetime import datetime, date
from carregamento_dados import carregar_dados

df = carregar_dados('base.csv')
df_lider = df[df['lider']==1]
df_lider['dados_gerente'] = df_lider['nome'] + " - ID: " + df_lider['id'].astype(str)

cont_func = df.shape[0]
cont_lider = len(df_lider)
media_span_control = cont_func/cont_lider
custo_pessoas = df['custo_mensal'].sum()

lang = st.session_state.get("lang", "Português")

if lang == "Português":
    container = st.container(border=True)
    with container:
        container.write("###### Painel de filtros")
        coluna_e, coluna_d = st.columns([1,1])
        filtro_lider = coluna_e.selectbox(label='Líder:', options=['Selecione'] + df_lider['dados_gerente'].sort_values().unique().tolist(), index=0)
        filtro_area = coluna_d.selectbox(label='Área:', options=['Selecione'] + df['area'].sort_values().unique().tolist(), index=0)
        filtro_genero = coluna_e.selectbox(label='Gênero:', options=['Selecione'] + df['genero'].sort_values().unique().tolist(), index=0)
        filtro_formacao = coluna_d.selectbox(label='Formação:', options=['Selecione'] + df['formacao'].sort_values().unique().tolist(), index=0)

    cont_func = (f'{cont_func:,}').replace(",",".")
    cont_lider = (f'{cont_lider:,}').replace(",",".")
    media_span_control = (f'{media_span_control:,.2f}').replace(".",",")
    custo_pessoas = (f'R$ {custo_pessoas:,.0f}').replace(",",".")   

    coluna1, coluna2 = st.columns([1,1])

    def cria_cartoes(imagem, nome_medida, valor, coluna):
        container = coluna.container(border=True)
        with container:
            coluna1, coluna2 = st.columns([0.5,1])
            coluna1.image(imagem)
            coluna2.write(nome_medida)
            coluna2.write(valor)

    cria_cartoes('employees.png', 'Quantidade de Funcionarios', cont_func, coluna1)
    cria_cartoes('leadership.png', 'Quantidade de Líderes', cont_lider, coluna2)
    cria_cartoes('average.png', 'Número de Liderados - Média', media_span_control, coluna1)
    cria_cartoes('money.png', 'Custo com pessoal', custo_pessoas, coluna2)

else:
    container = st.container(border=True)
    with container:
        container.write("###### Filters Panel")
        coluna_e, coluna_d = st.columns([1,1])
        filtro_lider = coluna_e.selectbox(label='Leader:', options=['Select'] + df_lider['dados_gerente'].sort_values().unique().tolist(), index=0)
        filtro_area = coluna_d.selectbox(label='Department:', options=['Select'] + df['area'].sort_values().unique().tolist(), index=0)
        filtro_genero = coluna_e.selectbox(label='Gender:', options=['Select'] + df['genero'].sort_values().unique().tolist(), index=0)
        filtro_formacao = coluna_d.selectbox(label='Education:', options=['Select'] + df['formacao'].sort_values().unique().tolist(), index=0)

    cont_func = (f'{cont_func:,}')
    cont_lider = (f'{cont_lider:,}')
    media_span_control = (f'{media_span_control:,.2f}')
    custo_pessoas = (f'R$ {custo_pessoas:,.0f}')

    coluna1, coluna2 = st.columns([1,1])

    def cria_cartoes(imagem, nome_medida, valor, coluna):
        container = coluna.container(border=True)
        with container:
            coluna1, coluna2 = st.columns([0.5,1])
            coluna1.image(imagem)
            coluna2.write(nome_medida)
            coluna2.write(valor)

    cria_cartoes('employees.png', 'Number of Employees', cont_func, coluna1)
    cria_cartoes('leadership.png', 'Number of Managers', cont_lider, coluna2)
    cria_cartoes('average.png', 'Span of Control - Avg', media_span_control, coluna1)
    cria_cartoes('money.png', 'People Cost', custo_pessoas, coluna2)