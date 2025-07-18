import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle 
# formata o valor na moeda brasileira
import locale 

# Esconder os menu padrao
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title('Sistema de Seguro de Saúde')
st.sidebar.title("Informe os dados")

# variaveis 
atributos = ['idade', 'sexo', 'IMC', 'num_filhos', 'fumante', 'regiao']
# prever o 'valor_seguro']

dict_categorias = {'sexo': {'Feminino': 0, 'Masculino': 1},
                   'fumante': {'nao': 0, 'sim': 1},
                   'regiao': {'sul': 0, 'sudeste': 1, 'Norte': 2, 'Nordeste': 3}
                   }

with st.sidebar:

    with st.form(key='my_form'):

        # [ 'idade', 'sexo', 'IMC', 'num_filhos', 'fumante', 'regiao']

        idade = st.number_input('idade', min_value=0, max_value=150, step=1, value=30)

        cat_sexo  = st.selectbox('sexo', options=list(dict_categorias['sexo'].keys()))
        sexo = dict_categorias['sexo'][cat_sexo]

        IMC = st.number_input('IMC', min_value=10.0, max_value=350.0, value=25.0, step=1.0)

        num_filhos = st.number_input('num_filhos', min_value=0, max_value=300, value=2)

        cat_fumante = st.selectbox('fumante',options=list(dict_categorias['fumante'].keys()))
        fumante = dict_categorias['fumante'][cat_fumante]
 
        cat_regiao = st.selectbox('região',options=list(dict_categorias['regiao'].keys()))
        regiao = dict_categorias['regiao'][cat_regiao]

        predict_button = st.form_submit_button(label='Prever')


# Pagina pricipal
arquivo_modelo = 'modelo.pkl'
with open(arquivo_modelo, 'rb') as f:
    modelo = pickle.load(f)

def previsao_seguro(modelo, idade, sexo, IMC, num_filhos, fumante, regiao):

    new_X = np.array([idade, sexo, IMC, num_filhos, fumante, regiao])
    valor_seguro = modelo.predict(new_X.reshape(1, -1) )[0]
    return valor_seguro

imagem = 'seguro.jpeg'

image = Image.open(imagem)
st.image(image, width=500)

if predict_button:
    valor_seguro  = previsao_seguro(modelo, idade, sexo, IMC, num_filhos, fumante, regiao)

    import numpy as np

    #locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    #locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")
    #locale.setlocale(locale.LC_ALL, "es_ES")
    str_valor_seguro  = str(round(valor_seguro,0)) #locale.currency(valor_seguro, grouping=True, symbol=None)
    str_valor_seguro_mensal = str(round(valor_seguro/12,0)) #}ale.currency(valor_seguro / 12, grouping=True, symbol=None)
    st.markdown('## Valor do Seguro (Anual): R$ ' +  str_valor_seguro )
    st.markdown('## Valor Mensal: R$ ' +  str_valor_seguro_mensal )



