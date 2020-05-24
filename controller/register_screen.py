from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.theming import ThemableBehavior


class RegisterScreen(Screen):
    """Registration screen. Opens when the application starts."""

    title = StringProperty()
