# this is a long document we can split it 

with open("mbox-short.txt") as f:
    mbox_short = f.read()

from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000
)

texts = text_splitter.create_documents([mbox_short])
# print(texts[0])
# print(texts[0].page_content)
print(len(texts[1].page_content))

print(len(texts),type(texts))
print(len(texts[0].page_content))

chunks=[len(i.page_content) for i in texts]
print(sum(chunks))

