import os

try:
    import google.generativeai as genai
except ImportError:
    genai = None

# NOTE: For production, use os.getenv('GEMINI_API_KEY') instead of hardcoding the key.
#  placeholder for demonstration purposes only.
GEMINI_API_KEY = "";

# Function for generate output from Gemini using  prompt
#  generated POC or an error message

def generate_with_gemini(prompt):
    api_key = GEMINI_API_KEY
    if not api_key:
        return "[Gemini API key not set.]"
    if genai is None:
        return "[google-generativeai package not installed.]"
    try:
        # Configure Gemini API with the API key
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('models/gemini-1.0-pro')
        response = model.generate_content(prompt)
        # Return the generated text
        return response.text.strip()
    except Exception as e:
        #  error message if API call fails
        return f"[Gemini API error: {e}]" 