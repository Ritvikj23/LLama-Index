import os
import openai
openai.api_key = "insert key here"
os.environ["OPENAI_API_KEY"] = "insert key here"

from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

storage_context = StorageContext.from_defaults(persist_dir="path where index is stored")

new_index = load_index_from_storage(storage_context)

new_query_engine = new_index.as_query_engine()

while True:
    user_input = input("Enter your question (type 'exit' to stop): ")

    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    response = new_query_engine.query(user_input)
    print("\n")
    print(response)
    print("\n")