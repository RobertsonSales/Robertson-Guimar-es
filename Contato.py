import streamlit as st
from datetime import datetime

def cont():
        
    st.subheader('Fale com o autor')
    #st.write("<h1><center>Envie sua mensagem, logo entraremos em contato.</center><h1>", unsafe_allow_html=True)


    with st.form('Formulário de contato'):
        nome= st.text_input('Nome:', max_chars=100)
        nome= st.text_input('E-mail:', max_chars=60)
        dt_nasc= st.date_input('Informe sua data de nascimento: ', min_value=datetime(1900,1,1))
        hr= st.time_input('Informe sua melhor hora para contatos: ')
        vr= st.slider('Selecione um valor que você possa doar, entre R$ 25 e R$ 100: ', min_value=25, max_value=100, value=25, step=15)
        mens= st.text_area('Informe sua necessidade:', max_chars=400)
        btn=st.form_submit_button('Enviar')

    if btn:
        st.success(f'Mensagem enviada com sucesso! Logo entraremos em contato, Sr(a): {nome}')
