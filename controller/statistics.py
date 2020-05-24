from kivy.factory import Factory
from os import environ
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from kivymd.uix.datatables import MDDataTable
from kivymd.icon_definitions import md_icons


class Statistics(Screen):
    list_tabs_name = list(["Statistic", "Unlocking history", "Notifications History"])
    tabs_created = False
    list_check = [range(10)]
    list_uncheck = [range(1)]

    def on_enter(self):
        self.__init_tabs()
        return

    def on_leave(self, *args):
        self.__remove_tabs()
        return

    def __init_tabs(self):
        self.__init_unlocking_tab()
        self.__init_notification_tab()

    def __init_statistic_tab(self):
        return

    def __init_unlocking_tab(self):

        for x in range(10):
            item = Factory.ThreeLineAvatarIconListItem(id=str(x),
                                                   text="Title",
                                                   secondary_text="Body",
                                                   tertiary_text="Created at")
            item.add_widget(Factory.ImageLeftWidget(source=f'{environ["APP_ASSETS"]}avatar.png'))
            item.add_widget(Factory.IconRightWidget(icon='cancel'))

            self.ids.list_unlocking.add_widget(item)

        for x in range(10):
            item = Factory.ThreeLineAvatarIconListItem(id=str(x),
                                                   text="Username",
                                                   secondary_text="Role",
                                                   tertiary_text="Accessed at")
            item.add_widget(Factory.ImageLeftWidget(source=f'{environ["APP_ASSETS"]}avatar.png'))
            item.add_widget(Factory.IconRightWidget(icon='check-circle'))
            self.ids.list_unlocking.add_widget(item)

        return

    def __init_notification_tab(self):

        for x in self.list_uncheck:
            item = Factory.ThreeLineAvatarIconListItem(id=str(x),
                                                   text="Title.",
                                                   secondary_text="Body",
                                                   tertiary_text="Created at")
            item.add_widget(Factory.ImageLeftWidget(source=f'{environ["APP_ASSETS"]}avatar.png'))
            item.add_widget(Factory.IconRightWidget(icon='bell-alert'))

            self.ids.list_notification.add_widget(item)

        for x in self.list_check:
            item = Factory.ThreeLineAvatarIconListItem(id=str(x),
                                                   text="Title.",
                                                   secondary_text="Body",
                                                   tertiary_text="Created at")
            item.add_widget(Factory.ImageLeftWidget(source=f'{environ["APP_ASSETS"]}avatar.png'))
            item.add_widget(Factory.IconRightWidget(icon='eye-check-outline'))

            self.ids.list_notification.add_widget(item)

        return

    def __noti_seen_check(self):
        return

    def __remove_tabs(self):
        self.ids.list_notification.clear_widgets()
        self.ids.list_unlocking.clear_widgets()

