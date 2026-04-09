# Alfred-Agent

Alfred-Agent is a small LangGraph + Ollama assistant styled as Alfred from Wayne Manor. It combines a local LLM, a lightweight retriever, and a few external tools behind a simple Gradio chat UI.

## Features

- Gradio chat interface
- LangGraph-based tool-using agent
- Local LLM via Ollama
- Guest information retrieval using a BM25 retriever
- Web search tool
- Weather lookup tool
- Hugging Face Hub stats lookup
- Joke tool

## Tech Stack

- Python
- Gradio
- LangChain
- LangGraph
- Ollama
- Hugging Face Datasets

## Project Structure

```text
Alfred-Agent/
  app/
    main.py
    agent.py
    llm.py
    agent_tools.py
    retriever/
      dataloaer.py
      retriever.py
  Dockerfile
  compose.yaml
  requirements.txt
  README.md
```

## Prerequisites

Before running the project, make sure you have:

- Ollama installed and running
- Docker Desktop if you want to run the app in a container
- An OpenWeather API key if you want weather lookups

You also need an Ollama model pulled locally. 

Example:

```powershell
ollama pull llama3.2:3b
```

## Environment Variables

Create a `.env` file in the repo root.

Example:

```env
OPENWEATHERMAP_API_KEY=your_api_key_here
```

## Run Locally

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start Ollama if it is not already running:

```powershell
ollama serve
```

Run the app:

```powershell
python app/main.py
```

Then open:

```text
http://localhost:7860
```

## Run With Docker

Build the image:

```powershell
docker build -t alfredagent .
```

Run the container:

```powershell
docker run --rm -p 7860:7860 --env-file .env alfredagent
```

Important:

- The app container expects Ollama to be reachable at `http://host.docker.internal:11434`
- Ollama should be running on your host machine
- The required model should already be pulled in Ollama

## Run With Docker Compose

Build and start:

```powershell
docker compose up --build
```

Run in the background:

```powershell
docker compose up --build -d
```

Stop everything:

```powershell
docker compose down
```


