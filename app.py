from langchain_community.llms import Ollama

llm = Ollama(
    model="phi3"
)

result = llm.invoke("why the sky is blue")
print(result)