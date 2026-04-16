from rag import get_memory
from llm import ask_llm, extract_preference
from notifier import send_message
import pandas as pd
from datetime import datetime, timedelta

# Load data
df = pd.read_csv("data/events.csv")

# Get tomorrow's date
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

# Find matching events
events = df[df['date'] == tomorrow]

if events.empty:
    send_message("No events tomorrow 🎉")
else:
   for _, row in events.iterrows():
    memory = get_memory(row['name'])

if not memory or memory == "":
    memory = row['notes']  # fallback to CSV"No specific preferences"
    preference = extract_preference(memory)

    prompt = f"""
Tomorrow is {row['name']}'s {row['type']}.

Known preference: {preference}

IMPORTANT:
- Suggest gift ONLY from this category
- Keep it short (2–3 lines)
- Add emojis

Give:
1. Reminder
2. Gift idea
"""
    ai_response = ask_llm(prompt)

    send_message(f"✨ {row['name']}'s Reminder\n\n{ai_response}")

print("Memory:", memory)
print("Extracted preference:", preference)
    