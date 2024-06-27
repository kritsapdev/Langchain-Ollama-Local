from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(
    model="phi3", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)
print(llm("why tree is green"))
#result = llm.invoke("why the sky is blue")
#print(result)