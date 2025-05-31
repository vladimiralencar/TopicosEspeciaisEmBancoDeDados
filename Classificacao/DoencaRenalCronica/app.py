import flet as ft

categorias_valor = {
    'class': {0: 'Doença Renal Crônica', 1: 'Normal'},
    'bu': {4: '48.1 - 86.2',
       6: '< 48.1',
       2: '200.5 - 238.6',
       0: '124.3 - 162.4',
       5: '86.2 - 124.3',
       1: '162.4 - 200.5',
       7: '≥ 352.9',
       3: '238.6 - 276.7'},
     'sod': {3: '133 - 138',
       4: '138 - 143',
       1: '123 - 128',
       5: '143 - 148',
       6: '148 - 153',
       7: '< 118',
       2: '128 - 133',
       0: '118 - 123',
       8: '≥ 158',
     'pot': {2: '< 7.31', 3: '≥ 42.59', 1: '7.31 - 11.72', 0: '38.18 - 42.59'},
     'stage': {0: 's1', 3: 's4', 2: 's3', 1: 's2', 4: 's5'}}
}


def main(page: ft.Page):

    # Carregar o modelo
    # arquivo_modelo = 'modelo.pkl'
    # with open(arquivo_modelo, 'rb') as f:
    #     modelo = pickle.load(f)

# Atributos

# 'bp (Diastolic)',
#  'bp limit',
#  'ba',
#  'bu',
#  'sod',
#  'pot',
#  'htn',
#  'stage',
#  'affected',
#  'class'
# bp   Blood pressure
# ba   Bacteria
# bu   Blood urea
# sod  Sodium
# pot  Potassium
# htn  Hypertension

# 'Pressão arterial (Diastolica)', 'Pressão Arterial limite', 'Bacteria', 
# 'Urina no Sangue', 'sódio', 'potássico', 'hipertensão', 

#'estágio doença', 'affected',

 # 
    # def previsao_doenca(modelo, pressao_arterial_diastolica, pressão_arterial_limite, 
    #                     bacteria, urina_no_Sangue, sodio, potássio, hipertensao, 
    #                     estagio_doença, affected):

    #     atributos = [ pressao_arterial_diastolica, pressão_arterial_limite, 
    #                         bacteria, urina_no_Sangue, sodio, potássio, hipertensao, 
    #                         estagio_doença, affected]

    #     new_X = np.array(atributos).reshape(1, -1)
    #     doenca = modelo.predict(new_X)[0]
    #     prob_doenca = round(modelo.predict_proba[doenca],0) * 100

    #     if doenca == 0:
    #         diagnostico = 'Não Possui Doença Renal'
    #         imagem = 'doenca_renal_cronica.jpg'
    #     else:
    #         diagnostico = 'Doença Renal Crônica'
    #         imagem = 'normal.jpg'

    # return diagnostico, prob_doenca, imagem

        # Classificar se tem doença e a probabilidade
    def button_clicked(e):

        pressao_arterial_diastolica.value = dd_pressao_arterial_diastolica.value
        page.update()

 
        diagnostico = 'Doença Renal Crônica'
        prob_doenca = 51
        # diagnostico, prob_doenca = previsao_doenca(modelo, pressao_arterial_diastolica, pressão_arterial_limite, 
        #                 bacteria, urina_no_Sangue, sodio, potássio, hipertensao, 
        #                 estagio_doença, affected)

        saida1 = ft.Text(f"Diagnostico:  {diagnostico}", size=32, font_family="Arial")
        saida2 = ft.Text(f"Probabilidade:  {prob_doenca} %", size=30, font_family="Arial")



        #return saida1, saida2
        page.add(saida1)
        page.add(saida2)

        page.update()
    

# Pagina Principal

    # container = ft.Container(
    #     width=200,
    #     height=200,
    #     border=ft.border.all(1, ft.colors.BLACK),
    #     content=ft.FilledButton("Primary color"),
    #     theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE_200)))
    
    # page.add(container)
    page.theme = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary=ft.colors.BLUE,
        primary_container=ft.colors.BLUE_200
    ))
    #page.theme = ft.Theme(color_scheme_seed='blue')
  #  page.update()

    color_dropdown = ft.Dropdown(width=100, options=[ 
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
                ])
    page.title = "Sistema de Clasificação de Doença Renal"
    titulo = 'Sistema de Clasificação de Doença Renal'
    titulo_pagina = ft.Text(titulo, size=40, font_family="Arial")
    imagem_abertura = ft.Image(src=f"/images/image_abertura.jpg",
             width=300,height=300
                    #fit=ft.ImageFit.SCALE_DOWN,
                    #border_radius=ft.border_radius.all(10)
                    )
    submit_btn = ft.ElevatedButton(text="Prever", on_click=button_clicked)

    page.padding = 5
    page.margin = 5


    c1 = ft.Container(
        content=ft.Text(titulo, size=25, font_family="Arial"),
        padding=5,
        margin=5,
    )

    c2 = ft.Container(
        content=ft.Image(src=f"/images/image_abertura_02.jpg"),
             # width=300,height=300),
        # bgcolor=ft.colors.YELLOW,
        padding=5,
        margin=0,

    )

    c3 = ft.Container(
        content=ft.ElevatedButton(text="Prever", on_click=button_clicked),
        padding=5,
        margin=0
    )
    page.add(
         ft.Column( [c1, c2 , c3 ],
            spacing=0,
            expand=False
        )
    )

    dd_pressao_arterial_diastolica = ft.Dropdown( width=100, options=[ 
                ft.dropdown.Option("Não"),
                ft.dropdown.Option("Sim"),
                ])
    page.add(dd_pressao_arterial_diastolica)
    str_pressao_arterial_diastolica = dd_pressao_arterial_diastolica.value
    #page.add(str_pressao_arterial_diastolica)
    page.add(ft.Text(str_pressao_arterial_diastolica, font_family="Arial"))


 #   pressão_arterial_limite, 
    #                         bacteria, urina_no_Sangue, sodio, potássio, hipertensao,

# 'Pressão arterial (Diastolica)', 'Pressão Arterial limite', 'Bacteria', 
# 'Urina no Sangue', 'sódio', 'potássico', 'hipertensão', 

   # color_dropdown = ft.Dropdown(width=100, options=[ 
   #              ft.dropdown.Option("Não"),
   #              ft.dropdown.Option("Sim")
   #              ])

   #  page.add(color_dropdown) #, submit_btn)
    page.update()



    # page.add(saida1)
    # page.add(saida2)

ft.app(
    target=main,
    assets_dir="assets"
)


