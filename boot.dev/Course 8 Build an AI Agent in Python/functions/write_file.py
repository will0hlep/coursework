import os
from google.genai import types

def write_file(working_directory, directory, content):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory_path, target_dir]) == working_directory_path
    if not valid_target_dir:
        return f'Error: Cannot write to "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(target_dir):
        return f'Error: Cannot write to "{directory}" as it is a directory'
    try:
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{directory}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes content to a specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="writes content to a specified file",
            ),
        },
    ),
)