import streamlit as st

# o exemplo abaixo é um dicionário para que a barra de navegação divida os itens em tópicos, caso queira só a lista de nome de páginas
# basta usar uma lista diretamente. Cada página é criada com st.page infromando o arquivo da página e o nome da página na barra lateral
pg = st.navigation(
    {
        "Home": [st.Page("home.py", title="Bem-vindo!")],
        "Dashboard": [st.Page("aposentadoria.py", title="Simulador Aposentadoria"), st.Page("dashboard.py", title="Dashboard")]
    }
)

pg.run()