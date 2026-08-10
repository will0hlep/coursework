import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERATIONS

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError('api key not found')
client = genai.Client(api_key=api_key)

i = MAX_ITERATIONS

while i > 0:
    response = client.models.generate_content(
        config=types.GenerateContentConfig(system_instruction=system_prompt,
                                            tools=[available_functions]
                                            ),
        model='gemini-2.5-flash',
        contents=messages
        )
    
    for stuff in response.candidates:
        messages.append(stuff.content)

    if response.usage_metadata is None:
        raise RuntimeError('API request failed... no idea why though...')

    if args.verbose:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

    if response.function_calls != None:
        function_results = []
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call)
            if type(function_call_result.parts) != list or function_call_result.parts == []:
                raise Exception
            if function_call_result.parts[0].function_response == None:
                raise Exception
            if function_call_result.parts[0].function_response.response == None:
                raise Exception
            function_results.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
        messages.append(types.Content(role="user", parts=function_results))
        i -= 1
    else:
        print(response.text)
        sys.exit(0)
print('maximum allowed interactions reached')
sys.exit(1)