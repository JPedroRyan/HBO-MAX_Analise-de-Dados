import streamlit as st

# Adicionando um titulo a página (Apenas uma assinatura como forma de identificação)
st.set_page_config(page_title="Pedro Ryan")

#Container 1º, titulo e logo da HBO MAX
with st.container():
    st.title('Análise da Base - HBO MAX')

    #Adicionando o link de um Gif da logo HBO MAX
    gif_url = 'https://images.squarespace-cdn.com/content/v1/52adf1abe4b0dbce9d210136/1604798976116-DX27OWGAXKUYDG9RIDKY/HBO+Max+-+Kutko+Article+GIF.gif?format=2500w'
    st.image(gif_url, use_column_width=True) #Comando para exibir o Gif

#Container 2º, explicando oque a base de dados
with st.container():
    st.title('Oque é a Base da HBO MAX?')
    st.write('A Base da HBO MAX é basicamente uma lista com o catalago de filmes e séries, onde também está detalhando o seu gênero sendo ação, comedia, romance entre outros mais.')
    st.write('Além dessas informações a base de dados fornece informações de onde mais os filmes e séries estão disponiveis, exemplos de outras plataformas de streaming como "Amazon Prime", "Netflix" e etc.')


    #Adicionando o link de um Gif da plataforma HBO MAX
    gif_url = 'https://images.squarespace-cdn.com/content/v1/52adf1abe4b0dbce9d210136/1604110439985-ZMHFGV7B48XOF35I14I2/HBO+Max+-+Family+Section+GIF.gif?format=2500w'
    st.image(gif_url, use_column_width=True) #Comando para exibir o Gif

#Container 3º, detalhando como funciona a base de dados
with st.container():
    st.title('Detalhes da base de dados')
    st.write('Informações de como funciona a base, especificação das colunas:')
    st.markdown('* **title:** Corresponde ao nome do filme ou série.')
    st.markdown('* **type:** Identifica o tipo do conteúdo se e do tipo filme (movie) ou série (TV).')
    st.markdown('* **year:** Ano de lançamento.')
    st.markdown('* **rating:** Avaliação do filme ou série.')
    st.markdown('* **year:** Ano de lançamento.')
    st.markdown('* **imdb_score:** Nota de avaliação do IMDB.')
    st.markdown('* **rotten_score:** Pontuação podre, mostra a potuação negativa do filme ou série.')
    st.markdown('* **decade:** Periodo de decada (periodo de 10 anos).')
    st.markdown('* **imdb_bucket:** Média de avaliação IMDB.')
    st.markdown('* **genres:** Referece ao gênero do filme ou série, a várias colunas de gênero cada uma para ação, comedia, romance e etc. Essas colunas recebem valores de 0 (False) é 1 (True) para o gênero pertencido.')
    st.markdown('* **platforms:** Referece a plataforma em que o filme e série se encontra, no mesmo modelo da coluna "genres" são várias colunas com nomes de plataformas onde recem valores de verdadeiro e falso para cada caso.')

