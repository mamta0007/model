import requests


user_query=input("enter your city-->")

url=f"https://wttr.in/{user_query}?format=%c+%t"
show=requests.get(url)

print(show.text)
