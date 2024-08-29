def metodo1():#esse método não funciona
    from langchain.chains import LLMChain
    from langchain.llms import OpenAI
    from langchain.prompts import PromptTemplate
    from langchain.callbacks.base import BaseCallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

    callback_manager = BaseCallbackManager([StreamingStdOutCallbackHandler()])

    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = OpenAI(openai_api_base="http://10.246.0.164:8080", 
                openai_api_key="YOUR_API_KEY",
                streaming=True,
                callback_manager=callback_manager,
                verbose=False)

    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=False)

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

    for chunk in llm_chain.stream("What NFL team won the Super Bowl in the year Justin Beiber was born?"):
        print(chunk, end="", flush=True)

def metodo2():#esse método funciona
    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI(temperature=0.5,
                    model="/home/teste/llama.cpp/meta-llama-3.1-8b-instruct-q4_0.gguf", 
                    openai_api_base="http://10.246.0.164:8080", 
                    openai_api_key="ed")

    # print(llm.predict("hi!"))

    for chunk in llm.stream("Write a bobble sort in c++"):
        print(chunk.content, end="", flush=True)
