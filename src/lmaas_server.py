
from utility import logger
from app import api_server
import uvicorn


if __name__ == "__main__":
    logger.info("start LMaaS server")
    import uvicorn
    uvicorn.run(api_server, host="0.0.0.0", port=8000)


#    json ={"text_list":{"messages":[{"role":"user","content":" "Not working"},{"role":"system","content":"Try again?"}]}}
#    req_list=ChatCompletionReq(**json)
#    reqList = ChatRequest( text_list= ChatTextList( messages=[ChatText(role="user", content="test"),ChatText(role="system", content="test system")]))
#    json = reqList.json()
#    print(req_list.json())







