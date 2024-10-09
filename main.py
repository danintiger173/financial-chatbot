import os
from openai import AzureOpenAI

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
key = os.getenv("AZURE_OPENAI_KEY")
model_name = "gpt-4o"


while True:
  user_input = input("")

  #converts to lowercase, and leaves
  if user_input.lower() in ["exit", "quit"]:  # Allow user to exit the loop
    print("Exiting the chatbot.")
    break


  client = AzureOpenAI(azure_endpoint=endpoint,api_version="2024-02-01",api_key=key)
  completion = client.chat.completions.create(
  model=model_name,
  messages=[{"role": "user",
      "content": user_input,  # Your question can go here
    },], 
  )

  print(completion.choices[0].message.content)
