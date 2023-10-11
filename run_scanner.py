import subprocess
import os


def get_actual_path(python_file_name):
    if not python_file_name.endswith(".py"):
        python_file_name += ".py"

    current_dir = os.getcwd()
    script_path = os.path.join(current_dir, python_file_name)
    actual_path = script_path.replace(" ", r"\ ")
    return actual_path


def run_script(script_name):
    command = f"sudo python3 -u {script_name}"
    process = subprocess.Popen(command, shell=True)
    process.wait()


run_script(str(get_actual_path("Scanner.py")))
