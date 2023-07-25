import openai

key = input("Enter your OpenAI API key: ")
openai.api_key = key

filename = input("Enter the name of the file you want to create documentation for: ")
with open(filename, "r") as file:
    file_content = file.read()
name = filename.split(".")[0]
# Create the documentation prompt
user_message = f"You are creating documentation for code. The code in the file is as follows:\n{file_content}\nPlease provide documentation in markdown format with these titles, newlines, formatting, and sections:\n# Title\n# Introduction\n# Usage\n# Dependencies\n# Functionality\n# Input."
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_message}]
)
print(response)
#take the response content and write it to a markdown file
name = name + "-documentation.md"
with open(name, "w") as file:
    file.write(response["choices"][0]["message"]["content"])


