class Button:
    def press():
        print("Button presed")

class WebButton(Button):
    def press():
        print("Web button presed")

class WindowsButton(Button):
    def press():
        print("Windows button presed")


class Dialog:
    def create_button():
        return Button()
    

class WebDialog(Dialog):
    def create_button():
        return WebButton()
    
class WindowsDialog(Dialog):
    def create_button():
        return WindowsButton



class App():
    def __init__(self, os) -> None:
        self.dialog = None
        self.button = None
         
        match os:
            case "windows":
                self.dialog = WindowsDialog
            case "web":
                self.dialog = WebDialog()
            case _:
                self.dialog = Dialog()
            
    def dialog_render(self):
        self.button = self.dialog.create_button()

    def button_presed(self):
        self.button.press()


app = App("windows")
app.dialog_render()
app.button_presed()
