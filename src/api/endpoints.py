
from fastapi import FastAPI, HTTPException, Body
from api.chat import ChatCompletionReq, ChatRes, complete_chat
from utility import logger

api_server = FastAPI()

#@app.post("/chat/call")
#async def chat_call(request: ChatCallReq):

sample_req ={"text_list":{"messages":[{"role":"user","content":"ask anything here"},{"role":"system","content":"add your instruction"}]}}

#@api_server.post("/chat/completion", response_model=ChatRes)
@api_server.post("/chat/completion")
async def chat_completion(request: ChatCompletionReq = Body(example=sample_req)) :
    return complete_chat(request)    


#    json ={"text_list":{"messages":[{"role":"user","content":" "Not working"},{"role":"system","content":"Try again?"}]}}
#    req_list=ChatCompletionReq(**json)
#    reqList = ChatRequest( text_list= ChatTextList( messages=[ChatText(role="user", content="test"),ChatText(role="system", content="test system")]))
#    json = reqList.json()
#    print(req_list.json())







