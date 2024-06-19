from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
print("Current working directory:", os.getcwd())

load_dotenv()

# Fetch the token from environment variables
HF_TOKEN = os.getenv('HF_TOKEN')
if not HF_TOKEN:
    raise ValueError("HF_TOKEN environment variable not set")

repo_id = "openai-community/gpt2"
# Pass max_length and token in model_kwargs as indicated by the warning
llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=200, temperature= 0.9, token= HF_TOKEN)

# try:
#     llm.invoke("A poem on a rainy day")
# except Exception as e:
#     print(f"Error: {e}")
#     # Implement retry logic here if necessary