
from typing import List, Optional, Union, Dict, Any
from pydantic import BaseModel
from data_models.chat.text import ChatTextList, ChatText
from utility import logger, lmaas_config
from llama_cpp import Llama
from datetime import datetime
import os, uuid

class CommonReq(BaseModel):
    max_tokens: Optional[int] = 1000
    temperature: float = 0.2
    top_p: float = 0.95
    stop: Optional[Union[str, List[str]]] = []
    model: Optional[str] = None
    id: str = str(uuid.uuid4())
    req_time: datetime = datetime.now()


class ChatRes(BaseModel):

    id: str = None
    res_time: datetime = None
    res_text_: Dict[str, Any]    

class ChatCallReq(CommonReq):
    echo: bool = True
    stream: bool = False
    text_list: ChatTextList    

class ChatCompletionReq(CommonReq):
    text_list: ChatTextList

def complete_chat(request: ChatCompletionReq)-> ChatRes :
    try:
        mock = False
        user_message = request.text_list.to_json_in()
        logger.info(f"start to send request to llm: {request.text_list.to_json_in()}")
        model_path = os.path.join(os.path.dirname(__file__), '../../'+lmaas_config.app.models.download_path+'/'+lmaas_config.app.models.chat.model_file)

        if mock == False:         
            model = Llama(model_path=model_path, chat_format="llama-2")
            output =model.create_chat_completion(
                messages=user_message,
                max_tokens = request.max_tokens,
                stop = request.stop,
                temperature = request.temperature,
                top_p = request.top_p,
                model = request.model
            )
            res_text = output["choices"][0]["message"]
        else:    
            res_text ={'role': 'assistant', 'content': "Here\'s a simple \"Hello World\" program written in Java:\n\n```java\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World!\");\n    }\n}\n```\n\nTo run this program, save it in a file with the name `HelloWorld.java`, then compile it using the `javac` compiler, and run it using the `java` command. For example, if you save the file in the current directory, you can compile and run it with the following commands in your terminal or command prompt:\n\n```bash\njavac HelloWorld.java\njava HelloWorld\n```" }
 
        chat_res: ChatRes ={
            "res_text":res_text,
            "res_time": datetime.now(),
            "id": request.id
        }
        logger.info(f"finish the request with response: {chat_res}")

        return chat_res
    except Exception as e:
        raise e

#if __name__ == "__main__":
#    reqList = ChatCompletionReq( text_list= ChatTextList( messages=[ChatText(role="user", content="who is bill clinton"),ChatText(role="system", content="find info")]))
#    output =complete_chat(reqList)
#    print(output)



