curl -X 'POST' \
  'http://localhost:8000/chat/completion' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text_list": {
    "messages": [
      {
        "role": "user",
        "content": "Not working"
      },
      {
        "role": "system",
        "content": "Try again?"
      }
    ]
  }
}'