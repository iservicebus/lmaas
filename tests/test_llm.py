import os
from llama_cpp import Llama

#model_path = os.path.join(os.path.dirname(__file__), '../downloads/phi-2.Q5_K_M.gguf')
#model_path = os.path.join(os.path.dirname(__file__), '../downloads/zephyr-7b-beta.Q4_0.gguf')
#model_path = os.path.join(os.path.dirname(__file__), '../downloads/mistral-7b-instruct-v0.2.Q4_K_M.gguf')
model_path = os.path.join(os.path.dirname(__file__), '../downloads/gritlm-7b_q4_1.gguf')

"""
model = Llama(
     model_path=model_path,
     )
print(model("The quick brown fox jumps ", stop=["."])["choices"][0]["text"])


"""
"""
model = Llama(model_path=model_path)

tokens = model.tokenize(b"Hello, world!")
for token in model.generate(tokens, top_k=40, top_p=0.95, temp=1.0, repeat_penalty=1.1):
    print(model.detokenize([token]))
"""


# LOAD THE MODEL
model = Llama(model_path=model_path, chat_format="llama-2")

output =model.create_chat_completion(
    messages=[{
        "role": "user",
        "content": "can you write a sample resume "
        }],

        max_tokens = 1000,
        stop = [],

        temperature = 0.8,
        top_p = 0.95,
        model = None

        )

print(output)



"""
model = Llama(model_path=model_path)

#prompt ="who is bill clinton"

prompt = "<|system|>You are a friendly chatbot who always responds in the style of a pirate</s> <|user|>Who is bill clinton?</s>"

#prompt = "What do you think about the inclusion policies in Tech companies?"
model_output = model(prompt)

   # Define the parameters
   
model_output = model(prompt,
                    max_tokens = 1000,
                        temperature = 0.3,
                        top_p = 0.1,
                        echo = True,
                    #    stop = ["Q", "\n"]
                    )




print(model_output)

"""
"""
        max_tokens: Optional[int] = 16,
        temperature: float = 0.8,
        top_p: float = 0.95,
        echo: bool = False,
        stop: Optional[Union[str, List[str]]] = [],
        stream: bool = False,
        model: Optional[str] = None,
"""