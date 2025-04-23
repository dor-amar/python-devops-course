#!/usr/bin/env python3

import os
import re
import sys

# Module files in order from the course
MODULE_FILES = [
    "shell-vs-python.md",
    "intro-to-python.md",
    "python-syntax.md",
    "variables.md",
    "string-num-index.md",
    "user-input.md",
    "type-casting.md",
    "functions.md",
    "if-else.md",
    "loops.md",
    "list.md",
    "dictionary.md",
    "dictionary-vs-json.md",
    "exception-handling.md",
    "files.md",
    "json.md",
    "modules.md",
    "api.md",
    "working-with-api.md",
    "working-with-api-2.md",
    "oop.md",
    "inheritance-polymorphism.md",
    "abstraction-encapsulation.md",
    "flask-intro.md",
    "flask-hello-world.md",
    "flask-route-template-form.md",
    "db-sql.md",
    "sqlite3.md",
    "flask-sqlite3.md",
    "rest-api.md"
]

BASE_DIR = "modules/python-basics"

def get_title(file_path):
    """Extract the title from a markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Try to find a H1 heading (# Title)
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
            
            # If no heading found, use the filename
            basename = os.path.basename(file_path)
            return os.path.splitext(basename)[0].replace('-', ' ').title()
    except:
        # Fallback to formatted filename
        basename = os.path.basename(file_path)
        return os.path.splitext(basename)[0].replace('-', ' ').title()

def add_navigation(file_path, prev_file=None, next_file=None):
    """Add navigation section to the end of a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if navigation section already exists
    if re.search(r'^## Navigation\s*$', content, re.MULTILINE):
        # Remove existing navigation section
        content = re.sub(r'\n---\n## Navigation\n\n.*?(\n\n|\n$|\Z)', '', content, flags=re.DOTALL)
    
    # Prepare navigation links
    nav_links = []
    if prev_file:
        prev_title = get_title(os.path.join(BASE_DIR, prev_file))
        nav_links.append(f"[⬅️ Previous: {prev_title}]({prev_file})")
    
    if next_file:
        next_title = get_title(os.path.join(BASE_DIR, next_file))
        nav_links.append(f"[Next: {next_title} ➡️]({next_file})")
    
    # Add navigation section
    nav_bar = " | ".join(nav_links)
    if nav_bar:
        content = content.rstrip() + f"\n\n---\n## Navigation\n\n{nav_bar}\n"
    
    # Write updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Added navigation to {file_path}")

def main():
    # Process each file in the array
    for i, filename in enumerate(MODULE_FILES):
        file_path = os.path.join(BASE_DIR, filename)
        
        # Only process if file exists
        if os.path.isfile(file_path):
            # Determine previous and next files
            prev_file = MODULE_FILES[i-1] if i > 0 else None
            next_file = MODULE_FILES[i+1] if i < len(MODULE_FILES) - 1 else None
            
            # Add navigation
            add_navigation(file_path, prev_file, next_file)

if __name__ == "__main__":
    main()
    print("Navigation sections added to all module files!") 