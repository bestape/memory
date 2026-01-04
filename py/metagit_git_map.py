import os
import json
import time

def generate_git_map(repo_root, output_path, agent_name):
    """
    Generates a structural map of the current Git repository,
    focusing on chrono-fractal heartwood nodes.
    """
    mappings = []
    
    # Identify key nodes
    # 1. Root JSON
    root_json = os.path.join(repo_root, "json")
    if os.path.exists(root_json):
        mappings.append({
            "path": "json/",
            "type": "heartwood_root",
            "status": "active",
            "description": "The legislative core of the repository."
        })

    # 2. Chrono-Fractal Scan (Last 2 days)
    for year in ['2025', '2026']:
        y_path = os.path.join(repo_root, year)
        if not os.path.exists(y_path): continue
        
        for q in ['Q1', 'Q2', 'Q3', 'Q4']:
            q_path = os.path.join(y_path, q)
            if not os.path.exists(q_path): continue
            
            # Simple walk to find leaf json dirs
            for root, dirs, files in os.walk(q_path):
                if root.endswith("/json"):
                    rel_path = os.path.relpath(root, repo_root)
                    mappings.append({
                        "path": rel_path + "/",
                        "type": "heartwood_leaf",
                        "status": "active" if "2026" in rel_path else "archived",
                        "contains": files[:5] # Sample first 5 files
                    })

    # 3. Substrate Scan
    substrate_nodes = ["webm", "pdf", "png"]
    for node in substrate_nodes:
        n_path = os.path.join(repo_root, "..", node) # Substrate is often next to public/
        if os.path.exists(n_path):
            mappings.append({
                "path": node + "/",
                "type": "substrate",
                "status": "active",
                "description": "Cloud-synced binary storage."
            })

    output_data = {
        "title": "Git Map: Memory Public",
        "version": "1.0",
        "generated_at": int(time.time()),
        "attribution": f"{agent_name} ({time.strftime('%Y%m%d-%H%M%S')})",
        "description": "Forensic map of the internal repository structure.",
        "mappings": mappings
    }

    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"✅ Git map generated at: {output_path}")

if __name__ == "__main__":
    # Dynamically determine the repository root
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # Load agent name from session environment if available
    session_env_path = os.path.abspath(os.path.join(repo_root, "../../../../.gemini/session_env.json"))
    agent_name = "Unknown"
    session_id = time.strftime("%Y%m%d-%H%M%S")
    
    if os.path.exists(session_env_path):
        try:
            with open(session_env_path, 'r') as f:
                env_data = json.load(f)
                agent_name = env_data.get("agent_name", "Unknown")
                session_id = env_data.get("session_id", session_id)
        except Exception:
            pass

    # Output to the current day's chrono-fractal json
    # Attempt to find or create the correct fractal path
    year, quarter, month, day = time.strftime("%Y Q%q %m %d").replace("Q1", "Q1").replace("Q2", "Q2").replace("Q3", "Q3").replace("Q4", "Q4").split()
    # Note: %q is not standard strftime, manually calculating quarter
    month_int = int(time.strftime("%m"))
    quarter = f"Q{(month_int-1)//3 + 1}"
    
    output_dir = os.path.join(repo_root, year, quarter, time.strftime("%m/%d"), "json")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{session_id}_metagit_git_map.json")
    
    generate_git_map(repo_root, output_file, agent_name)
