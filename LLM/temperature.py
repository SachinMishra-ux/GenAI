import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

def get_groq_llm():
    return ChatOpenAI(
        model= "openai/gpt-oss-120b",
        base_url= "https://api.groq.com/openai/v1",
        api_key= os.getenv("GROQ_API_KEY"),
        max_tokens= 1000,
        temperature= 0.7,
        top_p= 0.9, # 
        top_k= 50,
    )

model = get_groq_llm()
result = model.invoke("Write a 5 line poem on cricket")

print(result.content)

'''
                 AI predicts
                     │
                     ▼
        Chocolate 40%
        Vanilla   25%
        Strawberry15%
        Mango      8%
        Oreo       5%
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Top-K                 Top-P
 Keep top 3 words      Keep until 90%
          │                     │
          └──────────┬──────────┘
                     ▼
             Temperature decides
         how random the final choice is

'''