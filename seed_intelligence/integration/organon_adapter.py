import json
import sys

def serve(decide, review):
    request = json.load(sys.stdin)
    action = request.pop("action")
    if action == "plan":
        result = decide(**request)
    elif action == "review":
        result = review(**request)
    else:
        raise ValueError(f"unknown controller action: {action}")
    json.dump(result, sys.stdout, ensure_ascii=True, allow_nan=False)
