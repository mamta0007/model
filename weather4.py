import requests
from openai import OpenAI
import json

client=OpenAI(
     api_key="AIzaSyBkLScjm1Pbk7pJNGqT2H8sy9kHckTX1Tc",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def weather_tool(user_city):
        url=f"https://wttr.in/{user_city}?format=Condition:%c\nTemp:%t\nWind:%w\nHumidity:%h"
        
        response=requests.get(url)
        
        if response.status_code==200:
            return response.text
        else:
            return "something is wrong"
        
        

    
while True:
    user_query=input("enter you chat:\n")
    
    
    if user_query=="":
        break
    
    
    
    
    system_prompt="""You are an intent classification and entity extraction assistant.

Your tasks:
1. Detect if the user query is related to weather.
2. Extract the city name from the query (if present).

Output format (STRICT JSON):
{
  "intent": True or False,
  "city": "city_name" or null
}

Rules:
- If the query is about weather → intent = True
- Otherwise → intent = False
- Extract only the city name (no extra words)
- If no city is found → city = null
- Do NOT explain anything
- Do NOT add extra text
- Output ONLY valid JSON        
   
    """
    
  
    response2=client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type":"json_object"},
        messages=[{"role":"system","content":system_prompt},
                  {"role":"user","content":user_query}])
    
    result=response2.choices[0].message.content
    
    output=json.loads(result)
    
    weather_data=""
    
    if output["intent"]==True:
        weather_data=weather_tool(user_city=output["city"])
        
    system_prompt2=f"""you are a assistant chatbot who give
                   answer to user question.
                   
    your task-->
    - give answer for user question.
    - if the question is related to weather then use{weather_data} to give answer to user
     don't give assumtion.
     
     Rules:
   - If the query is about weather → use{weather_data} to solve query
   - Otherwise → use model for answer

    
    """
        
    response3=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role":"system","content":system_prompt2},
                  {"role":"user","content":user_query}])
    print(response3.choices[0].message.content)
        
    

   

        

