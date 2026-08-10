import os
import subprocess
from google.genai import types

def run_python_file(working_directory, directory, args=None):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory_path, target_dir]) == working_directory_path
    if not valid_target_dir:
        return f'Error: Cannot execute "{directory}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: "{directory}" does not exist or is not a regular file'
    if not target_dir.endswith('.py'):
        return f'Error: "{directory}" is not a Python file'
    try:
        command = ["python", target_dir]
        if args != None:
            command.extend(args)
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if completed_process.returncode != 0:
            return f"Process exited with code {completed_process.returncode}"
        if completed_process.stdout == None and completed_process.stderr == None:
            return f"No output produced"
        return f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs a specified python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="runs a specified python file",
            ),
        },
    ),
)