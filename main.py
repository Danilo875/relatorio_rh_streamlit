import streamlit as st

# o exemplo abaixo é um dicionário para que a barra de navegação divida os itens em tópicos, caso queira só a lista de nome de páginas
# basta usar uma lista diretamente. Cada página é criada com st.page infromando o arquivo da página e o nome da página na barra lateral
pg = st.navigation(
        {
            "Relatório de RH":
            [
                st.Page("inicio.py", title="Início"), 
                st.Page("painel.py", title="Dashboard"), 
                st.Page("aposentadoria.py", title="Simulador Aposentadoria"),
                st.Page("tabela_extracao.py", title="Tabela para Extração"),
                st.Page("definicoes.py", title="Definições")
            ]
        }
)

st.sidebar.write('Links Úteis')
st.sidebar.markdown("""
[<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="13" style="vertical-align: middle; margin-right: 5px;"> LinkedIn](https://www.linkedin.com/in/danilo-barros-machado-data-analyst/)

[<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="13" style="vertical-align: middle; margin-right: 5px;"> GitHub](https://github.com/Danilo875)
                    
[<img src="https://cdn-icons-png.flaticon.com/512/337/337946.png" width="13" style="vertical-align: middle; margin-right: 5px;"> Currículo (PDF)](https://drive.google.com/file/d/1uwfgQzYqSw8uHj6kSbEOeeTw8POimICi/view?usp=sharing)

""", unsafe_allow_html=True)


pg.run()