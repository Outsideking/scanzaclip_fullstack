# โมดูล Scanzaclip
SCANZACLIP_MODULES = {
    "vision": {"version": "1.0", "description": "Vision AI module"},
    "ai_core": {"version": "2.1", "description": "Core AI processing"}
}

def get_module(name):
    return SCANZACLIP_MODULES.get(name)
