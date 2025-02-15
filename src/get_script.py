from openai import OpenAI

from src.prompts import VOICE_ASSISTANT

client = OpenAI()

intended_tasks = "pay water bill"
intruding_tasks = "instagram"


def get_script(intended_tasks : str, intruding_tasks: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": VOICE_ASSISTANT},
            {
                "role": "user",
                "content": f"Important tasks: {intended_tasks}, intruding tasks:  {intruding_tasks}"
            }
        ]
    )

    return completion.choices[0].message
