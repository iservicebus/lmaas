
echo "-----Install Python Package------------"

pip install --user  .

mkdir ./downloads

echo "-------------download LLM Model, it will take a while--------"


curl -L -o ./downloads/mistral-7b-instruct-v0.2.Q4_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf
.
