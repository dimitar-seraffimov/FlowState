from elevenlabs_setup import ElevenLabsAPI
import pygame
import time

def play_mp3(file_path):
    """Play an MP3 file once using pygame."""
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"Error playing file: {e}")
    finally:
        pygame.mixer.quit()

def generate_focus_reminder(
    
    #num_tasks: int,
    #current_intention: str
    message = str
) -> None:
    """Generate a gentle focus reminder based on the current context.
    
    Args:
        num_tasks (int): Number of current open tasks
        current_intention (str): Description of the current task
    """
    client = ElevenLabsAPI()
    
    # Customize the message based on context
    #message = (
    #    f"I notice you have {num_tasks} task streams open. "
    #    f"Let's focus on {current_intention} for now. "
    #    "Would you like to take a moment to save the other tabs for later?"
    #)
    
    # Generate speech with gentle, stable parameters
    audio_data = client.generate_speech(
        text=message,
        stability=0.5,  # Higher stability for more consistent output
        similarity_boost=0.8,  # Strong similarity to maintain natural voice
        style=0.4,  # Moderate style for gentle delivery
        use_speaker_boost=True
    )
    
    # Save the audio
    client.save_audio(audio_data, "focus_reminder.mp3")


if __name__ == "__main__":
    try:
        generate_focus_reminder(
       #     num_tasks = 5,
       #     current_intention = "Working on the hackathon project"
            message = "test message"
        )
        play_mp3("focus_reminder.mp3")       
    except Exception as e:
        print(f"Error: {e}")

        
    
