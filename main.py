from flet import *
from pydux import create_store
from store import store


def main(page: Page):
    page.window_width = 300
    ct = Text(store.get_state(),size=30,weight="bold")
    store.subscribe(lambda:updatestate())

    def updatestate():
        ct.value = store.get_state()
        page.update()

    def addnew(e):
        store.dispatch({'type': 'INCREMENT'})


    def decnew(e):
        store.dispatch({'type': 'DECREMENT'})

    page.add(
        Column([
            Text(f"Pydux Store "),
           Row([
             ElevatedButton("add", on_click=addnew),
            ct,
            ElevatedButton("decrement", on_click=decnew)
            ],alignment="spaceBetween")
        ])
    )

flet.app(target=main)
