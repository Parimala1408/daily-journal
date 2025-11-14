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
    print("1. Create today's entry")
    print("2. Generate summary")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        create_entry()
    elif choice == "2":
        summarize_entries()

def summarize_entries():
    """Create a summary file listing all existing entries."""
    import os

    os.makedirs("entries", exist_ok=True)
    files = sorted([f for f in os.listdir("entries") if f.endswith(".md")])
    summary = "entries/summary.md"

    with open(summary, "w", encoding="utf-8") as s:
        s.write("# Journal Summary\n\n")
        for f in files:
            s.write(f"- [{f}]({f})\n")
    print("📝 Summary updated!")
