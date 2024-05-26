from langchain_community.document_loaders.csv_loader import CSVLoader


loader = CSVLoader(file_path='Visadataset.csv')
data = loader.load()

# print(data)
# print(type(data))  # list
# print(data[0])   # page content   -metadata   - row 
print(data[0].page_content)
print(data[0].metadata)
print(len(data))
print(data[254789])