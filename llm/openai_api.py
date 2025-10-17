import os
import openai

# Function to generate output from OpenAI using  prompt...
# Returns the generated POC or an error message..

def generate_with_openai(prompt):
    # Get the OpenAI API key from env variable...
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        return "[OpenAI API key not set in environment variable OPENAI_API_KEY.]"
    try:
        # Call OpenAI API ...
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
            temperature=0.2,
        )
        #  generated message content...
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        # R error message if API call fails...
        return f"[OpenAI API error: {e}]" 
