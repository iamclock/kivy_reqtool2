from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (520, 700)


class TabsView(TabbedPanel):
    pass


class ServerRootdirView(BoxLayout):
    pass


class CertsSettingsView(BoxLayout):
    pass


class FirstPageView(BoxLayout):
    """First and main widget to generate keys, create requests
    and get certificate to the rootdir folder setting in ServerRootdirView
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        layouts_to_add = (
            TabsView(),
            ServerRootdirView(),
            CertsSettingsView(),
        )
        self.orientation = "vertical"
        any(self.add_widget(layout) for layout in layouts_to_add)
        # btns: tuple[Button, Button] = (Button(text="Do it!"), )
        # any(self.add_widget(btn) for btn in btns)
        return


class RequestToolApp(App):
    pass


if __name__ == '__main__':
    RequestToolApp().run()
