from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

# system message - system prompt
# human message - user prompt
# ai message - model response
# tool 

prompt = chat_template.invoke({'domain':'cricket','topic':'No Ball'})

print(prompt)