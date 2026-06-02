import requests


while True:
    user_city=input("enter your city: ").strip().lower()
    api_key="c1c81417b9bbb83ef44a395743eb4620"
    if user_city== "":
        break
    
    
    url=f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric"
    response=requests.get(url)
    data=response.json()
    
    
    if response.status_code==200:
        print("\nweather repot...\n")
        print(data["name"])
        print(data["weather"])
        print(data["main"]["temp"])
        print(data["weather"][0]["description"])
        
        
        
        
        
        
    else:
        print("something is wrong")
        
        
    