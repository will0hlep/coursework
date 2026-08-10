import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, directory):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory_path, target_dir]) == working_directory_path
    if not valid_target_dir:
        return f'Error: Cannot read "{directory}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{directory}"'
    try:
        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{directory}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a file, character capped is set in config.py",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Returns the content of a file, character capped is set in config.py",
            ),
        },
    ),
)