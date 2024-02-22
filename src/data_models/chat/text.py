from pydantic import BaseModel, validator
from typing import Any

class ChatText(BaseModel):
    """
    Represents a single message in a conversation.
    """
    role: str  = "system" # Default role to "system"
    content: Any
    generated: str = None

    @validator("role")
    def validate_role(cls, value):
        valid_roles = ["system", "user", "assistant"]
        if value not in valid_roles:
            raise ValueError(f"Invalid role: {value}. Valid roles are: {', '.join(valid_roles)}")
        return value

    """
    output string format
    <|role|>
    content
    """
    def to_str(self):
        all_str= "<|"+self.role+">\n" +self.content+"\n"
        return all_str    

    def to_partial_json(self) -> dict:
        """Converts the ChatText object to a JSON object with only the content and role properties."""
        return dict(content=self.content, role=self.role)

class ChatTextList(BaseModel):
    """
    Represents a collection of messages in a conversation.
    """
    messages: list[ChatText] = []

    def add_message(self, message: ChatText):
        """
        Adds a new message to the message List.

        Args:
            message (ChatText): The message to add.
        """
        self.messages.append(message)

    def list_all_messages(self):
        """
        Returns a list of system messages.

        Returns:
            list[Message]: a list of all messages
        """
        return [message for message in self.messages]

    def to_str_in(self):
        str_list = [message.to_str() for message in self.messages]
        return "".join(str_list) 

    def to_json_in(self):
        return [message.to_partial_json() for message in self.messages]

    def list_messages_by_role(self, role: str):
        """
        Returns a list of user messages.

        Returns:
            list[Message]: A list of message objects with role "user".
        """
        return [message for message in self.messages if message.role == role]

