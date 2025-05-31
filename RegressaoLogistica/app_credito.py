import streamlit as st
import numpy as np
from PIL import Image
import pickle 

# Esconder os menu padrao
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title('Previsão de Crédito')
st.sidebar.title("Informe os dados")

# classficar se pode receber crédito e a sua probabilidade]
def previsao_credito(modelo, saldo_conta, duracao_credito_meses, 
                    status_pagamento_credito_anterior, valor_credito, idade):

    new_X = np.array([saldo_conta, duracao_credito_meses, status_pagamento_credito_anterior,
                      valor_credito, idade])
    classificacao_credito = modelo.predict(new_X.reshape(1, -1) )[0]
    probs = modelo.predict_proba(new_X.reshape(1, -1) )[0]
    prob = round(probs[classificacao_credito] * 100,0)

    print(classificacao_credito, probs)

    if classificacao_credito == 1:
        status_credito = ':blue[Crédito Aprovado]'
    else:
        status_credito = ':red[Crédito Negado]'

    return status_credito, prob


with st.sidebar:
    with st.form(key='my_form'):

        saldo_conta = st.number_input('Saldo Conta', min_value=0, max_value=1000000, step=100, value=3000)

        duracao_credito_meses = st.number_input('duração do crédito (meses)',
                                     min_value=0, max_value=72, step=1, value=12)

        status_pagamento_credito_anterior = 3 

        valor_credito = st.number_input('Valor Crédito', min_value=250, 
                                                        max_value=150000, step=250, value=2000)

        idade = st.number_input('idade', min_value=0, max_value=150, step=1, value=30)


        predict_button = st.form_submit_button(label='Prever')


def previsao_credito(modelo, saldo_conta, duracao_credito_meses, 
                    status_pagamento_credito_anterior, valor_credito, idade):

    new_X = np.array([saldo_conta, duracao_credito_meses, status_pagamento_credito_anterior,
                      valor_credito, idade])

    classificacao_credito = modelo.predict(new_X.reshape(1, -1) )[0]
    probs = modelo.predict_proba(new_X.reshape(1, -1) )[0]
    prob = round(probs[classificacao_credito] * 100,0)

    print(classificacao_credito, probs)

    if classificacao_credito == 1:
        status_credito = ':blue[Crédito Aprovado]'
    else:
        status_credito = ':red[Crédito Negado]'

    return status_credito, prob


# Pagina pricipal
arquivo_modelo = "modelo_credito.pkl"
with open(arquivo_modelo, 'rb') as f:
    modelo = pickle.load(f)

imagem = 'credito.jpeg'
image = Image.open(imagem)
st.image(image, width=500)

if predict_button:
    classificacao_credito, prob  = previsao_credito(modelo, saldo_conta, duracao_credito_meses, 
                    status_pagamento_credito_anterior, valor_credito, idade)

    st.markdown('## Classificação: ' +  classificacao_credito )
    st.markdown('## Probabilidade: '  +  str(prob) + ' %' )


