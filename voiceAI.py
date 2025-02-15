from elevenlabs_integration import ElevenLabsAPI

# Replace with your API key from https://elevenlabs.io/
API_KEY = "sk_c6913cc2bd5161badfda6eb01d77587353528f801e0de63b"

def test_elevenlabs():
    # Initialize the client
    client = ElevenLabsAPI(API_KEY)
    
    # First, let's get available voices
    voices = client.get_voices()
    print("Available voices:")
    for voice in voices["voices"]:
        print(f"- {voice['name']}: {voice['voice_id']}")
    
    # For testing, let's use the first available voice
    voice_id = voices["voices"][0]["voice_id"]
    
    # Generate a test reminder
    try:
        generate_focus_reminder(
            api_key=API_KEY,
            voice_id=voice_id,
            num_tasks=3,
            current_task="working on the hackathon project"
        )
        print("\nSuccess! Check focus_reminder.mp3 in your current directory")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
def generate_focus_reminder(
    api_key: str,
    voice_id: str,
    num_tasks: int,
    current_task: str
) -> None:
    """Generate a gentle focus reminder based on the current context.
    
    Args:
        api_key (str): ElevenLabs API key
        voice_id (str): ID of the voice to use
        num_tasks (int): Number of current open tasks
        current_task (str): Description of the current task
    """
    client = ElevenLabsAPI(api_key)
    
    # Customize the message based on context
    message = (
        f"I notice you have {num_tasks} tasks open. "
        f"Let's focus on {current_task} for now. "
        "Would you like to take a moment to save the other tabs for later?"
    )
    
    # Generate speech with gentle, stable parameters
    audio_data = client.generate_speech(
        text=message,
        voice_id=voice_id,
        stability=0.7,  # Higher stability for more consistent output
        similarity_boost=0.8,  # Strong similarity to maintain natural voice
        style=0.3,  # Moderate style for gentle delivery
        use_speaker_boost=True
    )
    
    # Save the audio
    client.save_audio(audio_data, "focus_reminder.mp3")


if __name__ == "__main__":
    test_elevenlabs()