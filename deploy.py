import os
import subprocess
import json

def auto_deploy(instance_path: str, master_api_key: str):
    config_path = os.path.join(instance_path, "config.json")
    with open(config_path) as f:
        config = json.load(f)
    
    if config.get("owner") != master_api_key:
        raise PermissionError("Master API Key mismatch!")
    
    subprocess.run(["pip", "install", "-r", "requirements.txt"], cwd=instance_path)
    subprocess.Popen(["uvicorn", "run_api:app", "--host", "0.0.0.0", "--port", "8000"], cwd=instance_path)
    
    print(f"Deployment complete: {instance_path}")# Auto deploy script
