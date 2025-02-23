from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save
import os
load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

# audio = client.text_to_speech.convert(
#     text="Hola ya me conecte con eleven labs.",
#     voice_id="JBFqnCBsd6RMkjVDRZzb",
#     model_id="eleven_multilingual_v2",
#     output_format="mp3_44100_128",
# )
# play(audio)

response = client.conversational_ai.get_agents()
print(response)

# save(
#     audio,
#     "first_move.wav"
# )