from kivy.app import App
from GUI.views import CustomLayout


class MainApp(App):

    def build(self):
        root = CustomLayout()
        return root


