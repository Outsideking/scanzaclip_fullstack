SCANZACLIP_MODULES = {
    "vision": {"version": "1.0", "description": "Vision AI module"},
    "ai_core": {"version": "2.1", "description": "Core AI processing"},
    "speech": {"version": "1.0", "description": "Speech recognition module"},
    "nlp": {"version": "1.0", "description": "Natural Language Processing module"}
}

def get_module(name):
    return SCANZACLIP_MODULES.get(name)
