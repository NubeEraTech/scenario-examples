import os
import json

scenarios = [
    "01-basic-python-syntax",
    "02-working-with-variables",
    "03-conditionals-if-statements",
    "04-loops-for-and-while",
    "05-functions-in-python",
    "06-file-handling",
    "07-error-handling",
    "08-working-with-lists-and-dictionaries",
    "09-using-external-libraries",
    "10-creating-a-simple-cli-script"
]

base_path = "learning-python"

def create_scenario(index, scenario_name, steps):
    scenario_path = os.path.join(base_path, scenario_name)
    os.makedirs(scenario_path, exist_ok=True)
    
    # Create setup and finish files
    with open(os.path.join(scenario_path, "setup.sh"), "w") as f:
        f.write("#!/bin/bash\napt update && apt install -y python3\n")

    with open(os.path.join(scenario_path, "finish.md"), "w") as f:
        f.write(f"\n### Well Done!\n\nYou've successfully completed Scenario {index}: {scenario_name.replace('-', ' ').title()}!\n")
    
    with open(os.path.join(scenario_path, "intro.md"), "w") as f:
        f.write(f"## Scenario {index}: {scenario_name.replace('-', ' ').title()}\n\nLearn and practice Python programming.\n")

    index_json = {
        "title": f"Scenario {index}: {scenario_name.replace('-', ' ').title()}",
        "description": f"Learn essential Python concepts: {scenario_name.replace('-', ' ')}.",
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
        
        text_md = f"## {index}.{i}: {step['title']}\n\n{step['description']}\n\n```python\n{step['code']}\n```{{exec}}\n"
        verify_sh = f"#!/bin/bash\n{step['verify']}"

        with open(os.path.join(step_path, "text.md"), "w") as f:
            f.write(text_md)

        with open(os.path.join(step_path, "verify.sh"), "w") as f:
            f.write(verify_sh)
        
        index_json["details"]["steps"].append({
            "title": f"Step {index}.{i}: {step['title']}",
            "text": f"step{i}/text.md",
            "verify": f"step{i}/verify.sh"
        })

    with open(os.path.join(scenario_path, "index.json"), "w") as f:
        json.dump(index_json, f, indent=2)

steps_data = {
    "01-basic-python-syntax": [
        {"title": "Print a Message", "description": "Print 'Hello, Python!' to the console.", "code": "print('Hello, Python!')", "verify": "python3 -c \"print('Hello, Python!')\" | grep 'Hello, Python!'"},
    ],
    "02-working-with-variables": [
        {"title": "Create a Variable", "description": "Create a variable `x` with value `10` and print it.", "code": "x = 10\nprint(x)", "verify": "python3 -c \"x=10; print(x)\" | grep 10"}
    ],
    "03-conditionals-if-statements": [
        {"title": "Use an `if` Statement", "description": "Check if a number is greater than 5.", "code": "x = 7\nif x > 5:\n    print('x is greater than 5')", "verify": "python3 -c \"x=7; print('x is greater than 5' if x > 5 else '')\" | grep 'x is greater than 5'"}
    ],
    "04-loops-for-and-while": [
        {"title": "Loop Through Numbers", "description": "Print numbers from 1 to 5 using a `for` loop.", "code": "for i in range(1, 6):\n    print(i)", "verify": "python3 -c \"for i in range(1, 6): print(i)\" | grep 5"}
    ],
    "05-functions-in-python": [
        {"title": "Create a Function", "description": "Define a function `greet` that prints 'Hello!'.", "code": "def greet():\n    print('Hello!')\ngreet()", "verify": "python3 -c \"def greet(): print('Hello!'); greet()\" | grep 'Hello!'"},
    ],
    "06-file-handling": [
        {"title": "Write to a File", "description": "Write 'Python is great!' to `output.txt`.", "code": "with open('output.txt', 'w') as f:\n    f.write('Python is great!')", "verify": "cat output.txt | grep 'Python is great!'"},
    ],
    "07-error-handling": [
        {"title": "Handle Division by Zero", "description": "Use `try-except` to handle division by zero errors.", "code": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')", "verify": "python3 -c \"try: result=10/0 except ZeroDivisionError: print('Cannot divide by zero')\" | grep 'Cannot divide by zero'"},
    ],
    "08-working-with-lists-and-dictionaries": [
        {"title": "Access List Elements", "description": "Create a list `[1, 2, 3]` and print the second element.", "code": "numbers = [1, 2, 3]\nprint(numbers[1])", "verify": "python3 -c \"numbers=[1,2,3]; print(numbers[1])\" | grep 2"},
    ],
    "09-using-external-libraries": [
        {"title": "Make an HTTP Request", "description": "Use `requests` to fetch data from `example.com`.", "code": "import requests\nres = requests.get('http://example.com')\nprint(res.status_code)", "verify": "python3 -c \"import requests; res = requests.get('http://example.com'); print(res.status_code)\""},
    ],
    "10-creating-a-simple-cli-script": [
        {"title": "Create a CLI Script", "description": "Write a script that accepts a name and prints a greeting.", "code": "import sys\nname = sys.argv[1]\nprint(f'Hello, {name}!')", "verify": "python3 -c \"import sys; print(f'Hello, Test!')\" | grep 'Hello, Test!'"},
    ]
}

for index, scenario in enumerate(scenarios, 1):
    create_scenario(index, scenario, steps_data[scenario])

print("10 Python scenarios generated successfully!")
