import os
from dotenv import load_dotenv
from google import genai


"""
Temporary API handshake test.
Verifies Gemini API connectivity and .env loading.
Will be deleted after Day 1 - this is diagonostic, not module
"""


# Step 1: Load environment variables from .env file
load_dotenv()

# Step 2: Read API key from environment
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Step 3: Validate key is present
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in environment. "
        "Check your .env file in project root"
    )

print(f"API key loaded (starts with: {api_key[:10]}...)")
print(f"Using model: {model_name}")
print("-" * 50)

# Step 4: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 5: Send a Bengali prompt
prompt = "বাংলায় একটি বাক্যে নিজের পরিচয় দাও।"

print(f"Prompt: {prompt}")
print("Sending request to Gemini...")
print("-" * 50)

# Step 6: Get response
response = client.models.generate_content(
    model = model_name,
    contents = prompt,
)

# Step 7: Print response
print("Response from Gemini:")
print(response.text)
print("-" * 50)
print("✓ Handshake successful")
