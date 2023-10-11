# running-Python-script-using-sudo
The provided code snippet demonstrates a Python function for running a script in sudo mode `(using the subprocess, and os modules)`. The script takes a Python file name as input and executes it using the "sudo python3 -u" the name of the `script.py` ile.

To use this code, follow these steps:

1. Import the necessary modules:

```python
import subprocess
import os
```

2. Define the  `get_actual_path`  function:
```python
def get_actual_path(python_file_name):
    current_dir = os.getcwd()
    script_path = os.path.join(current_dir, python_file_name)
    actual_path = script_path.replace(" ", r"\ ")
    return actual_path
```

This function takes a  `python_file_name`  parameter and returns the actual path of the file. It first gets the current working directory using  `os.getcwd()` . Then, it joins the current directory with the provided  `python_file_name`  using  `os.path.join()` . Finally, it replaces any spaces in the file path with escaped spaces (to handle paths with spaces in them) and returns the actual path.

3. Define the  `run_script`  function:
```python
def run_script(script_name):
    if not python_file_name.endswith(".py"):
        python_file_name += ".py"

    command = f"sudo python3 -u {script_name}"
    process = subprocess.Popen(command, shell=True)
    process.wait()
```
This function takes a  `script_name`  parameter and runs the script using the  `subprocess.Popen()`  method. It constructs a command string by appending the  `script_name`  to the "sudo python3 -u" command. Then, it creates a subprocess using  `subprocess.Popen()`  and waits for it to complete using  `process.wait()` .


4. Use the functions to run a script:
```python
run_script(str(get_actual_path("Scanner.py")))
```

To run a script named `Scanner.py`, pass its name as a string to the  `run_script()`  function. The  `get_actual_path()`  function is used to get the actual path of the script file.

Note: Make sure to replace `"Scanner.py"` with the actual name of the script you want to run.

Please note that the code snippet uses the "sudo" command, which requires administrative privileges. Adjust the command accordingly if you don't need elevated privileges.

Remember to import the necessary modules and call the functions appropriately in your own code 👍😄.
