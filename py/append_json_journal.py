import json
import os
import sys

def append_json_journal(json_block_str, journal_path):
    try:
        new_entry = json.loads(json_block_str)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON block: {str(e)}")
        sys.exit(1)

    os.makedirs(os.path.dirname(journal_path), exist_ok=True)

    if os.path.exists(journal_path):
        with open(journal_path, 'r') as f:
            try:
                journal = json.load(f)
            except json.JSONDecodeError:
                journal = []
    else:
        journal = []

    if not isinstance(journal, list):
        print(f"⚠️ Warning: Journal at {journal_path} is not a list. Resetting.")
        journal = []

    journal.append(new_entry)

    with open(journal_path, 'w') as f:
        json.dump(journal, f, indent=2)
    
    print(f"✔ Appended entry to {journal_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python py/append_json_journal.py '<json_block>' <journal_path>")
        sys.exit(1)
    
    append_json_journal(sys.argv[1], sys.argv[2])
