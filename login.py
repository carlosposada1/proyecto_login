import flet as ft
from flet import(Column)

def main(page: ft.Page):
    page.title = "Bot Company"
    ft.Text(value="LIBERTY")
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    page.bgcolor = "#A9D4D0"
    titulo = ft.Text(value="BOT ACTIVACION MOVIL", font_family="Arial")
    user_gac = ft.TextField(label ="        USER GAC", prefix_icon=ft.icons.PERSON, width=320)
    password_gac = ft.TextField(label="        PASSWORD GAC",  width=320)
    password_udb = ft.TextField(label="        PASSWORD UDB",  width=320)
    greetings = ft.Column()
    subtitulo = ft.Text(value="© TecnoAndroid, Ing. Carlos Posada")
    
    
    img = ft.Image(
        src=f"/assets/tecno.PNG",
        width=200,
        height=110,
        fit=ft.ImageFit.CONTAIN,)
    border_radius=ft.border_radius.all(10),
    images = ft.Row( wrap=False, scroll="always")
    
    c = ft.Container(
        
            ft.Image(
                
                src=f"/assets/tecno.PNG",
                border_radius=ft.border_radius.all(10),
                width=320,
                height=70,
                fit=ft.ImageFit.NONE,
            ),
        
        
         
        width=1920,
        height=70,
        padding=0,
        alignment=ft.alignment.center_left,
        bgcolor="white",
        border_radius=0,
        
        animate_opacity=300,
    ) 
    
    def btn_click(e):
        titulo = ""

        subtitulo = ""
        page.update()
        
    
    c1 = ft.Container(
        ft.Column(controls=[
            
            
            ft.Text(f"BOT ACTIVACION MOVIL", size=16, color="black", font_family="Arial", weight="bold" ),
            ft.Text(f"  ", size=5),
            ft.TextField(label="  USER GAC", prefix_icon=ft.icons.PERSON, width=320),
            ft.TextField(label="        PASSWORD GAC",  width=320),
            ft.TextField(label="        PASSWORD UDB",  width=320),
            
            ft.FilledButton(
            "          Ingresar          ", on_click=btn_click, 
            style=ft.ButtonStyle(
                shape=ft.StadiumBorder(),
            ),
        ),
            ft.Text(value="© TecnoAndroid, Ing. Carlos Posada", weight="bold")
    ],
                  alignment=ft.MainAxisAlignment.CENTER,
                  horizontal_alignment="center",
                  ),
        
        width=350,
        height=410,
        padding=0,
        alignment=ft.alignment.top_center,
        bgcolor="white",
        border_radius=15,
        animate_opacity=300,
        
    )

    
    
    page.add(
        c,
        c1,
        greetings,
        
        
    )
   
    


ft.app(target=main,
       assets_dir="./assets")