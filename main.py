import os
from openai import AzureOpenAI

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
key = os.getenv("AZURE_OPENAI_KEY")
model_name = "gpt-4"

client = AzureOpenAI(azure_endpoint=endpoint,api_version="2024-02-01",api_key=key)
completion = client.chat.completions.create(
model=model_name,
messages=[{"role": "user",
    "content": "Who is donald trump?",  # Your question can go here
  },], 
)
print(completion.choices[0].message.content)
