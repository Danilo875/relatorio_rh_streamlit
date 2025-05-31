import streamlit as st
import pandas as pd
from datetime import datetime, date
from data_loader import carregar_dados

df = carregar_dados('base.csv')

# criando coluna de idade
df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], format="%d/%m/%Y")
df['idade'] = (datetime.today() - df['data_nascimento']).dt.days // 365

st.title('Simulador de Aposentadoria')
# genero_escolhido = st.text_input("Digite um gênero para filtrar a tabela:")
# genero_escolhido = st.selectbox(label= 'Genêro', options=['Selecione uma opção', 'Masculino', 'Feminino'], index=0)
container = st.container(border=True)
with container:
    st.write('Selecione a idade mínina para aposentadoria no seu país e veja o número de funcionários que atendem aos critérios:')
    coluna1, coluna2 = st.columns([1,1])
    idade_minina_homem = coluna1.number_input("Masculino:", step=1, min_value=55, max_value=120)
    idade_minina_mulher = coluna2.number_input("Feminino:", step=1, min_value=55, max_value=120)
    data_simulacao = coluna1.date_input('Selecione uma data para simular o futuro:', min_value='today', max_value=datetime(2100,12,31), format="DD/MM/YYYY")
    data_simulacao = datetime.combine(data_simulacao, datetime.min.time())
    df['idade_simulacao'] = (data_simulacao - df['data_nascimento']).dt.days // 365

    df_homens = df[(df['idade_simulacao']>=idade_minina_homem) & (df['genero']=='Masculino')]
    df_mulheres = df[(df['idade_simulacao']>=idade_minina_mulher) & (df['genero']=='Feminino')]
    df = pd.concat([df_homens, df_mulheres])
    df = df.rename(columns={
        'area': 'Área',
        'Masculino': 'Homens',
        'Feminino': 'Mulheres',
        'posicao': 'Posição',
        'formacao': 'Formação',
        'genero': 'Gênero',
        'qtd_liderados': 'Qtd Liderados'
    })

# st.write(f'Qtd homens: {df_homens.shape[0]}, qtd mulheres: {df_mulheres.shape[0]}')
    atributo = coluna2.selectbox(label='Selecione como quer distribuir os dados:', options=['Área', 'Posição', 'Formação'], index=0)
    df_atributo = pd.crosstab(df[atributo], df['Gênero'])
    df_atributo['Total'] = df_atributo.sum(axis=1)
    df_atributo.loc['Total'] = df_atributo.sum(axis=0)
    df_atributo = df_atributo.reset_index()
    df_atributo.columns.name = None
    st.dataframe(df_atributo)

    st.write('### Tabela de funcionários para download em .csv')
    st.dataframe(df.drop(['data_nascimento', 'custo_mensal', 'idade', 'idade_simulacao', 'lider'], axis=1))