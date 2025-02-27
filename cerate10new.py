import os
import json

# List of scenarios with their tasks
scenarios = [
    ("start-service", "Start a Service", "Start the `apache2` service."),
    ("add-line", "Add a Line to a File", "Add the line `export MY_VAR=123` to `/etc/environment`."),
    ("create-symlink", "Create a Symbolic Link", "Create a symbolic link `/etc/mylink` pointing to `/etc/abc`."),
]

# Verify scripts for each scenario
verify_scripts = {
    "start-service": 'systemctl is-active --quiet apache2 && exit 0 || exit 1',
    "add-line": 'grep -q "export MY_VAR=123" /etc/environment && exit 0 || exit 1',
    "create-symlink": 'LINK="/etc/mylink"; TARGET="/etc/abc"; [ -L "$LINK" ] && [ "$(readlink "$LINK")" == "$TARGET" ] && exit 0 || exit 1',
}

# Base directory
base_dir = "killercoda_scenarios"
os.makedirs(base_dir, exist_ok=True)

for folder, title, task in scenarios:
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)

    # Create Markdown file
    md_filename = f"{folder.replace('-', '_')}.md"
    md_content = f"## Task: {title}\n{task}\n"
    
    with open(os.path.join(folder_path, md_filename), "w") as md_file:
        md_file.write(md_content)

    # Create JSON file
    index_json = {
        "title": f"{title} Test",
        "description": f"Verify {title.lower()}",
        "details": {
            "steps": [
                {
                    "title": title,
                    "text": md_filename,
                    "verify": "verify.sh"
                }
            ]
        },
        "backend": {
            "imageid": "ubuntu"
        }
    }

    with open(os.path.join(folder_path, "index.json"), "w") as json_file:
        json.dump(index_json, json_file, indent=4)

    # Create verify.sh script
    verify_script = f"#!/bin/bash\n{verify_scripts[folder]}\n"
    
    with open(os.path.join(folder_path, "verify.sh"), "w") as sh_file:
        sh_file.write(verify_script)

    # Make verify.sh executable
    os.chmod(os.path.join(folder_path, "verify.sh"), 0o755)

print(f"All scenarios created in '{base_dir}' directory.")
