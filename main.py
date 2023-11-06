from kivy.app import App
from kivy.uix.image import Image



class КомандорApp(App):
    def build(self):
        img = Image(source="kom.png",
                    size_hint=(1, 1),
                    pos_hint={"center_x": .5, "top": 1.2, })  # "center_y":.5,"top":1,})

        return img


if __name__ == "__main__":
    КомандорApp().run()