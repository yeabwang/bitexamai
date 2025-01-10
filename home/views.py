import os
from openai import OpenAI
from dotenv import load_dotenv
import logging
from django.shortcuts import render
from django.http import JsonResponse

# Load environment variables from .env
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Set up logger
logger = logging.getLogger(__name__)

def chat(request):
    return render(request, 'index.html')

def chatAPI(request):
    try:
        # Use the OpenAI API to make a chat completion request
        response = client.chat.completions.create(
            model="gpt-4", 
            messages=[
                {"role": "developer", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "Write a haiku about recursion in programming."
                }
            ]
        )

        openai_response = response.choices[0].message.content.strip()

        data = {"response": openai_response}
        return JsonResponse(data)

    except Exception as e:  # Handle any exceptions
        logger.error(f"Unexpected error: {e}")
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)
