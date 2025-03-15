## Generate file links programmatically

# This script generates a markdown file with links to all files in the project directory.
# It skips hidden files and directories, and excludes directories based on patterns.
# The generated links are in the format `[file_path](./file_path) - Add description here`.

import os
import fnmatch


def generate_md_links(
    directory=".", exclude_patterns=[".git", "node_modules", ".github", "__pycache__"]
):
    links = []

    for root, dirs, files in os.walk(directory):
        # Skip excluded directories
        dirs[:] = [
            d
            for d in dirs
            if not any(fnmatch.fnmatch(d, pattern) for pattern in exclude_patterns)
        ]

        path = root.replace("\\", "/")
        if path == ".":
            path = ""
        else:
            path = path[2:]  # Remove './'

        for file in files:
            # Skip hidden files
            if file.startswith("."):
                continue

            file_path = os.path.join(path, file)
            file_path = file_path.replace("\\", "/")
            links.append(f"- [{file_path}](./{file_path}) - Add description here")

    return "\n".join(links)


with open("file_links.md", "w") as f:
    f.write("# Project Files\n\n")
    f.write(generate_md_links())
