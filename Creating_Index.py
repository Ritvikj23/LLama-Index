import os
import openai
openai.api_key = "insert key here"
os.environ["OPENAI_API_KEY"] = "insert key here"

from llama_index import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader(r"path to resources").load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

index.storage_context.persist("path where you want to save the index")

while True:
    user_input = input("Enter your questions here (type exit to stop): ")

    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break 

    response = query_engine.query(user_input)
    print("\n")
    print(response)
    print("\n")
