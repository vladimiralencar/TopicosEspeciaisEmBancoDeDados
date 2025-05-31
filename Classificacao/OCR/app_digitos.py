# Web App Para OCR

# Imports
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
from tensorflow import keras

# Configuração da página
st.set_page_config(page_title = "Bonus Web App DSA", layout = "centered")

# Carrega o mapeamento
mapping = np.loadtxt('mapeamento.txt', dtype = int, usecols = (1), unpack = True)

# Dicionário
char_labels = {}

# Loop para carregar o mapeamento
for i in range(47):
    char_labels[i] = chr(mapping[i])

# Carrega o modelo treinado
model = keras.models.load_model('modelo')

with st.container():
    st.subheader("Desenhe um Número ou Letra! Eu sou uma aplicação de IA e tentarei descobrir o que você desenhou!")
    
    # Cria o canvas
    canvas_result = st_canvas(stroke_width = 10,
                              stroke_color = "#000000",
                              background_color = "#FFFFFF",
                              update_streamlit = True,
                              height = 300,
                              width = 300,
                              drawing_mode = "freedraw",
                              display_toolbar = True,
                              key = "canvas",)

    # Botão
    guess = st.button("Fazer Previsão")

    # Faz a previsão
    if guess:
        
        # Captura a imagem desenhada no canvas
        result = (canvas_result.image_data[:, :, :3]).astype(np.uint8)

        # Converte a imagem
        im = Image.fromarray(result).convert("L")

        # Resize e Reshape da imagem
        im = im.resize((28, 28))
        img = np.array(im)
        img = np.invert(np.array([img]))
        img = img.reshape(1, 28, 28, 1)
        img = img / 255

        # Faz a previsão
        predict = model.predict(img)  

        # Imprime na web app
        st.write("Processamento concluído! Você desenhou um: " + char_labels[np.argmax(predict)])

st.subheader("Instruções:")

st.write("Reconhecimento Óptico de Caracteres (OCR) é a capacidade de um computador interpretar corretamente uma entrada manuscrita. "
         "Nesta web app executamos um modelo de aprendizado de máquina usando redes neurais artificiais, que é capaz de identificar uma "
         "imagem e prever a saída que o computador acha que a imagem se assemelha.")

st.write("Obrigado!")
