import streamlit as st

#st.set_page_config(layout='centered', page_title="Robertson Guimarães")

def Sobre():
        
    #st.write("<h1><center>Informações sobre o autor do projeto</center><h1>", unsafe_allow_html=True)
    #st.subheader('O autor e suas publicações')

    cam_arq_1 = 'Foto Sales.jpeg'
    st.image(cam_arq_1, caption='O autor', width=200)

    with st.expander('Vídeos do autor sobre seus livros:'):
        st.write('Sou Robertson Guimarães - Escritor')
        st.write('Conheça meu canal no Youtube [clicando aqui:]("https://www.youtube.com/@iscutaqui")')
        st.write('Liberdade de Escolha - Nos domínios da Fé:[Clique aqui:](https://www.youtube.com/watch?v=-54gY8EsFvI)')
        st.write('A Ciência da Separação - Da indignação e respeito:[Clique aqui:](https://www.youtube.com/watch?v=YDvvE9adOJM&t=1s)')
        #st.write('A Ciência da União - Da da ilusão à realidade:[Clique aqui:](https://loja.uiclap.com/titulo/ua27600/?srsltid=AfmBOoqy5Tfbc0x5kBseyMLAWr9Fdp1iYN-0H8QCTYUgaAUqfR-YaUqf)')    

    #st.divider()

    radio = st.radio("Conheça melhor o autor, através dos vídeos já publicados:", 
        options=["Apresentação do Canal Iscutaqui",
                "A Parábola da Farinha - Uma reflexão sobre a generalização",
                "Política - A arte de transformar por argumentos, indicadores e indicações!"])

    if radio == "Apresentação do Canal Iscutaqui":
        VIDEO_URL = "https://youtu.be/dBaD-bH9m3Q"
        st.video(VIDEO_URL)

    if radio == "A Parábola da Farinha - Uma reflexão sobre a generalização":
        VIDEO_URL = "https://www.youtube.com/watch?v=c7Fso0cvKlQ&t=170s"
        st.video(VIDEO_URL)

    if radio== "Política - A arte de transformar por argumentos, indicadores e indicações!":
        VIDEO_URL = "https://www.youtube.com/watch?v=6hpXRliEWoM"
        st.video(VIDEO_URL)


    #st.subheader('Músicas preferidas do autor:')

    #cam_arq_2 = './images/Brasil.mp3'
    #st.audio(cam_arq_2)

    st.write('Quer assistir mais videos do autor? [Clique Aqui: ](https://www.youtube.com/@iscutaqui)')