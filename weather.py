from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={api_key}"
        try:
            json_data = requests.get(api).json()
            print(f"API response: {json_data}")

            if json_data.get('cod') != 200:
                messagebox.showerror("Weather App", "Failed to retrieve weather data. Please check the city name.")
                return
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Weather App", "Failed to retrieve data. Please check your network connection.")
    
    
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']


        t.config(text=(temp,"°C"))
        c.config(text=(condition))
        w.config(text=(wind))
        h.config(text=(humidity))
        d.config(text=(description))
        p.config(text=(pressure))
    

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")
        print(f"Error: {e}")

#search box
search_box = PhotoImage(file='images/search.png')
my_image = Label(image=search_box)
my_image.place(x=20,y=20)

textfield = tk.Entry(root,justify='center',width=17,font=('poppins',25,'bold'),bg='#404040',fg='white',bd=0)
textfield.place(x=50,y=40)
textfield.focus()

search_icon = PhotoImage(file='images/search_icon.png')
myimage_icon = Button(image=search_icon,borderwidth=0,cursor='hand2',bg='#404040',command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file='images/logo.png')
logo = Label(image=logo_image)
logo.place(x=150,y=100)

#bottom box
box = PhotoImage(file='images/box.png')
Label(root,image=box).pack(side='bottom',padx=5,pady=5)

#time
name = Label(root, font=('arial', 15, 'bold'))
name.place(x=30, y=100)
clock=Label(root, font=('Helvetica', 20))
clock.place(x=30, y=130)

#label
label1 = Label(root, text='WIND', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)

label2 = Label(root, text='HUMIDITY', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=250, y=400)

label3 = Label(root, text='DESCRIPTION', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=430, y=400)

label4 = Label(root, text='PRESSURE', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)

t=Label(font=('arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef',fg='white')
w.place(x=120,y=430)
h=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef',fg='white')
h.place(x=280,y=430)
d=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef',fg='white')
d.place(x=440,y=430)
p=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef',fg='white')
p.place(x=680,y=430)


root.mainloop()