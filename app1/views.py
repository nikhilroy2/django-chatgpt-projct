from django.shortcuts import render
# from .openai_api import generate_response
# Create your views here.
import openai, os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)

def Index(request):
    chatbot_response = None
    
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = prompt,
            max_tokens = 256,
            #stop = "."
            temperature = 0.5
        )
        
        output = response.choices[0].text
        print(output)
    return render(request, "app1/index.html", {'output': output})