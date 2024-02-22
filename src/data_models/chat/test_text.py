from unittest import TestCase
from pydantic import ValidationError

from .text import ChatText, ChatTextList

class TestChatText(TestCase):

    def test_init_with_valid_data(self):
        message = ChatText(role="user", content="Hello!")
        self.assertEqual(message.role, "user")
        self.assertEqual(message.content, "Hello!")

    def test_init_with_invalid_role(self):
        with self.assertRaises(ValidationError):
            ChatText(role="invalid", content="This will fail")

    def test_validate_role(self):
        valid_roles = ["system", "user"]
        for role in valid_roles:
            self.assertEqual(ChatText.validate_role(role), role)
        with self.assertRaises(ValueError):
            ChatText.validate_role("invalid")

class TestChatTextList(TestCase):

    def test_add_message(self):
        text_list = ChatTextList()
        text_list.add_message(ChatText(role="system", content="Welcome!"))
        self.assertEqual(len(text_list.messages), 1)
        self.assertEqual(text_list.messages[0].content, "Welcome!")

    def test_list_all_messages(self):
        text_list = ChatTextList()
        text_list.add_message(ChatText(role="system", content="System message"))
        text_list.add_message(ChatText(role="user", content="User message"))
        all_messages = text_list.list_all_messages()
        self.assertEqual(len(all_messages), 1)
        self.assertEqual(all_messages[0].content, "System message")

    def test_list_messages_by_role(self):
        text_list = ChatTextList()
        text_list.add_message(ChatText(role="system", content="System message"))
        text_list.add_message(ChatText(role="user", content="User message"))
        user_messages = text_list.list_messages_by_role("user")
        self.assertEqual(len(user_messages), 1)
        self.assertEqual(user_messages[0].content, "User message")

