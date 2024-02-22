# Language Model as a Service (LMaaS)
For many developers, Generative AI (GenAI) remains a mystical realm, locked behind expensive GPUs, complex ML frameworks, and the gates of large tech companies. But what if you could leverage your existing coding skills and unleash the power of GenAI from your own laptop?
**This is where LMaaS (Language Model as a Service) comes in**
Forget powerful machines and years of specialized learning. LMaaS, an open-source project, empowers you to deploy language models directly on your laptop, even if it's a decade old! **No heavy lifting, no PhD required.**

LMaaS empowers developers of all levels to tap into the exciting world of GenAI. With your existing skills and an open laptop, you can now explore new creative avenues, solve problems, and push the boundaries of what's possible. **Let us start!**

## Install LMaaS

Installing LMaaS is a breeze, and the best method depends on your needs:

**Solo Explorer**

- **Docker**: The easiest option for personal use. Just follow the quick Docker installation guide and you're ready to roll. Perfect for experimenting and tinkering!
- **Local Install**: Want more control or contribute to LMaaS? Follow the local installation instructions for a deeper dive.

**Collaborative Crew**

- **Kubernetes**: Got a Kubernetes cluster humming? This is your golden ticket. Deploy LMaaS there for seamless group sharing and development.


### Installation on Docker
If you do not have docker on your local machine. Please following this instruction https://docs.docker.com/engine/install/

After docker is installed, 

- clone the project from github
```bash
  git clone https://github.com/iservicebus/lmaas.git

```


- download LLM model from hugging face. 

 ```bash
curl -L -o mistral-7b-instruct-v0.2.Q4_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf

```

if you do not have curl command, you can use browser to directly download from https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf


After the file is downloaded,  Create subdirectories ./work/genai in Linux home directory or .\work\genai in windows user directory. Move the file to the subdirectory. If you want to use a different directory, please change the source path in docker-compose.yml, which is located in lmaas project directory. 

- your last step is run deployment command. go to lmaas project. you should see a file name called docker-compose.yml. within that directory, run the following command

```bash
docker-compose up
```

After this step is finished. you can validate the installation at http://localhost:8000. 

### Installation on Local Machine

LMaaS requires C++ and CMake libraries. It is not easy to install those libraries on windows.  Docker is a better option.  Installation on Mac and Linux is straight forward:

- on Mac
  
  run the following command if the libraries are not installed yet

```bash

xcode-select --install

```

- Ubuntu/Debian
  run the following command to install the libraries

```bash
apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    libx11-dev \

```


- CentOS/Redhat Linux
  run the following command

```bash
yum update -y && \
    yum install -y \
        gcc gcc-c++ cmake openblas-devel python3-devel
```

- clone the project from github
```bash
  git clone https://github.com/iservicebus/lmaas.git

```



- install Python package and download LLM models
  
  In project directory (./lmaas), run the following command

  ```bash
  ./setup.sh

  ```

  - start LMaaS server
  
```bash
./start_server.sh
```

 - go to http://localhost:8000. validate the LMaaS. 



### Installation on Kubernetes

LmaaS installation script is written for kubernetes kind.  If you use different kubernetes providers, you may modify the script.  In the script, we assume that LLM model is downloaded at local file system (/tmp/downloads). if you use external persistent volume (PV). please modify accordingly.  

The following is the step how to download the LLM model at Hugging face:


 ```bash
curl -L -o mistral-7b-instruct-v0.2.Q4_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf

```

if you do not have curl command, you can use browser to directly download from ttps://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf


## GenAI development

please go to https://github.com/iservicebus/lmaas.clients.git

## GenAI Chat
please go to https://github.com/iservicebus/lmaas.js.git
