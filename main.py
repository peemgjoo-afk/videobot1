from kivy.app import App
from kivy.uix.label import Label
class VideoBotApp(App):
    def build(self):
        return Label(text='VideoBot Build OK!')
VideoBotApp().run()
