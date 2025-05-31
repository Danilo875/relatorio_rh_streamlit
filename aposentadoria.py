import streamlit as st
import pandas as pd
from datetime import datetime, date
from carregamento_dados import carregar_dados

df = carregar_dados('base.csv')

st.title('Simulador de Aposentadoria')

container = st.container(border=True)
with container:
    st.write('Selecione a idade mínina para aposentadoria no seu país e veja o número de funcionários que atendem aos critérios:')

    coluna1, coluna2 = st.columns([1,1])
    idade_minina_homem = coluna1.number_input("Masculino:", step=1, min_value=55, max_value=120)
    idade_minina_mulher = coluna2.number_input("Feminino:", step=1, min_value=55, max_value=120)
    data_simulacao = coluna1.date_input('Selecione uma data para simular cenários futuros:', min_value='today', max_value=datetime(2100,12,31), format="DD/MM/YYYY")
    data_simulacao = datetime.combine(data_simulacao, datetime.min.time())

    df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], format="%d/%m/%Y")
    df['Idade'] = (data_simulacao - df['data_nascimento']).dt.days // 365

    df_homens = df[(df['Idade']>=idade_minina_homem) & (df['Gênero']=='Masculino')]
    df_mulheres = df[(df['Idade']>=idade_minina_mulher) & (df['Gênero']=='Feminino')]
    df = pd.concat([df_homens, df_mulheres])

    atributo = coluna2.selectbox(label='Selecione como quer distribuir os dados:', options=['Área', 'Posição', 'Formação'], index=0)
    df_atributo = pd.crosstab(df[atributo], df['Gênero'])
    df_atributo = df_atributo.rename(columns={
        'Masculino': 'Homens',
        'Feminino': 'Mulheres'
    })
    df_atributo['Total'] = df_atributo.sum(axis=1)
    df_atributo.loc['Total'] = df_atributo.sum(axis=0)
    df_atributo = df_atributo.reset_index()
    df_atributo.columns.name = None
    st.dataframe(df_atributo)

    st.write('### Tabela de funcionários para download em .csv')
    st.dataframe(df.drop(['data_nascimento', 'custo_mensal', 'Formação', 'lider'], axis=1))