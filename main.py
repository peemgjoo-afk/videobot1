from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

class VideoBotPro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)
        self.is_recording = False
        self.timer = 0

        self.add_widget(Label(text='[b]VideoBot PRO[/b]\nหาเงินจากวิดีโอ', markup=True, font_size=22, size_hint_y=0.2))

        self.status = Label(text='พร้อมถ่าย - กด REC เพื่อเริ่มหาเงิน', font_size=16, size_hint_y=0.15)
        self.add_widget(self.status)

        self.timer_label = Label(text='00:00', font_size=32, size_hint_y=0.15)
        self.add_widget(self.timer_label)

        self.btn_rec = Button(text='🔴 REC เริ่มถ่าย', font_size=20, background_color=(1,0.2,0.2,1), size_hint_y=0.2)
        self.btn_rec.bind(on_press=self.toggle_rec)
        self.add_widget(self.btn_rec)

        row = BoxLayout(spacing=10, size_hint_y=0.15)
        btn_gallery = Button(text='📁 แกลลอรี่')
        btn_gallery.bind(on_press=lambda x: self.update_status('เปิดแกลลอรี่ - ดูวิดีโอที่ถ่าย'))
        btn_share = Button(text='📤 แชร์ขาย')
        btn_share.bind(on_press=lambda x: self.update_status('แชร์ลง TikTok / FB / YT - สร้างรายได้!'))
        row.add_widget(btn_gallery)
        row.add_widget(btn_share)
        self.add_widget(row)

        row2 = BoxLayout(spacing=10, size_hint_y=0.15)
        btn_effect = Button(text='✨ เอฟเฟค')
        btn_effect.bind(on_press=lambda x: self.update_status('เลือกเอฟเฟค - ทำให้วิดีโอน่าสนใจ'))
        btn_money = Button(text='💰 รายได้', background_color=(0.2,0.8,0.2,1))
        btn_money.bind(on_press=lambda x: self.update_status('รายได้วันนี้: 0 บาท - ถ่ายเยอะๆเพื่อเพิ่มรายได้!'))
        row2.add_widget(btn_effect)
        row2.add_widget(btn_money)
        self.add_widget(row2)

        self.add_widget(Label(text='VideoBot V2 PRO - No Crash - Ready to Earn!', font_size=12, size_hint_y=0.1))

    def update_status(self, text):
        self.status.text = text

    def toggle_rec(self, instance):
        if not self.is_recording:
            self.is_recording = True
            self.btn_rec.text = '⏹️ STOP หยุดถ่าย'
            self.btn_rec.background_color = (0.5,0.5,0.5,1)
            self.update_status('🔴 กำลังถ่าย... ถ่ายให้นานเพื่อสร้างคอนเทนต์ขาย!')
            Clock.schedule_interval(self.update_timer, 1)
        else:
            self.is_recording = False
            self.btn_rec.text = '🔴 REC เริ่มถ่าย'
            self.btn_rec.background_color = (1,0.2,0.2,1)
            self.update_status(f'✅ บันทึกเสร็จ {self.timer_label.text} - พร้อมแชร์หาเงิน!')
            Clock.unschedule(self.update_timer)
            self.timer = 0

    def update_timer(self, dt):
        self.timer += 1
        m = self.timer // 60
        s = self.timer % 60
        self.timer_label.text = f'{m:02d}:{s:02d}'

class VideoBotApp(App):
    def build(self):
        return VideoBotPro()

if __name__ == '__main__':
    VideoBotApp().run()
