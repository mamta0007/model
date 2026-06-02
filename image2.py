from openai import OpenAI

client=OpenAI(
     api_key="AIzaSyBkLScjm1Pbk7pJNGqT2H8sy9kHckTX1Tc",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
    
    

response=client.responses.create(
    model="gemini-2.0-flash-preview-image-generation",
    input="generate a image of golden retriever dog"
)

print(response)