import openai
import os

# Set up the OpenAI API client with your API key
openai.api_key = os.environ["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"]

def generate_response(prompt):
    # Call the OpenAI GPT-3 API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated response from the API response
    return response.choices[0].text.strip()
