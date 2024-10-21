import os
import re
import sys

def get_first_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()
        # Remove Markdown heading symbols and whitespace
        return re.sub(r'^#+\s*', '', first_line)

def create_toc(root_dir, current_dir):
    toc = []
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        if level > 0:
            subdir = os.path.basename(root)
            toc.append(f"{'  ' * (level - 1)}- {subdir}\n")
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, current_dir)
                title = get_first_line(file_path)
                toc.append(f"{'  ' * level}- [{title}]({relative_path})\n")
    
    return ''.join(toc)

if __name__ == "__main__":
    current_dir = os.getenv('CUR_DIR')
    docs_dir = "docs"

    if not os.path.exists(docs_dir):
        print(f"Error: 'docs' directory not found in {current_dir}")
        sys.exit(1)

    toc = create_toc(docs_dir, current_dir)
    print(toc)