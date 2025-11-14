# test_journal.py
import os
from datetime import datetime
from journal import create_entry

def test_entry_creation(monkeypatch, tmp_path):
    # Patch input() to simulate responses
    monkeypatch.setattr('builtins.input', lambda _: "happy" if "feel" in _ else "Worked on my GitHub project")

    os.chdir(tmp_path)
    create_entry()
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = f"entries/{today}.md"
    assert os.path.exists(filepath)
