from langchain_google_genai import GoogleGenerativeAIEmbeddings
api_key = 'AIzaSyAVdmSlrL8PA62m--SllyfcOACQ5S2ws5U'

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key, timeout=100)
vector = embeddings.embed_query("hello, world")
print(vector[:5])
print(len(vector))

"""
Sentence represents with a vector has 768 value
dimensionality : 768 
"""