from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class VideoBotApp(App):
    def build(self):
        return Label(text='VideoBot V2 OK!\nNo Crash!', font_size='24sp')

if __name__ == '__main__':
    VideoBotApp().run()
