# llm

This directory contains API integration logic for different Large Language Models (LLMs) used by the CLI tool.

- `openai_api.py`: Handles OpenAI API integration.
- `gemini_api.py`: Handles Gemini API integration.

To add a new LLM provider, create a new module in this directory and implement a function that takes a prompt and returns the generated output. 