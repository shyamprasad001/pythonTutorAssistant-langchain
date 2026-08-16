Python Tutor Assistant

A simple Python Tutor Assistant built with Python and LangChain. It uses the Groq LLaMA 3.3 70B model to explain Python concepts with simple code examples.

Features
Uses LangChain for conversation management.
Uses Groq's llama-3.3-70b-versatile model.
Loads the Groq API key securely from a .env file.
Uses system and human messages to guide the model.
Provides beginner-friendly Python explanations.
Technologies Used
Python
LangChain
Groq
LLaMA 3.3 70B
python-dotenv
Installation

Clone the repository:

git clone <your-repository-url>
cd PythonTutorAssistant


Install the required packages:

pip install langchain langchain-groq python-dotenv

Environment Variables

Create a .env file in the project directory:

GROQ_API_KEY="your_groq_api_key"


Replace your_groq_api_key with your actual Groq API key.

Do not commit your .env file to Git. Add it to .gitignore:

.env
__pycache__/

Usage

Run the application with:

python app.py


The assistant will explain:

Explain what a dictionary is in Python with an example.

How It Works

The application:

Loads the Groq API key from the .env file.
Creates a system message defining the assistant as a Python tutor.
Creates a human message containing the Python question.
Initializes the Groq LLaMA model through LangChain.
Sends the messages to the model using invoke().
Prints the model's response.
Example

Question:

Explain what a dictionary is in Python with an example.


Response:

A dictionary in Python is a collection of key-value pairs.

Example:

student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print(student["name"])

Project Structure
PythonTutorAssistant/
├── app.py
├── .env
├── .gitignore
└── README.md

Security

Keep your API key private. Never upload .env or expose your GROQ_API_KEY in your source code or Git repository.

License

This project is for educational purposes.
