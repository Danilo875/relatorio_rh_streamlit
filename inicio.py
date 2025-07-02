import streamlit as st

lang = st.session_state.get("lang", "Português")

if lang == 'Português':
    st.markdown("""
        # Bem-vindo ao Projeto de Análise de Dados de RH

        Este projeto foi desenvolvido utilizando as bibliotecas **Streamlit**, **Pandas** e **Plotly**, oferecendo uma interface interativa e visualizações dinâmicas para facilitar a análise dos dados de recursos humanos.

        ## Funcionalidades do Projeto

        - **Seletor de Idiomas:** Disponível em Português e Inglês, para atender diferentes perfis de usuários.
        - **Navegação Intuitiva:** O painel lateral contém as páginas:
        - **Início:** Informações sobre o projeto.
        - **Painel:** Visualizações gráficas com filtros interativos para análise detalhada.
        - **Simulador de Aposentadoria:** Permite verificar quantos colaboradores poderiam se aposentar, possibilitando planejamento e tomada de ações para evitar perdas de conhecimentos importantes e criar uma cadeia de sucessão.
        - **Tabela para Extração:** Possibilita aplicar filtros e exportar os dados dos funcionários em formato `.csv` para análises externas.

        ## Sobre Mim

        Sou analista de dados com sólida experiência em **Python**, **Excel**, **SQL** e **Power BI**.
         
        Tenho experiência prática no desenvolvimento de soluções que combinam análise de dados e visualização para apoiar decisões estratégicas. Este projeto reflete minha capacidade de integrar diferentes tecnologias para entregar resultados eficientes e acessíveis.
    """)
else:
    st.markdown("""
    # Welcome to the HR Data Analysis Project

    This project was developed using **Streamlit**, **Pandas**, and **Plotly**, providing an interactive interface and dynamic visualizations to facilitate human resources data analysis.

    ## Project Features

    - **Language Selector:** Available in Portuguese and English to accommodate different user profiles.
    - **Intuitive Navigation:** The sidebar contains the following pages:
    - **Home:** Project information.
    - **Dashboard:** Graphical visualizations with interactive filters for detailed analysis.
    - **Retirement Simulator:** Allows you to check how many employees could retire, it makes possible to the user to plan and take actions to avoid significant knowledge loss and create a succession chain.
    - **Extract Table:** Enables filtering and exporting employee data in `.csv` format for external analysis.

    ## About Me
                
    I am a data analyst with solid experience in **Python**, **Excel**, **SQL**, and **Power BI**.

    I have practical experience developing solutions that combine data analysis and visualization to support strategic decisions. This project reflects my ability to integrate different technologies to deliver efficient and accessible results.
    """)