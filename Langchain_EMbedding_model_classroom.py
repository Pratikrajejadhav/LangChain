from langchain_google_genai import GoogleGenerativeAIEmbeddings
api_key = 'AIzaSyAqvYGJR8W-rK4FkPsBlA7M0IxaUP861V4'

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key, timeout=100)
vector = embeddings.embed_query("hello, world")
print(vector[:5])
print(len(vector))

"""
Sentence represents with a vector has 768 value
dimensionality : 768 
"""



