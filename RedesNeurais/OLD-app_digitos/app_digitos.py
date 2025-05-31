# Web App Para Reconhecimento de dígitos

#pip install streamlit-drawable-canvas
# Imports
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import pickle as pkl
from NeuralNetMLP import NeuralNetMLP
#from tensorflow import keras

# Configuração da página
st.set_page_config(page_title = "Reconhecimento de Dígitos", layout = "centered")

# Carrega o modelo treinado

with open("modelo_nn.pickle", "rb") as f:
    model = pkl.load(f)

st.write("## Reconhecimento de Dígitos - Redes Neurais")

with st.container():
    st.subheader("Desenhe um Número")
    
    # Cria o canvas
    canvas_result = st_canvas(stroke_width = 10,
                              stroke_color = "#000000",
                              background_color = "#FFFFFF",
                              update_streamlit = True,
                              height = 280, #300,
                              width = 280, #300,
                              drawing_mode = "freedraw",
                              display_toolbar = True,
                              key = "canvas",)

    # Botão
    predict_button = st.button("Fazer Previsão")

    # Faz a previsão
    if predict_button:
        
        # Captura a imagem desenhada no canvas
        result = (canvas_result.image_data[:, :, :3]).astype(np.uint8)

        # Converte a imagem
        im = Image.fromarray(result).convert("L")

        # Resize e Reshape da imagem
        im = im.resize((28, 28))
        img = np.array(im)
        img = np.invert(np.array([img]))
        #img = img.reshape(1, 28, 28, 1)
        img = img / 255
        img = img.reshape(img.shape[0], 28 * 28) 


        # Converte para Preto e Branco
        # img[img >= 100] = 255
        # img[img < 100] = 0

        # Faz a previsão
        predict = model.predict(img)[0]

        # Imprime na web app
        st.write("Número desenhado: " + str(predict))

st.subheader("")

st.write("")

