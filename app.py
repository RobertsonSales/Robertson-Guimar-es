import streamlit as st 
import Dashboard, Contato, Inicial, Sobre

page = st.sidebar.selectbox('**Menu de opções:**', ['Inicial','Dashboard', 'Sobre', 'Contato'])

st.title('ROBERTSON GUIMARÃES')
#st.write('**Escolha uma opção no menu lateral**')

if page == 'Inicial':
  Inicial.init()

if page == 'Dashboard':
  Dashboard.Dash()

if page == 'Sobre':
  Sobre.Sobre()

if page == 'Contato':
  Contato.cont()

