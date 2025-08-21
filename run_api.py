from fastapi import FastAPI, HTTPException
import json
from auth import verify_master_key

app = FastAPI()

# โหลด config ของ instance
with open("config/country_x.json") as f:
    config = json.load(f)

@app.get("/modules")
def list_modules(api_key: str = None):
    if api_key and verify_master_key(api_key):
        return {"modules": config.get("allowed_modules", []), "owner": "Super-Admin"}
    return {"modules": config.get("allowed_modules", []), "owner": config.get("owner")}

@app.post("/update_module")
def update_module(module_name: str, api_key: str):
    if not verify_master_key(api_key):
        raise HTTPException(status_code=403, detail="Permission denied")
    if module_name not in config["allowed_modules"]:
        config["allowed_modules"].append(module_name)
    with open("config/country_x.json", "w") as f:
        json.dump(config, f, indent=4)
    return {"status": "Module added", "modules": config["allowed_modules"]}
