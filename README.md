# Multi-Agent Research Assistant

A simple AI research assistant built with LangGraph, Django, and Streamlit.

The system uses multiple agents to answer user questions.

## Features
- Planner Agent: Decides what information is needed
- Research Agent: Uses a mock MCP tool to retrieve data
- Django REST API backend
- Streamlit UI
- PostgreSQL database for storing conversations

## Architecture

User → Streamlit UI → Django API → LangGraph → Agents → MCP Tool → Response

## Tech Stack
- LangGraph
- Django REST Framework
- Streamlit
- Ollama (local LLM)
- PostgreSQL
- Redis (optional caching)

## Installation

### 1. Clone repo

git clone https://github.com/yourname/multi-agent-research-assistant.git

cd multi-agent-research-assistant

### 2. Create virtual environment

python -m venv venv

source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run Django backend

cd backend

python manage.py migrate

python manage.py runserver

### 5. Start Ollama

ollama run llama3

### 6. Run Streamlit UI

cd ../ui

streamlit run app.py

## Example

Question:
What is the capital of France?

Planner Decision:
capital of france

Research Result:
The capital of France is Paris.

Final Answer:
The capital of France is Paris.




User
  ↓
Streamlit UI
  ↓
Django API
  ↓
LangGraph
  ↓
Planner Agent
  ↓
Research Agent
  ↓
MCP Tool
  ↓
PostgreSQL
