import os
from openai import OpenAI
from dotenv import load_dotenv
import logging
from django.shortcuts import render
from django.http import JsonResponse

# Load environment variables from .env
load_dotenv()

# Set up logger
logger = logging.getLogger(__name__)

# Initialize OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat(request):
    return render(request, 'index.html')

def chatAPI(request):
    try:
        # Use the new client API to make a chat completion request
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" or another model as needed
            messages=[
                {
                    "role": "user",
                    "content": "You are a helpful assistant."
                }
            ]
        )

        # Extract the generated response from the API response
        openai_response = response['choices'][0]['message']['content'].strip()

        # Return the response as JSON
        data = {"response": openai_response}
        return JsonResponse(data)

    except Exception as e:  # Handle any exceptions
        logger.error(f"Unexpected error: {e}")
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)
