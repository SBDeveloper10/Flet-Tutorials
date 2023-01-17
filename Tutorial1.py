import flet as ft


def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 700
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.add(ft.Text(value="Hello World!", size=30))


ft.app(target=main)
