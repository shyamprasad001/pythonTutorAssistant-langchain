# Python Tutor Assistant

A simple Python Tutor Assistant built with Python and LangChain. It uses the Groq LLaMA 3.3 70B model to explain Python concepts with simple code examples.

## Features

- Uses LangChain for conversation management
- Uses Groq's `llama-3.3-70b-versatile` model
- Loads the Groq API key securely from a `.env` file
- Uses `SystemMessage` and `HumanMessage`
- Provides beginner-friendly Python explanations

## Technologies Used

- Python
- LangChain
- Groq
- LLaMA 3.3 70B
- python-dotenv

## Installation

Install the required packages:

    pip install langchain langchain-groq python-dotenv

## Environment Variables

Create a `.env` file in the project directory:

    GROQ_API_KEY="your_groq_api_key"

Replace `your_groq_api_key` with your actual Groq API key.

## Usage

Run the application:

    python app.py

The assistant will answer:

    Explain what a dictionary is in Python with an example.

## How It Works

1. Loads the Groq API key from the `.env` file.
2. Creates a `SystemMessage` defining the assistant as a Python tutor.
3. Creates a `HumanMessage` containing the Python question.
4. Initializes the Groq LLaMA model using LangChain.
5. Invokes the model using `invoke()`.
6. Prints the model's response using `response.content`.

## Project Structure

    PythonTutorAssistant/
    ├── app.py
    ├── .env
    ├── .gitignore
    └── README.md

## Security

Never commit your `.env` file or expose your Groq API key.

Add the following to `.gitignore`:

    .env
    __pycache__/

## License

This project is for educational purposes.
