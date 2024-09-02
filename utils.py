import json
from constants import CONFIG_PATH, PROMPT_PATH, LOG_FILE


def load_config():
    with open(CONFIG_PATH, 'r') as file:
        return json.load(file)


def load_prompts():
    with open(PROMPT_PATH, 'r') as file:
        return json.load(file)


def log_response(message):
    with open(LOG_FILE, 'a') as file:
        file.write(message + "\n")
