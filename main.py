import streamlit as st

def update_language():
    st.session_state.lang = st.session_state.lang_select

if "lang" not in st.session_state:
    st.session_state.lang = "Português"

st.sidebar.selectbox(
    "Idioma/Language:",
    ["Português", "English"],
    index=["Português", "English"].index(st.session_state.lang),
    key="lang_select",
    on_change=update_language
)

lang = st.session_state.lang

if lang == "Português":
    pg = st.navigation(
        {
            "Relatório de RH": [
                st.Page("inicio.py", title="Início"),
                st.Page("painel.py", title="Painel"),
                st.Page("aposentadoria.py", title="Simulador Aposentadoria"),
                st.Page("tabela_extracao.py", title="Tabela para Extração"),
                st.Page("definicoes.py", title="Definições")
            ]
        }
    )

    st.sidebar.write('Links Úteis')
    st.sidebar.markdown("""
    [<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="13" style="vertical-align: middle; margin-right: 5px;">LinkedIn](https://www.linkedin.com/in/danilo-barros-machado-data-analyst/)

    [<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="13" style="vertical-align: middle; margin-right: 5px;">GitHub](https://github.com/Danilo875)
                        
    [<img src="https://cdn-icons-png.flaticon.com/512/337/337946.png" width="13" style="vertical-align: middle; margin-right: 5px;">Currículo (PDF)](https://drive.google.com/file/d/1uwfgQzYqSw8uHj6kSbEOeeTw8POimICi/view?usp=sharing)
    """, unsafe_allow_html=True)

else:
    pg = st.navigation(
        {
            "HR Report": [
                st.Page("inicio.py", title="Home"),
                st.Page("painel.py", title="Dashboard"),
                st.Page("aposentadoria.py", title="Retirement Simulator"),
                st.Page("tabela_extracao.py", title="Extract Table"),
                st.Page("definicoes.py", title="Definitions")
            ]
        }
    )

    st.sidebar.write('Useful Links')
    st.sidebar.markdown("""
    [<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="13" style="vertical-align: middle; margin-right: 5px;">LinkedIn](https://www.linkedin.com/in/danilo-barros-machado-data-analyst/)

    [<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="13" style="vertical-align: middle; margin-right: 5px;">GitHub](https://github.com/Danilo875)
                        
    [<img src="https://cdn-icons-png.flaticon.com/512/337/337946.png" width="13" style="vertical-align: middle; margin-right: 5px;">Resume (PDF)](https://drive.google.com/file/d/1tDclHHK1zFSlv6m2Vzj4JY1CFpeHJoL3/view?usp=sharing)
    """, unsafe_allow_html=True)

pg.run()