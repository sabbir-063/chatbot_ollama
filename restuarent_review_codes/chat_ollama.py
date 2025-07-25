import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "gemma3"  # Replace with your model name
prompt = "explain RAG in 3 sentences?"

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Ollama:")
print(response.response)