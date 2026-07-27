from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv(override=True)

llm = HuggingFaceEndpoint(
    repo_id="unsloth/Laguna-S-2.1-GGUF",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)