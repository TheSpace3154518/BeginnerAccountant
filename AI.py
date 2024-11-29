# Lah yster o sf
import os
from dotenv import load_dotenv
from groq import Groq

#replicate
#together ai
#groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def Get_Info(query,system="You are a helpful AI Assistant",temp=0.5):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system
            }, 
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama3-70b-8192",
        temperature=temp
    )
    return chat_completion.choices[0].message.content




Description = input("Yalah ash baghi tsne3 : ")
Needed_info = [ "Cost of production", "Price of a unit", "Sales for 6 months", "Target Audience"]
prompt = f"""
        You are an expert financial accountant.
        Extract the following Metrics from the user's query  : {Needed_info}. 
        If one of the elements isn't found in the description, make a conservative estimation.
        The output should follow this template where tags are placeholders to be filled.
        Template : 
        [
        """
for i in Needed_info :
    prompt += f"{i} :  < {i} based on the query >"
prompt += "]\n\n"
result = Get_Info(Description, prompt, 0.1)
print(result)

