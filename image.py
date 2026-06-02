from openai import OpenAI

client=OpenAI( 
              api_key="AIzaSyBkLScjm1Pbk7pJNGqT2H8sy9kHckTX1Tc",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
    


response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages={"role":"user","content":[{"type":"text","text":"desribe  the  image"},
                                       {"type":"image_url","image_url":{"url":"https://api.nga.gov/iiif/a2e6da57-3cd1-4235-b20e-95dcaefed6c8/full/!800,800/0/default.jpg"}}]}
)

print("Heading:",response.choices[0].message.content)