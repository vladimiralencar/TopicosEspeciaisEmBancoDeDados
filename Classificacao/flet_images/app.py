import flet as ft

def main(page: ft.Page):




    #t = ft.Text(value="Hello, world!", color="green")
    #page.controls.append(t)
    # file_picker = ft.FilePicker()
    # page.overlay.append(file_picker)
    # page.update

    # file_picker = ft.FilePicker()
    # page.overlay.append(file_picker)
    # page.update()

    # # file = ft.ElevatedButton("Choose file...",
    # #         on_click=lambda _: file_picker.pick_files(allow_multiple=False))

    # page.add(ft.ElevatedButton("Choose file...",
    #         on_click=lambda _: file_picker.pick_files(allow_multiple=False)))

    # file = page.file_picker.file

    # print(file)

    # def on_dialog_result(e: ft.FilePickerResultEvent):
    #     print("Selected file:", e.files)
    #     print("Selected file or directory:", e.path)

    #     return e.files

    # file_picker = ft.FilePicker(on_result=on_dialog_result)
    # print(file_picker)


    # def upload_files(e):
    #     upload_list = []
    #     if file_picker.result != None and file_picker.result.files != None:
    #         for f in file_picker.result.files:
    #             upload_list.append(
    #                 FilePickerUploadFile(
    #                     f.name,
    #                     upload_url=page.get_upload_url(f.name, 600),
    #                 )
    #             )
    
    # file_picker = ft.FilePicker()
    # files = file_picker.upload()

    files = [ 'teste']

    #btn = ft.ElevatedButton("Upload", on_click=ft.FilePicker().upload(files))
    page.add(
        ft.ElevatedButton("Upload", on_click=ft.FilePicker().upload(files))
        )

ft.app(target=main)

