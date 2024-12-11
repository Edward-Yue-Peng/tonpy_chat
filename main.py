import flet as ft
from chat_program.chat_client_class import *
from login import login_view
from chat import chat_view
from five_row import five_row_view


def main(page: ft.Page):
    page.title = "Tonpy"
    page.views.append(login_view(page))
    page.session.set("exception", "")

    def route_change(route):
        page.views.clear()
        if page.route == "/login":
            page.views.append(login_view(page))
            page.update()
        elif page.route == "/chat":
            global client
            client = Client(page.session.get("server_addr"))
            page.views.append(chat_view(page, client))
            page.update()
            client.init_chat()
            client_thread = threading.Thread(
                target=client.run_chat, args=[page], daemon=True
            )
            client_thread.start()
            client.read_input(page.session.get("usrname"))
        elif page.route == "/five_row":
            page.views.append(five_row_view(page, client))
            page.update()

    page.on_route_change = route_change
    page.go("/login")


ft.app(main)
