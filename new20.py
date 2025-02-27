import os
import json

# Define 20 scenarios with (folder_name, title, task_description)
scenarios = [
    ("delete-file", "Delete a File", "Delete the file `/etc/testfile.txt`."),
    ("delete-folder", "Delete a Folder", "Delete the folder `/etc/testdir`."),
    ("rename-file", "Rename a File", "Rename `/etc/testfile.txt` to `/etc/testfile_new.txt`."),
    ("create-group", "Create a Group", "Create a group named `devgroup`."),
    ("add-user-group", "Add User to Group", "Add `testuser` to the `devgroup` group."),
    ("change-owner", "Change File Owner", "Change ownership of `/etc/testfile.txt` to `testuser`."),
    ("change-group", "Change File Group", "Change group ownership of `/etc/testfile.txt` to `devgroup`."),
    ("list-users", "List All Users", "List all users on the system."),
    ("list-groups", "List All Groups", "List all groups on the system."),
    ("kill-process", "Kill a Process", "Kill the process running on port `8080`."),
    ("create-service", "Create a Service", "Create and enable a service named `mycustom.service`."),
    ("enable-firewall", "Enable Firewall", "Enable the `ufw` firewall and allow SSH connections."),
    ("disable-firewall", "Disable Firewall", "Disable the `ufw` firewall."),
    ("disk-usage", "Check Disk Usage", "Check disk usage and free space on `/`."),
    ("network-info", "Show Network Information", "Display current network interface details."),
    ("ping-test", "Ping Test", "Ping `google.com` and confirm connectivity."),
    ("download-file", "Download a File", "Download `https://example.com/test.txt` and save it as `/etc/testfile.txt`."),
    ("extract-tar", "Extract a Tar Archive", "Extract `archive.tar.gz` to `/etc/testdir`."),
    ("mount-drive", "Mount a Drive", "Mount `/dev/sdb1` to `/mnt/drive`."),
    ("unmount-drive", "Unmount a Drive", "Unmount `/mnt/drive`."),
]

# Verify scripts for each scenario
verify_scripts = {
    "delete-file": '[ ! -f "/etc/testfile.txt" ] && exit 0 || exit 1',
    "delete-folder": '[ ! -d "/etc/testdir" ] && exit 0 || exit 1',
    "rename-file": '[ -f "/etc/testfile_new.txt" ] && exit 0 || exit 1',
    "create-group": 'getent group devgroup >/dev/null && exit 0 || exit 1',
    "add-user-group": 'id testuser | grep -q "devgroup" && exit 0 || exit 1',
    "change-owner": 'stat -c "%U" /etc/testfile.txt | grep -q "testuser" && exit 0 || exit 1',
    "change-group": 'stat -c "%G" /etc/testfile.txt | grep -q "devgroup" && exit 0 || exit 1',
    "list-users": 'getent passwd | grep -q "testuser" && exit 0 || exit 1',
    "list-groups": 'getent group | grep -q "devgroup" && exit 0 || exit 1',
    "kill-process": '[ -z "$(lsof -i :8080)" ] && exit 0 || exit 1',
    "create-service": 'systemctl list-unit-files | grep -q "mycustom.service" && exit 0 || exit 1',
    "enable-firewall": 'ufw status | grep -q "Status: active" && exit 0 || exit 1',
    "disable-firewall": 'ufw status | grep -q "Status: inactive" && exit 0 || exit 1',
    "disk-usage": 'df -h | grep -q "/" && exit 0 || exit 1',
    "network-info": 'ip addr show | grep -q "inet " && exit 0 || exit 1',
    "ping-test": 'ping -c 1 google.com >/dev/null 2>&1 && exit 0 || exit 1',
    "download-file": '[ -f "/etc/testfile.txt" ] && exit 0 || exit 1',
    "extract-tar": '[ -d "/etc/testdir" ] && exit 0 || exit 1',
    "mount-drive": 'mount | grep -q "/mnt/drive" && exit 0 || exit 1',
    "unmount-drive": '[ ! -d "/mnt/drive" ] && exit 0 || exit 1',
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
