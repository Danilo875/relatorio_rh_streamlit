import streamlit as st
import pandas as pd
from datetime import datetime, date
from carregamento_dados import carregar_dados

df = carregar_dados('base.csv')

lang = st.session_state.get("lang", "Português")

if lang == "Português":
    st.title('Simulador de Aposentadoria')

    container = st.container(border=True)
    with container:
        df = df.rename(columns={
            'area': 'Área',
            'posicao': 'Posição',
            'formacao': 'Formação',
            'genero': 'Gênero',
            'qtd_liderados': 'Qtd. Liderados',
            'nome': 'Nome'
        })

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
        df_atributo['Homens'] = df_atributo['Homens'].apply(lambda x: f"{x:,}".replace(",", "."))
        df_atributo['Mulheres'] = df_atributo['Mulheres'].apply(lambda x: f"{x:,}".replace(",", "."))
        df_atributo['Total'] = df_atributo['Total'].apply(lambda x: f"{x:,}".replace(",", "."))
        df_atributo = df_atributo.reset_index()
        df_atributo.columns.name = None
        st.dataframe(df_atributo)

        st.write('### Tabela de funcionários (extração em .csv)')
        st.dataframe(df.drop(['data_nascimento', 'custo_mensal', 'Formação', 'lider'], axis=1))
else:
    st.title('Retirement Simulator')

    container = st.container(border=True)
    with container:
        df = df.rename(columns={
            'area': 'Department',
            'posicao': 'Position',
            'formacao': 'Education',
            'genero': 'Gender',
            'qtd_liderados': 'Direct Reports',
            'nome': 'Name'
        })

        st.write('Select the minimum retirement age in your country and see the number of employees who meet the criteria:')

        coluna1, coluna2 = st.columns([1,1])
        idade_minina_homem = coluna1.number_input("Male:", step=1, min_value=55, max_value=120)
        idade_minina_mulher = coluna2.number_input("Female:", step=1, min_value=55, max_value=120)
        data_simulacao = coluna1.date_input('Select a date to simulate future scenarios:', min_value='today', max_value=datetime(2100,12,31), format="MM/DD/YYYY")
        data_simulacao = datetime.combine(data_simulacao, datetime.min.time())

        df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], errors='coerce')
        df['Age'] = (data_simulacao - df['data_nascimento']).dt.days // 365

        df_homens = df[(df['Age']>=idade_minina_homem) & (df['Gender']=='Masculino')]
        df_mulheres = df[(df['Age']>=idade_minina_mulher) & (df['Gender']=='Feminino')]
        df = pd.concat([df_homens, df_mulheres])

        atributo = coluna2.selectbox(label='Select how you want to distribute the data:', options=['Department', 'Position', 'Education'], index=0)
        df_atributo = pd.crosstab(df[atributo], df['Gender'])
        df_atributo = df_atributo.rename(columns={
            'Masculino': 'Men',
            'Feminino': 'Women'
        })
        df_atributo['Total'] = df_atributo.sum(axis=1)
        df_atributo.loc['Total'] = df_atributo.sum(axis=0)
        df_atributo['Men'] = df_atributo['Men'].apply(lambda x: f"{x:,}")
        df_atributo['Women'] = df_atributo['Women'].apply(lambda x: f"{x:,}")
        df_atributo['Total'] = df_atributo['Total'].apply(lambda x: f"{x:,}")
        df_atributo = df_atributo.reset_index()
        df_atributo.columns.name = None
        st.dataframe(df_atributo)

        st.write('### Employee Data Table (exports in .csv)')
        st.dataframe(df.drop(['data_nascimento', 'custo_mensal', 'Education', 'lider'], axis=1))