from datetime import datetime
from pydantic import BaseModel
import uuid

class CommonMessage(BaseModel):
    """
    Represents a common message 
    """
    id: str = str(uuid.uuid4())
    init_time: datetime = datetime.now()
    res_time: datetime = None
    def update_time(self):
        res_time = datetime.now()
