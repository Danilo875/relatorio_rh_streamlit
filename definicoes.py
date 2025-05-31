import streamlit as st

lang = st.session_state.get("lang", "Português")

if lang == 'Português':
    st.write(f'{lang}')
else:
    st.write('Português é o melhor')