# journal.py
# Daily Journal Creator — saves entries as Markdown files.

from datetime import datetime
import os

def create_entry():
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"entries/{today}.md"
    os.makedirs("entries", exist_ok=True)

    if os.path.exists(filename):
        print(f"Entry for {today} already exists.")
        return

    mood = input("How are you feeling today? (happy/sad/productive): ").strip()
    note = input("Write a quick note about your day: ").strip()

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {today}\n\n")
        f.write(f"**Mood:** {mood}\n\n")
        f.write(f"**Note:** {note}\n\n")
        f.write("---\n")
        f.write(f"Created on {datetime.now().strftime('%H:%M:%S')}\n")

    print(f"✅ Journal entry created: {filename}")

if __name__ == "__main__":
    create_entry()
