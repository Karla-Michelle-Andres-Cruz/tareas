import flet as ft
from controllers.userController import AuthController
from controllers.tareaController import TareaController 
from views.loginView import LoginView
from views.dashboard import DashboardView

def main(page: ft.Page):
    auth_ctrl = AuthController()
    tarea_ctrl = TareaController() 
    
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, auth_ctrl, tarea_ctrl))
            
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacía")])
            )
        page.update()
    
    page.on_route_change = route_change
    page.go("/")
    
def main():
    ft.app(target=start)

if __name__ == "__main__":
    ft.run(main)
    