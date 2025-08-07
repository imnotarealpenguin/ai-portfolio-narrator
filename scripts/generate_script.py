# scripts/generate_script.py

"""
Generates a personal narration script based on your project list using GPT-4.
Optional: Sends it to ElevenLabs for audio generation.
"""

import openai

# --- CONFIG --- #
openai.api_key = "YOUR-OPENAI-API-KEY"  # 🔒 Replace with your own
voice_tone = "friendly and confident"

# --- INPUT --- #
with open("input/project-list.txt", "r") as file:
    projects = file.read()

prompt = f"""
You're an expert AI assistant. Generate a 1-minute narration script introducing Santiago and his personal projects.
Tone: {voice_tone}
Use these projects as inspiration:

{projects}
"""

# --- GPT-4 OUTPUT --- #
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a personal branding assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

narration = response['choices'][0]['message']['content']

print("\n=== AI-NARRATED SCRIPT ===\n")
print(narration)

# To add ElevenLabs later:
# - Use the ElevenLabs API to send `narration` as input
# - Save MP3 in `audio/output.mp3`
scripts/generate_script.py
