from rag import store_event
import pandas as pd

df = pd.read_csv("data/events.csv")

for _, row in df.iterrows():
   context = f"{row['name']} is a {row['type']} and {row['notes']}"
store_event(row['name'], context)

print("✅ Memory stored successfully!")