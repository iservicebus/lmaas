from fastapi import FastAPI,  Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.chat import ChatCompletionReq, complete_chat
from utility import logger

api_server = FastAPI(
   title="LMaaS API",
    description="An API for Language Model as a Service (LMaaS) !",

)

templates = Jinja2Templates(directory="templates")

@api_server.get("/", include_in_schema=False)
def landing_page(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"openapi_schema": api_server.openapi()})



#@app.post("/chat/call")
#async def chat_call(request: ChatCallReq):

sample_req ={"text_list":{"messages":[{"role":"user","content":"ask anything here"},{"role":"system","content":"set your instruction"}]}}

#@api_server.post("/chat/completion", response_model=ChatRes)
@api_server.post("/chat/completion")
async def chat_completion(request: ChatCompletionReq = Body(example=sample_req)) :
    return complete_chat(request)    


#    json ={"text_list":{"messages":[{"role":"user","content":" "Not working"},{"role":"system","content":"Try again?"}]}}
#    req_list=ChatCompletionReq(**json)
#    reqList = ChatRequest( text_list= ChatTextList( messages=[ChatText(role="user", content="test"),ChatText(role="system", content="test system")]))
#    json = reqList.json()
#    print(req_list.json())



