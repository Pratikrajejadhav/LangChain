**RAG  Retrieval-Augmented Generation** 

- if you want to do
- Document search
- Query from the documents

    - step-1: you need to load the data
    - step-2: split the data into chunks
    - step-3: apply the any embeddings model to convert that chunks to a vector
    - step-4: vector database
    - step-5: a new question query user asking
    - step-6: this new query also into embeddings
    - step-7: this vector multiply with each and every vector chunk
    - step-8: which is the most similar that is our output