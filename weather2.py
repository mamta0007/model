import requests
while True:
    user_city=input("enter city name: ").strip().lower()
    if user_city=="stop":
        break
    

    url=f"https://wttr.in/{user_city}?format=City:%l\nCondition:%c\nTemp:%t\nWind:%w\nHumidity:%h\nPrecip:%p"
    response=requests.get(url)
    if response.status_code==200:
        print(response.text)
        print("\n")
        
    
    else:
        print("something is wrong")
        
 
        
