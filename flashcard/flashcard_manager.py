import json
import os

FLASHCARD_FILE = "flashcards.json"

def load_flashcards():
    """Loads flashcards from the file."""
    if os.path.exists(FLASHCARD_FILE):
        with open(FLASHCARD_FILE, "r") as f:
            return json.load(f)
    return {}

def save_flashcard(data):
    """Saves flashcards data to the JSON file."""
    with open(FLASHCARD_FILE, "w") as f:
        json.dump(data, f, indent=2)



def get_topics(data):
    """Returns the list of available topics."""
    return list(data.keys())
