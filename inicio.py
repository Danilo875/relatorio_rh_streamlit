import streamlit as st

lang = st.session_state.get("lang", "Português")

if lang == 'Português':
    st.title('Relatório de RH')
else:
    st.title('HR Report')