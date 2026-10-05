from kivy.app import App
from kivy.uix.label import Label

class VideoBotApp(App):
    def build(self):
        return Label(text='VideoBot V2 OK!\nNo Crash!', font_size=24)

if __name__ == '__main__':
    VideoBotApp().run()
