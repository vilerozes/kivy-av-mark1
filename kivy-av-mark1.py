import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.video import Video


class MyApp(App):
    def build(self):
        video = Video(source='D:/w3b/python-practice/kivy-av-mark2/video-sample/test-two.mp4')
        video.state = 'play'
        video.options = {'eos': 'loop'}
        video.allow_stretch = False
        return video


if __name__ == '__main__':
    MyApp().run()