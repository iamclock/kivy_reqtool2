from multiprocessing import current_process
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MainWidget(Widget):
    pass


class Certificate_StuffApp(App):

    def build(self) -> None:
        scrollview_layout: ScrollView = ScrollView()
        anchor_layouts: tuple[AnchorLayout, AnchorLayout] = (AnchorLayout(
            anchor_x="center", anchor_y="center"), )
        box_layout1 = BoxLayout()
        any(
            box_layout1.add_widget(widget)
            for widget in (TextInput(), TextInput()))
        anchor_layouts[0].add_widget(box_layout1)

        box_layout2: BoxLayout = BoxLayout(orientation="vertical")
        buttons: tuple[Button,
                       Button] = (Button(text="Ass"), Button(text="Butt"))

        widgets: tuple[AnchorLayout, AnchorLayout, Button,
                       Button] = (*anchor_layouts, *buttons)
        current_layout: BoxLayout = box_layout2

        any(current_layout.add_widget(widget) for widget in widgets)
        # current_layout: BoxLayout = scrollview_layout.add_widget(current_layout)
        return current_layout


if __name__ == "__main__":
    Certificate_StuffApp().run()