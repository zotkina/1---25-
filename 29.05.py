from tkinter import *
import requests

def get_weather_data(city):
    api_key = "ffe38f305b88d0c589581af3cb589963"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    weather = data['weather']['main']
    temperature = data['main']['temp']
    return f"Weather: {weather}, Temperature: {temperature}K"

def get_weather():
    city = entry.get()
    weather_info = get_weather_data(city)
    label['text'] = weather_info

root = Tk()
root.title("Погода")

label_city = Label(root, text="Город:")
entry = Entry(root)
button = Button(root, text="Получить погоду", command=get_weather)
label = Label(root, text="Погодные данные будут здесь")

label_city.pack()
entry.pack()
button.pack()
label.pack()

root.mainloop()