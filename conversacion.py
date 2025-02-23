from elevenlabs import stream
from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv
load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)
audio_stream = client.text_to_speech.convert_as_stream(
    text="esto es una prueba",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2"
)
# option 1: play the streamed audio locally
este es un cambio de prueba
stream(audio_stream)