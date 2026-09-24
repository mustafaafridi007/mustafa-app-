from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.05, 0.08, 1)


class Home(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        layout.add_widget(Label(
            text="💻",
            font_size=50
        ))

        layout.add_widget(Label(
            text="MR MUSTAFA AFRIDI",
            font_size=28,
            bold=True
        ))

        layout.add_widget(Label(
            text="Python Developer",
            font_size=20
        ))

        profile = Button(
            text="👤  MY PROFILE",
            font_size=20
        )

        services = Button(
            text="💻  MY SERVICES",
            font_size=20
        )

        contact = Button(
            text="📞  CONTACT ME",
            font_size=20
        )

        about = Button(
            text="ℹ️  ABOUT APP",
            font_size=20
        )

        profile.bind(
            on_press=lambda x: self.open_screen("profile")
        )

        services.bind(
            on_press=lambda x: self.open_screen("services")
        )

        contact.bind(
            on_press=lambda x: self.open_screen("contact")
        )

        about.bind(
            on_press=lambda x: self.open_screen("about")
        )

        layout.add_widget(profile)
        layout.add_widget(services)
        layout.add_widget(contact)
        layout.add_widget(about)

        self.add_widget(layout)

    def open_screen(self, screen):
        self.manager.current = screen


class InfoScreen(Screen):

    def __init__(self, title, message, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        layout.add_widget(Label(
            text=title,
            font_size=30,
            bold=True
        ))

        layout.add_widget(Label(
            text=message,
            font_size=20
        ))

        back = Button(
            text="← BACK",
            font_size=20,
            size_hint_y=None,
            height=60
        )

        back.bind(
            on_press=lambda x: self.go_back()
        )

        layout.add_widget(back)

        self.add_widget(layout)

    def go_back(self):
        self.manager.current = "home"


class MyApp(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(Home(name="home"))

        manager.add_widget(
            InfoScreen(
                name="profile",
                title="MY PROFILE",
                message=
                "Name: Mustafa Afridi\n"
                "Age: 19\n"
                "Field: Python Developer"
            )
        )

        manager.add_widget(
            InfoScreen(
                name="services",
                title="MY SERVICES",
                message=
                "Python Software\n"
                "Web Applications\n"
                "Mobile Applications"
            )
        )

        manager.add_widget(
            InfoScreen(
                name="contact",
                title="CONTACT ME",
                message=
                "Phone: 03255951944"
            )
        )

        manager.add_widget(
            InfoScreen(
                name="about",
                title="ABOUT APP",
                message=
                "Welcome to my professional app.\n\n"
                "Created with Python and Kivy."
            )
        )

        return manager


MyApp().run()