from openai import OpenAI

from src.models.models import ActiveTasks, ActiveTabs, Tab
from src.prompts import IDENTIFY_TASKS

client = OpenAI(
    api_key="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"
)

active_tabs = ActiveTabs(
    tabs=[
        Tab(index="0", window_id="1", title="Google Maps - London", url="https://www.google.com/maps/place/London", active="false", status="complete"),
        Tab(index="1", window_id="1", title="Amazon.co.uk: Wireless Headphones", url="https://www.amazon.co.uk/dp/B09XYZ123", active="false", status="complete"),
        Tab(index="2", window_id="1", title="Thames Water - My Account", url="https://www.thameswater.co.uk/my-account", active="true", status="complete"),
        Tab(index="3", window_id="1", title="Thames Water - Pay My Bill", url="https://www.thameswater.co.uk/pay-my-bill", active="false", status="complete"),
        Tab(index="4", window_id="1", title="Thames Water - Report a Leak", url="https://www.thameswater.co.uk/report-a-leak", active="false", status="complete")
    ]
)


completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": IDENTIFY_TASKS},
        {"role": "user", "content": f"str {str(active_tabs)} "},
    ],
    response_format=ActiveTasks,
)

response = completion.choices[0].message.parsed




