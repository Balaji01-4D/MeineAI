import spacy
from spacy.matcher import Matcher
import re

# Initialize spaCy model
nlp = spacy.load("en_core_web_lg")

# Define file extensions for heuristic identification
FILE_EXTENSIONS = {".pdf", ".txt", ".exe", ".docx", ".html", ".csv", ".yaml", ".json", ".js", ".py"}

def classify_path(path):
    """Classify a path as file or folder based on heuristics."""
    if any(path.endswith(ext) for ext in FILE_EXTENSIONS):
        return "file"
    elif path.endswith("/") or not re.search(r"\.\w+$", path):
        return "folder"
    return "unknown"

def parse_command_with_paths(command):
    """Parse the command to identify operation and classify paths."""
    # Define patterns for actions
    actions = {
        "rename": r"rn|rename",
        "copy": r"copy|cp|\bc\b",
        "move": r"move|mv|push|\bm\b",
        "delete": r"delete|rm|del|remove",
        "create": r"create|mk|make",
        "search": r"search|find",
        "change_dir": r"cd|change directory",
        "list": r"ls",
        "system_info": r"ip|disk|ram|info|time|battery|cpu|gpu|my ip",
    }

    # Tokenize with spaCy
    doc = nlp(command)
    
    # Identify operation
    operation = None
    for action, pattern in actions.items():
        if re.search(pattern, command, re.IGNORECASE):
            operation = action
            break
    
    # Extract file and folder paths
    paths = re.findall(r"/[^\s]+", command)
    classified_paths = [{"path": path, "type": classify_path(path)} for path in paths]
    
    return {
        "operation": operation,
        "paths": classified_paths or None,
        "raw_command": command,
    }

# Test cases
commands = [
    "rn the folder /logs/errors as error_logs",
    "rename the file /home/user/docs/resume.pdf as cv.pdf",
    "copy the folder /images/nature/scenery to /gallery/photos folder",
    "delete the file /documents/assignments/math_homework.pdf",
    "move the file /setup.exe to /tools folder",
    "search the 'manager name' text in reports.csv",
    "cd to /system/tools/utilities as system_utilities",
    "create the folder /data/logs",
    "my ip"
]

for cmd in commands:
    result = parse_command_with_paths(cmd)
    print(result)
