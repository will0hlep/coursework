import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory_path, target_dir]) == working_directory_path
    if not valid_target_dir:
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    if not os.path.isdir(target_dir):
        return f"Error: '{directory}' is not a directory"
    return_string = 'Result for current directory:'
    for file in os.listdir(target_dir):
        try:
            return_string += f'\n- {file}: file_size={os.path.getsize(os.path.join(target_dir, file))} bytes, is_dir={os.path.isdir(os.path.join(target_dir, file))}'
        except Exception as e:
            return f"Error: executing Python file: {e}"
    return return_string

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)