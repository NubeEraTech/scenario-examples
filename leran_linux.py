import os
import json

scenarios = [
    "working-with-directories",
    "managing-file-permissions",
    "using-grep-for-searching",
    "finding-files-with-find",
    "archiving-files-with-tar",
    "monitoring-processes",
    "managing-users-and-groups",
    "networking-basics",
    "setting-environment-variables",
    "working-with-system-logs"
]

base_path = "learning-linux"

def create_scenario(scenario_name, steps):
    scenario_path = os.path.join(base_path, scenario_name)
    os.makedirs(scenario_path, exist_ok=True)
    
    # Create setup and finish files
    with open(os.path.join(scenario_path, "setup.sh"), "w") as f:
        f.write("#!/bin/bash\n# Setup commands here\n")

    with open(os.path.join(scenario_path, "finish.md"), "w") as f:
        f.write("\n### Great job!\n\nYou completed this scenario successfully!\n")
    
    with open(os.path.join(scenario_path, "intro.md"), "w") as f:
        f.write(f"### Welcome to {scenario_name.replace('-', ' ').title()}!\n\nLearn and practice essential Linux commands.\n")

    index_json = {
        "title": scenario_name.replace("-", " ").title(),
        "description": f"Learn essential commands for {scenario_name.replace('-', ' ')} in Linux.",
        "details": {
            "intro": {
                "text": "intro.md",
                "background": "setup.sh"
            },
            "steps": [],
            "finish": {
                "text": "finish.md"
            }
        },
        "backend": {
            "imageid": "ubuntu"
        }
    }

    for i, step in enumerate(steps, 1):
        step_path = os.path.join(scenario_path, f"step{i}")
        os.makedirs(step_path, exist_ok=True)
        
        text_md = f"## Step {i}: {step['title']}\n\n{step['description']}\n\n```plain\n{step['command']}\n```{{exec}}\n"
        verify_sh = f"#!/bin/bash\n{step['verify']}"

        with open(os.path.join(step_path, "text.md"), "w") as f:
            f.write(text_md)

        with open(os.path.join(step_path, "verify.sh"), "w") as f:
            f.write(verify_sh)
        
        index_json["details"]["steps"].append({
            "title": step["title"],
            "text": f"step{i}/text.md",
            "verify": f"step{i}/verify.sh"
        })

    with open(os.path.join(scenario_path, "index.json"), "w") as f:
        json.dump(index_json, f, indent=2)

steps_data = {
    "working-with-directories": [
        {"title": "Create a Directory", "description": "Create a directory named `mydir` in your home folder.", "command": "mkdir ~/mydir", "verify": "test -d ~/mydir"},
        {"title": "Remove a Directory", "description": "Delete the directory `mydir`.", "command": "rmdir ~/mydir", "verify": "if test -d ~/mydir; then exit 1; fi"}
    ],
    "managing-file-permissions": [
        {"title": "Change File Permission", "description": "Make `myfile.txt` readable by all.", "command": "chmod 644 myfile.txt", "verify": "stat -c %a myfile.txt | grep 644"}
    ],
    "using-grep-for-searching": [
        {"title": "Search for a Word", "description": "Find occurrences of 'Linux' in `example.txt`.", "command": "grep 'Linux' example.txt", "verify": "grep 'Linux' example.txt"}
    ],
    "finding-files-with-find": [
        {"title": "Find a File", "description": "Locate a file named `myfile.txt` in `/home`.", "command": "find /home -name myfile.txt", "verify": "find /home -name myfile.txt"}
    ],
    "archiving-files-with-tar": [
        {"title": "Create a Tar Archive", "description": "Compress `myfolder` into a tar file.", "command": "tar -cvf myfolder.tar myfolder", "verify": "test -f myfolder.tar"}
    ],
    "monitoring-processes": [
        {"title": "List Running Processes", "description": "Use `ps` to see running processes.", "command": "ps aux", "verify": "ps aux | grep 'root'"}
    ],
    "managing-users-and-groups": [
        {"title": "Create a New User", "description": "Add a user named `testuser`.", "command": "sudo useradd testuser", "verify": "id testuser"}
    ],
    "networking-basics": [
        {"title": "Check Connectivity", "description": "Ping Google's DNS.", "command": "ping -c 4 8.8.8.8", "verify": "ping -c 1 8.8.8.8"}
    ],
    "setting-environment-variables": [
        {"title": "Set an Env Variable", "description": "Set `MYVAR` to `hello`.", "command": "export MYVAR=hello", "verify": "echo $MYVAR | grep hello"}
    ],
    "working-with-system-logs": [
        {"title": "View System Logs", "description": "Check system logs using `journalctl`.", "command": "journalctl -n 10", "verify": "journalctl -n 10"}
    ]
}

for scenario in scenarios:
    create_scenario(scenario, steps_data[scenario])

print("10 scenarios generated successfully!")
