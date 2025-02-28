import os
import json

# Define 20 scenarios with (folder_name, title, task_description)
scenarios = [
    ("1delete-file", "Delete a File", "Delete the file `/etc/testfile.txt`."),
    ("1delete-folder", "Delete a Folder", "Delete the folder `/etc/testdir`."),
    ("1rename-file", "Rename a File", "Rename `/etc/testfile.txt` to `/etc/testfile_new.txt`."),
    ("1create-group", "Create a Group", "Create a group named `devgroup`."),
    ("1add-user-group", "Add User to Group", "Add `testuser` to the `devgroup` group."),
    ("1change-owner", "Change File Owner", "Change ownership of `/etc/testfile.txt` to `testuser`."),
    ("1change-group", "Change File Group", "Change group ownership of `/etc/testfile.txt` to `devgroup`."),
    ("1list-users", "List All Users", "List all users on the system."),
    ("1list-groups", "List All Groups", "List all groups on the system."),
    ("1kill-process", "Kill a Process", "Kill the process running on port `8080`."),
    ("1create-service", "Create a Service", "Create and enable a service named `mycustom.service`."),
    ("1enable-firewall", "Enable Firewall", "Enable the `ufw` firewall and allow SSH connections."),
    ("1disable-firewall", "Disable Firewall", "Disable the `ufw` firewall."),
    ("1disk-usage", "Check Disk Usage", "Check disk usage and free space on `/`."),
    ("1network-info", "Show Network Information", "Display current network interface details."),
    ("1ping-test", "Ping Test", "Ping `google.com` and confirm connectivity."),
    ("1download-file", "Download a File", "Download `https://example.com/test.txt` and save it as `/etc/testfile.txt`."),
    ("1extract-tar", "Extract a Tar Archive", "Extract `archive.tar.gz` to `/etc/testdir`."),
    ("1mount-drive", "Mount a Drive", "Mount `/dev/sdb1` to `/mnt/drive`."),
    ("1unmount-drive", "Unmount a Drive", "Unmount `/mnt/drive`."),
]

# Verify scripts for each scenario
verify_scripts = {
    "1delete-file": '[ ! -f "/etc/testfile.txt" ] && exit 0 || exit 1',
    "1delete-folder": '[ ! -d "/etc/testdir" ] && exit 0 || exit 1',
    "1rename-file": '[ -f "/etc/testfile_new.txt" ] && exit 0 || exit 1',
    "1create-group": 'getent group devgroup >/dev/null && exit 0 || exit 1',
    "1add-user-group": 'id testuser | grep -q "devgroup" && exit 0 || exit 1',
    "1change-owner": 'stat -c "%U" /etc/testfile.txt | grep -q "testuser" && exit 0 || exit 1',
    "1change-group": 'stat -c "%G" /etc/testfile.txt | grep -q "devgroup" && exit 0 || exit 1',
    "1list-users": 'getent passwd | grep -q "testuser" && exit 0 || exit 1',
    "1list-groups": 'getent group | grep -q "devgroup" && exit 0 || exit 1',
    "1kill-process": '[ -z "$(lsof -i :8080)" ] && exit 0 || exit 1',
    "1create-service": 'systemctl list-unit-files | grep -q "mycustom.service" && exit 0 || exit 1',
    "1enable-firewall": 'ufw status | grep -q "Status: active" && exit 0 || exit 1',
    "1disable-firewall": 'ufw status | grep -q "Status: inactive" && exit 0 || exit 1',
    "1disk-usage": 'df -h | grep -q "/" && exit 0 || exit 1',
    "1network-info": 'ip addr show | grep -q "inet " && exit 0 || exit 1',
    "1ping-test": 'ping -c 1 google.com >/dev/null 2>&1 && exit 0 || exit 1',
    "1download-file": '[ -f "/etc/testfile.txt" ] && exit 0 || exit 1',
    "1extract-tar": '[ -d "/etc/testdir" ] && exit 0 || exit 1',
    "1mount-drive": 'mount | grep -q "/mnt/drive" && exit 0 || exit 1',
    "1unmount-drive": '[ ! -d "/mnt/drive" ] && exit 0 || exit 1',
}

# Base directory for all scenarios
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

print(f"All 20 scenarios created in '{base_dir}' directory.")
