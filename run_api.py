from fastapi import FastAPI, HTTPException
import json
from auth import verify_master_key

app = FastAPI()

# โหลด config public instance
with open("config/public.json") as f:
    config = json.load(f)

@app.get("/modules")
def list_modules(api_key: str = None):
    if config.get("public_access", False):
        return {"modules": config.get("allowed_modules", []), "owner": "Public"}
    elif api_key and verify_master_key(api_key):
        return {"modules": config.get("allowed_modules", []), "owner": "Super-Admin"}
    return {"modules": [], "owner": None}

@app.post("/update_module")
def update_module(module_name: str, api_key: str):
    if not verify_master_key(api_key):
        raise HTTPException(status_code=403, detail="Permission denied")
    if module_name not in config["allowed_modules"]:
        config["allowed_modules"].append(module_name)
    with open("config/public.json", "w") as f:
        json.dump(config, f, indent=4)
    return {"status": "Module added", "modules": config["allowed_modules"]}
