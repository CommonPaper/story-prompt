import json
import sys
from typing import NamedTuple

PROMPTS_FILE = "prompts.txt"
ERRORS_FILE = "errors.txt"
MAX_STR_LENGTH = 127  # Maximum length for each string value in input
STR_KEYS = {"unit_of_measure", "place", "adjective", "noun"}  # Set of string keys to iterate through for validation
TEMPLATE = "One day Anna was walking her {number} {unit_of_measure} commute to {place} and found a {" \
           "adjective} {noun} on the ground."


# Class for input, used to convert json string into an object
class Prompt(NamedTuple):
    number: int
    unit_of_measure: str
    place: str
    adjective: str
    noun: str


# Convert json input to Prompt object
def convert_json_to_object(input_prompt) -> Prompt:
    try:
        return json.loads(input_prompt, object_hook=lambda prompt_dict: Prompt(**prompt_dict))
    except json.JSONDecodeError as json_decode_exception:
        err_msg = "Invalid json: {}".format(json_decode_exception)
        write_to_errors_file(err_msg)
        sys.exit(err_msg)
    except TypeError as type_exception:
        err_msg = "Invalid prompt: {}".format(type_exception)
        write_to_errors_file(err_msg)
        sys.exit(err_msg)


# If an error occurs while generating a story, write the error to errors file and print to stdout
def write_to_errors_file(err: str):
    try:
        file = open(ERRORS_FILE, 'a')
        print(err, file=file)  # Append error to file
        file.close()
    except IOError as io_error:
        sys.exit(
            "Error occurred while writing to errors file. Original error: {}, writing to file error: {}".format(err,
                                                                                                                io_error))


# Write valid input prompts to prompts file
def write_to_prompts_file(prompt: str):
    try:
        file = open(PROMPTS_FILE, 'a')
        print(prompt, file=file)  # Append input prompt to file
        file.close()
    except IOError as e:
        sys.exit("Error writing to stats file: {}".format(e))
