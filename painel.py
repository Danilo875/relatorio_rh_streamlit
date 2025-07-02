import streamlit as st
import pandas as pd
import plotly.express as px
from carregamento_dados import carregar_dados

df = carregar_dados('base.csv')
df_lider = df[df['lider']==1]

lang = st.session_state.get("lang", "Português")

if lang == "Português":
    container = st.container(border=True)
    with container:
        container.write("###### Painel de filtros")
        coluna_e, coluna_d = st.columns([1,1])
        filtro_lider = coluna_e.selectbox(label='Líder:', options=['Selecione'] + df_lider['nome'].sort_values().unique().tolist(), index=0)
        filtro_area = coluna_d.selectbox(label='Área:', options=['Selecione'] + df['area'].sort_values().unique().tolist(), index=0)
        filtro_genero = coluna_e.selectbox(label='Gênero:', options=['Selecione'] + df['genero'].sort_values().unique().tolist(), index=0)
        filtro_formacao = coluna_d.selectbox(label='Formação:', options=['Selecione'] + df['formacao'].sort_values().unique().tolist(), index=0)

    if filtro_lider != 'Selecione':
        df = df[df['nome']==filtro_lider.split(" -")[0]]
    if filtro_area != 'Selecione':
        df = df[df['area']==filtro_area]
    if filtro_genero != 'Selecione':
        df = df[df['genero']==filtro_genero]
    if filtro_formacao != 'Selecione':
        df = df[df['formacao']==filtro_formacao]

    if filtro_lider != 'Selecione':
        cont_func = df['qtd_liderados'].sum()
    else:
        cont_func = df.shape[0]
    cont_lider = len(df[df['lider']==1])
    media_span_control = cont_func/cont_lider
    custo_pessoas = df['custo_mensal'].sum()
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

    df = df.rename(columns={
            'area': 'Área',
            'posicao': 'Posição',
            'formacao': 'Formação',
            'genero': 'Gênero'
        })
    atributo = st.selectbox(label='Selecione como quer distribuir os dados:', options=['Área', 'Posição', 'Gênero', 'Formação'], index=0)
    df_grafico = df.groupby(atributo, as_index=False)["qtd_liderados"].sum()
    df_grafico = df_grafico.sort_values(by="qtd_liderados", ascending=False)
    fig1 = px.bar(df_grafico, x=atributo, y="qtd_liderados", text="qtd_liderados", title=f"Número de Funcionários por {atributo}")

    fig1.update_layout(
        plot_bgcolor="white",
        title_x=0.1,
        yaxis_title="Qtd. Funcionários",
        yaxis=dict(showgrid=False)
    )
    fig1.update_traces(textposition='outside')

    df_grafico = df[df['lider']==1].groupby("Gênero", as_index=False).size().rename(columns={'size': 'Total'})
    fig2 = px.pie(
    df_grafico,
    names="Gênero",
    values="Total",
    title="Liderança por Gênero",
    hole=0.4,
    color="Gênero",
    color_discrete_map={
        "Feminino": "#A8337D",
        "Masculino": "#1E90FF"
    }
)
    
    df_grafico = df.groupby(atributo, as_index=False)["custo_mensal"].sum()
    df_grafico = df_grafico.sort_values(by="custo_mensal", ascending=True)
    fig3 = px.bar(df_grafico, x="custo_mensal", y=atributo, text="custo_mensal", title=f"Custo com Pessoas por {atributo}")

    fig3.update_layout(
        plot_bgcolor="white",
        title_x=0.1,
        xaxis_title=None,
        yaxis_title=None
    )
    fig3.update_traces(textposition='inside')

    container = st.container(border=True)
    with container:
        container.plotly_chart(fig1, use_container_width=True)
        coluna_e, coluna_d = st.columns([1,1])
        coluna_e.plotly_chart(fig2, use_container_width=True)
        coluna_d.plotly_chart(fig3, use_container_width=True)

else:
    container = st.container(border=True)
    with container:
        container.write("###### Filters Panel")
        coluna_e, coluna_d = st.columns([1,1])
        filtro_lider = coluna_e.selectbox(label='Leader:', options=['Select'] + df_lider['nome'].sort_values().unique().tolist(), index=0)
        filtro_area = coluna_d.selectbox(label='Department:', options=['Select'] + df['area'].sort_values().unique().tolist(), index=0)
        filtro_genero = coluna_e.selectbox(label='Gender:', options=['Select'] + df['genero'].sort_values().unique().tolist(), index=0)
        filtro_formacao = coluna_d.selectbox(label='Education:', options=['Select'] + df['formacao'].sort_values().unique().tolist(), index=0)

    if filtro_lider != 'Select':
        df = df[df['nome']==filtro_lider.split(" -")[0]]
    if filtro_area != 'Select':
        df = df[df['area']==filtro_area]
    if filtro_genero != 'Select':
        df = df[df['genero']==filtro_genero]
    if filtro_formacao != 'Select':
        df = df[df['formacao']==filtro_formacao]

    if filtro_lider != 'Selecione':
        cont_func = df['qtd_liderados'].sum()
    else:
        cont_func = df.shape[0]
    cont_lider = len(df[df['lider']==1])
    media_span_control = cont_func/cont_lider
    custo_pessoas = df['custo_mensal'].sum()
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

    df = df.rename(columns={
            'area': 'Department',
            'posicao': 'Position',
            'formacao': 'Education',
            'genero': 'Gender'
        })
    atributo = st.selectbox(label='Select how you want to display data:', options=['Department', 'Position', 'Gender', 'Education'], index=0)
    df_grafico = df.groupby(atributo, as_index=False)["qtd_liderados"].sum()
    df_grafico = df_grafico.sort_values(by="qtd_liderados", ascending=False)
    fig1 = px.bar(df_grafico, x=atributo, y="qtd_liderados", text="qtd_liderados", title=f"Number of Employees by {atributo}")

    fig1.update_layout(
        plot_bgcolor="white",
        title_x=0.1,
        yaxis_title="# Employees",
        yaxis=dict(showgrid=False)
    )
    fig1.update_traces(textposition='outside')

    df_grafico = df[df['lider']==1].groupby("Gender", as_index=False).size().rename(columns={'size': 'Total'})
    fig2 = px.pie(
    df_grafico,
    names="Gender",
    values="Total",
    title="Leadership by Gender",
    hole=0.4,
    color="Gender",
    color_discrete_map={
        "Feminino": "#A8337D",
        "Masculino": "#1E90FF"
    }
)
    
    df_grafico = df.groupby(atributo, as_index=False)["custo_mensal"].sum()
    df_grafico = df_grafico.sort_values(by="custo_mensal", ascending=True)
    fig3 = px.bar(df_grafico, x="custo_mensal", y=atributo, text="custo_mensal", title=f"People Cost by {atributo}")

    fig3.update_layout(
        plot_bgcolor="white",
        title_x=0.1,
        xaxis_title=None,
        yaxis_title=None
    )
    fig3.update_traces(textposition='inside')

    container = st.container(border=True)
    with container:
        container.plotly_chart(fig1, use_container_width=True)
        coluna_e, coluna_d = st.columns([1,1])
        coluna_e.plotly_chart(fig2, use_container_width=True)
        coluna_d.plotly_chart(fig3, use_container_width=True)
