import flet as ft


def main(page: ft.Page):

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    page.add(
        ft.Column(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ], spacing=0)
    )


    page.add(
        ft.Column(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )    

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", upload_dir="assets/uploads")