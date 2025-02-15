import requests
import json
from typing import Optional, Dict, Any


class ElevenLabsAPI:
    def __init__(self):
        self.api_key = "sk_c6913cc2bd5161badfda6eb01d77587353528f801e0de63b"
        self.voice_id ="6O8E1UOlJbvkhJDpV0aB"
        self.base_url = "https://api.elevenlabs.io/v1"
        self.headers = {
            "Accept": "application/json",
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def get_voices(self) -> Dict[str, Any]:
        """Retrieve available voices."""
        endpoint = f"{self.base_url}/voices"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def generate_speech(
        self,
        text: str,
        stability: float = 0.5,
        similarity_boost: float = 0.75,
        style: float = 0.0,
        use_speaker_boost: bool = True
    ) -> bytes:
        """Generate speech from text using specified parameters.
        
        Args:
            text (str): The text to convert to speech
            voice_id (str): ID of the voice to use
            stability (float): Voice stability (0-1)
            similarity_boost (float): Similarity boost factor (0-1)
            style (float): Speaking style (0-1)
            use_speaker_boost (bool): Whether to use speaker boost
            
        Returns:
            bytes: Audio data in bytes
        """
        
        endpoint = f"{self.base_url}/text-to-speech/{self.voice_id}"
        
        payload = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost,
                "style": style,
                "use_speaker_boost": use_speaker_boost
            }
        }

        response = requests.post(
            endpoint,
            headers=self.headers,
            json=payload
        )

        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error generating speech: {response.text}")

    def save_audio(self, audio_data: bytes, filename: str):
        """Save audio data to a file.
        
        Args:
            audio_data (bytes): Audio data to save
            filename (str): Output filename (should end in .mp3)
        """
        with open(filename, "wb") as f:
            f.write(audio_data)
