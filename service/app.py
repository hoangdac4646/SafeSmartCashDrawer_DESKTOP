import ast
import os
import sys

from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

from controller.dialog_change_theme import KitchenSinkDialogChangeTheme
from controller.expansionpanel import KitchenSinkExpansionPanelContent
import controller.register_screen

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    sys.path.append(os.path.abspath("main.py"))
else:
    sys.path.append(os.path.abspath("main.py"))
    os.environ["APP_ROOT"] = os.path.dirname(os.path.abspath("main.py"))
os.environ["APP_ASSETS"] = os.path.join(
    os.environ["APP_ROOT"], f"assets{os.sep}"
)


class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "LightGreen"
        self.dialog_change_theme = None
        self.toolbar = None
        self.data_screens = {}

    def build(self):

        Builder.load_file(
            f"{os.environ['APP_ROOT']}/view/register_screen.kv"
        )

        return Builder.load_file(
            f"{os.environ['APP_ROOT']}/view/start_screen.kv"
        )

    def show_dialog_change_theme(self):
        if not self.dialog_change_theme:
            self.dialog_change_theme = KitchenSinkDialogChangeTheme()
            self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

    def on_start(self):
        """Creates a list of items with examples on start screen."""
        exec('from controller.register_screen import RegisterScreen')
        screen_object = eval('RegisterScreen()')
        manager = self.root.ids.screen_manager
        manager.add_widget(screen_object)
        manager.current = 'register screen'

    def set_screen(self, name_screen):
        manager = self.root.ids.screen_manager
        if not manager.has_screen(
            self.data_screens[name_screen]["name_screen"]
        ):
            name_kv_file = self.data_screens[name_screen]["kv_string"]
            Builder.load_file(
                f"{os.environ['APP_ROOT']}/view/{name_kv_file}.kv"
            )
            if "Import" in self.data_screens[name_screen]:
                exec(self.data_screens[name_screen]["Import"])
            screen_object = eval(self.data_screens[name_screen]["Factory"])
            self.data_screens[name_screen]["object"] = screen_object
            if "toolbar" in screen_object.ids:
                screen_object.ids.toolbar.title = name_screen
            manager.add_widget(screen_object)
        manager.current = self.data_screens[name_screen]["name_screen"]

    def back_to_home_screen(self):
        self.root.ids.screen_manager.current = "home"

    def callback_for_menu_items(self, *args):
        from kivymd.toast import toast

        toast(args[0])

    def add_expansion_panel(self, card):
        content = KitchenSinkExpansionPanelContent()
        card.add_widget(
            MDExpansionPanel(
                icon=f"{os.environ['APP_ASSETS']}avatar.png",
                content=content,
                panel_cls=MDExpansionPanelOneLine(text="KivyMD v.0.102.1"),
            )
        )

    """def init_register_screen(self):
        return Builder.load_file(
            f"{os.environ['APP_ROOT']}/view/register_screen.kv"
        )"""

    def init_home_screen(self):
        Builder.load_file(
            f"{os.environ['APP_ROOT']}/view/base_content.kv"
        )
        Builder.load_file(
            f"{os.environ['APP_ROOT']}/view/toolbar.kv"
        )
        Builder.load_file(
            f"{os.environ['APP_ROOT']}/view/list_items.kv"
        )
        Builder.load_file(
            f"{os.environ['APP_ROOT']}/view/dialog_change_theme.kv"
        )

        # import screens from file
        with open(f"{os.getcwd()}/screens_data.json") as read_file:
            self.data_screens = ast.literal_eval(read_file.read())
            data_screens = list(self.data_screens.keys())

        for name_item in data_screens:
            self.root.ids.backdrop_front_layer.data.append(
                {
                    "viewclass": "KitchenSinkOneLineLeftIconItem",
                    "text": name_item,
                    "icon": self.data_screens[name_item]["icon"],
                    "on_release": lambda x=name_item: self.set_screen(
                        x
                    ),
                }
            )

        self.back_to_home_screen()




