# pip install 
from langchain_google_genai import GoogleGenerativeAI 
api_key = "AIzaSyAqvYGJR8W-rK4FkPsBlA7M0IxaUP861V4"
llm = GoogleGenerativeAI(model="gemini-1.5-flash-latest",
                             google_api_key=api_key)
print(
    llm.invoke("list of top 5 indian cricketers"
               )
)
