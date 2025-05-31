import flet as ft
import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array  

def main(page: ft.Page):

    new_model = tf.keras.models.load_model('modelo_cats_dogs.h5')

    arq = path = name = 0


    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected file:", e.files)
        arq = e.files[0]
        name = arq.name
        path = arq.path
        print(arq, name, path)

        c4 = ft.Container(
            content=ft.Image(src=path, width=300,height=300, 
                             fit=ft.ImageFit.FIT_HEIGHT),
            padding=5,
            margin=0,
        )

        page.controls.pop()
        page.update()

        # Predict
        new_model = tf.keras.models.load_model('modelo_cats_dogs.h5')
        test_image = load_img(path, target_size = (64, 64))
        test_image = img_to_array(test_image)
        test_image = test_image / 255.
        test_image = np.expand_dims(test_image, axis = 0)
        result = new_model.predict(test_image)
        result = result.flatten()[0]
        print(result)
        result = int(round(result.flatten()[0],0))

        if result == 0:
            classe = 'Gato'
        else:
            classe = 'Cachorro'

        previsao = 'Previsão: ' + classe

        c5 = ft.Container(
            content=ft.Text(previsao, size=25, font_family="Arial"),
            padding=5,
            margin=0,
        )

        page.add(

            ft.Column( [c1, c2, c4, c5 ],
                spacing=0 #,
                #expand=False
            )

        )

    # main
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)
    page.update()


    titulo = 'Sistema de classificação de imagens'

    c1 = ft.Container(
        content=ft.Text(titulo, size=25, font_family="Arial"),
        padding=5,
        margin=5,
    )

    c2 = ft.Container(
        content=ft.ElevatedButton("Escolha uma imagem...",
                   on_click=lambda _: file_picker.pick_files(allow_multiple=False)),
        padding=5,
        margin=0,
    )

    page.add(
         ft.Column( [c1, c2 ],
            spacing=0,
            expand=False
        )
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", upload_dir="assets/uploads")