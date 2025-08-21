import json

def load_master_keys():
    with open("config/master_keys.json") as f:
        return json.load(f).get("super_admin_keys", [])

def verify_master_key(key: str) -> bool:
    return key in load_master_keys()
