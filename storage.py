import json
import cases

def save_cases(path, items):
    if not cases.valid_cases(items):
        return False

    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(items,file,ensure_ascii=False,indent=4)

        return True

    except (OSError, TypeError, ValueError):
        return False


def load_cases(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        return []

    except (OSError, UnicodeError, json.JSONDecodeError):
        return None

    if not cases.valid_cases(data):
        return None

    return data


