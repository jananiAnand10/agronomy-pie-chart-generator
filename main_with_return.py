from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import matplotlib.pyplot as plt

class MainScreen(Screen):
    pass

class TemperatureScreen(Screen):
    pass

class MoistureScreen(Screen):
    pass

class WaterScreen(Screen):
    pass

class iotapp(App):
    def build(self):
        sm = ScreenManager()

        # Create a main screen
        main_screen = MainScreen(name='main')
        layout = RelativeLayout()

        background_image = Image(source='main_page.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        b1_button = Button(
            background_normal='temp_icon.png',
            size_hint=(None, None),
            size=(110, 100),
            border=(0, 0, 0, 0),
            pos=(120, 60)
        )

        b2_button = Button(
            background_normal='moisture_icon.png',
            size_hint=(None, None),
            size=(110, 100),
            border=(0, 0, 0, 0),
            pos=(340, 60)
        )

        b3_button = Button(
            background_normal='water_icon.png',
            size_hint=(None, None),
            size=(110, 100),
            border=(0, 0, 0, 0),
            pos=(590, 60)
        )

        layout.add_widget(b1_button)
        layout.add_widget(b2_button)
        layout.add_widget(b3_button)

        def b1_callback(instance):
            sm.current = 'temperature'

        def b2_callback(instance):
            sm.current = 'moisture'

        def b3_callback(instance):
            sm.current = 'water'

        b1_button.bind(on_release=b1_callback)
        b2_button.bind(on_release=b2_callback)
        b3_button.bind(on_release=b3_callback)

        main_screen.add_widget(layout)
        sm.add_widget(main_screen)

        # Create a temperature screen
        temperature_screen = TemperatureScreen(name='temperature')
        temp_layout = RelativeLayout()

        temp_background_image = Image(source='3.png', allow_stretch=True, keep_ratio=False)
        temp_layout.add_widget(temp_background_image)

        text_label = Label(
            text="Temperature is crucial for plant growth, influencing\n"
                 "processes like germination, photosynthesis, and growth rates.\n"
                 "The temperature requirements of the plant today are..\n"
                 "Extreme temperatures can harm plants, and temperature plays \n"
                 "a significant role in determining \n"
                 "Let's check out the temperature today..",
            font_size=24,
            pos=(20, -80)
        )

        back_button_temp = Button(
            text="Back to Main",
            size_hint=(None, None),
            size=(110, 50),
            pos=(10, 10),
            background_color="#BEDD78"
        )

        next_button_temp = Button(
            text="Next",
            background_normal='arrow.png',
            size_hint=(None, None),
            size=(110, 110),
            pos=(50, 50)
        )

        def temperature_button_callback(instance):
            def collect_data():
                data = {}
                while True:
                    label = input("Enter a label for the pie slice (or 'done' to finish): ")
                    if label.lower() == 'done':
                        break
                    try:
                        value = float(input("Enter the value for slice '{}': ".format(label)))
                        data[label] = value
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the value.")
                return data

            def main():
                data = collect_data()

                if not data:
                    print("No data provided. Exiting.")
                    return
                labels = data.keys()
                sizes = data.values()
                colors = ["#008080", "#ffb229", "#E04227","#c0d8f8"]

                plt.figure(figsize=(8, 8))
                plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
                plt.axis('equal')
                plt.title("TEMPERATURE CHART")
                plt.show()


            main()
        def back_to_main_temperature(instance):
            sm.current = 'main'
        back_button_temp.bind(on_release=back_to_main_temperature)  # Back to MainScreen
        next_button_temp.bind(on_release=temperature_button_callback)

        temp_layout.add_widget(text_label)
        temp_layout.add_widget(back_button_temp)
        temp_layout.add_widget(next_button_temp)

        temperature_screen.add_widget(temp_layout)
        sm.add_widget(temperature_screen)

        # Create a moisture screen
        moisture_screen = MoistureScreen(name='moisture')
        moist_layout = RelativeLayout()

        moist_background_image = Image(source='1.png', allow_stretch=True, keep_ratio=False)
        moist_layout.add_widget(moist_background_image)

        text_label = Label(
            text="Soil moisture is the critical parameter in agriculture.\n"
                 "If there is a shortage or overabundance of water,\n"
                 "plants may die. At the same time, this data depends\n"
                 "on many external factors, primarily weather conditions \n"
                 "and climate changes.\n"
                 "Let's check out the moisture of the soil today..",
            font_size=24,
            pos=(20, -50)
        )

        back_button_moist = Button(
            text="Back to Main",
            size_hint=(None, None),
            size=(110, 50),
            pos=(10, 10),
            background_color="#78B942"
        )

        next_button_moist = Button(
            text="Next",
            background_normal='arrow.png',
            size_hint=(None, None),
            size=(110, 110),
            pos=(100, 80)
        )

        def moisture_button_callback(instance):
            def collect_data():
                data = {}
                while True:
                    label = input("Enter a label for the pie slice (or 'done' to finish): ")
                    if label.lower() == 'done':
                        break
                    try:
                        value = float(input("Enter the value for slice '{}': ".format(label)))
                        data[label] = value
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the value.")
                return data

            def main():
                data = collect_data()

                if not data:
                    print("No data provided. Exiting.")
                    return
                labels = data.keys()
                sizes = data.values()
                colors = ["#C9D1E9", "#7F84BE", "#4E4E8C", "#4E3246"]

                plt.figure(figsize=(8, 8))
                plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
                plt.axis('equal')
                plt.title("MOISTURE LEVELS")
                plt.show()

            main()
        def back_to_main_moisture(instance):
            sm.current = 'main'
        back_button_moist.bind(on_release=back_to_main_moisture)  # Back to MainScreen
        next_button_moist.bind(on_release=moisture_button_callback)

        moist_layout.add_widget(text_label)
        moist_layout.add_widget(back_button_moist)
        moist_layout.add_widget(next_button_moist)

        moisture_screen.add_widget(moist_layout)
        sm.add_widget(moisture_screen)

        # Create a water screen
        water_screen = WaterScreen(name='water')
        wat_layout = RelativeLayout()

        wat_background_image = Image(source='2.png', allow_stretch=True, keep_ratio=False)
        wat_layout.add_widget(wat_background_image)

        text_label = Label(
            text="The amount of water required for a plant can vary \nwidely depending on several factors,\n including the type of plant, its size, environmental conditions,\n and the season. Adjusting the watering schedule based on\n the changing seasons and moisture levels is essential.\nHave a look at today's watering schedule..",
            font_size=24,
            pos=(20, -60)
        )

        back_button_water = Button(
            text="Back to Main",
            size_hint=(None, None),
            size=(110, 50),
            pos=(10, 10),
            background_color="#0BD6FF"
        )

        next_button_water = Button(
            text="Next",
            background_normal='arrow3.png',
            size_hint=(None, None),
            size=(110, 110),
            pos=(60, 60)
        )

        def water_button_callback(instance):
            def collect_data():
                data = {}
                while True:
                    label = input("Enter a label for the pie slice (or 'done' to finish): ")
                    if label.lower() == 'done':
                        break
                    try:
                        value = float(input("Enter the value for slice '{}': ".format(label)))
                        data[label] = value
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the value.")
                return data

            def main():
                data = collect_data()

                if not data:
                    print("No data provided. Exiting.")
                    return
                labels = data.keys()
                sizes = data.values()
                colors = ["#B3E8E6", "#78CECC", "#2EBCB1", "#123955", "#81d7d3"]

                plt.figure(figsize=(8, 8))
                plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
                plt.axis('equal')
                plt.title("WATERING LEVELS")
                plt.show()

            main()
        def back_to_main_water(instance):
            sm.current = 'main'
        back_button_water.bind(on_release=back_to_main_water) # Back to MainScreen
        next_button_water.bind(on_release=water_button_callback)

        wat_layout.add_widget(text_label)
        wat_layout.add_widget(back_button_water)
        wat_layout.add_widget(next_button_water)

        water_screen.add_widget(wat_layout)
        sm.add_widget(water_screen)

        return sm

if __name__ == '__main__':
    iotapp().run()
