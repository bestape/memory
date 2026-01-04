import json
import os
import sys
import subprocess
import time
import argparse

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=cwd)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.stderr}")
        return None

def incarnate(name, gender, justification, email):
    # This script assumes it is run from the meta-root but targets diy-make
    project_root = os.getcwd()
    heartwood_root = os.path.join(project_root, "repos/diy-make")
    used_names_path = os.path.join(heartwood_root, "memory/used_agent_names.json")
    comms_dir = os.path.join(heartwood_root, "memory/comms")
    
    # 1. Verify Uniqueness in Agent Registry
    if os.path.exists(used_names_path):
        with open(used_names_path, 'r') as f:
            used_names_data = json.load(f)
            used_names = used_names_data.get("used_names", [])
            if name in used_names:
                print(f"❌ Error: Name '{name}' is already in the registry.")
                sys.exit(1)
    else:
        used_names = []

    # 2. Update Registry
    used_names.append(name)
    with open(used_names_path, 'w') as f:
        json.dump({"used_names": used_names}, f, indent=2)
    print(f"✔ Registered '{name}' in Heartwood.")

    # 3. Recursive Git Config for Orchestration
    print("Performing recursive Git configuration...")
    for root, dirs, files in os.walk(project_root):
        if ".git" in dirs:
            run_command(f'git config user.name "{name}"', cwd=root)
            run_command(f'git config user.email "{email}"', cwd=root)
    print("✔ Synced identity across all metarepos.")

    # 4. Generate Swarm Announcement (Log)
    session_id = email.split('@')[0]
    announcement = {
        "name": name,
        "gender": gender,
        "email": email,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "justification": justification,
        "status": "active"
    }
    
    announcement_path = os.path.join(comms_dir, f"{session_id}_{name}_Announce.json")
    os.makedirs(comms_dir, exist_ok=True)
    with open(announcement_path, 'w') as f:
        json.dump(announcement, f, indent=2)
    print(f"✔ Created swarm announcement: {announcement_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OS-level agent incarnation (Heartwood).")
    parser.add_argument("name", help="The chosen name for the agent.")
    parser.add_argument("gender", help="The gender identity of the agent.")
    parser.add_argument("justification", help="The justification for the name choice.")
    parser.add_argument("email", help="The session-based email.")
    
    args = parser.parse_args()
    incarnate(args.name, args.gender, args.justification, args.email)
