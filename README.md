# Self-Hosted AI Development Environment

A simple AI chatbot API using Flask to serve an Ollama model locally.
We are using flask right now but will change for prod


## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/texasmadecode/CISD-self_hosted_ai-
   cd self-hosted-ai-dev
## Build and Run docker container   
1. Make dockerfile and run
  ```bash
  docker build . -t ai_docker
  docker run -p 5000:5000 ai_docker
