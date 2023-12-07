from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivy.graphics.texture import Texture
import cv2
from kivy.clock import Clock
import subprocess

class MainApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        self.image = Image()
        layout.add_widget(self.image)
        self.save_img_button = MDRaisedButton(
            text="Capture",
            pos_hint={'center_x': .5, 'center_y': 1},
            size_hint=(None, None))
        self.save_img_button.bind(on_press=self.take_picture)
        
        layout.add_widget(self.save_img_button)
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1440)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


        
        Clock.schedule_interval(self.load_video, 1.0/30.0)

        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()

        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def take_picture(self, *args):
        image_name="inputs/image.jpg"
        cv2.imwrite(image_name, self.image_frame)
        subprocess.run(['python', 'omr.py', '-a', '-i', './inputs'])
        # self.show_image_popup()

    # def show_image_popup(self, *args):
    #     # Create a dialog with an image
    #     dialog = MDDialog(
    #         title="Captured Image",
    #         content=KivyImage(source="outputs/CheckedOMRs/image.jpg"),
    #         size_hint=(None, None),
    #         size=("300dp", "300dp"),
    #     )
    #     dialog.open()

if __name__ == '__main__':
    MainApp().run()
