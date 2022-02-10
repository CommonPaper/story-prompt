import sys
import lib


# Validate lengths of string values
def validate_input(input_to_validate: lib.Prompt):
    is_err = False
    for key in lib.STR_KEYS:
        value = getattr(input_to_validate, key)
        if len(value) > lib.MAX_STR_LENGTH:
            print("{} value is too long".format(key))
            is_err = True

    if is_err:
        failed_validation_err = "Input validation failed"
        lib.write_to_errors_file(failed_validation_err)
        sys.exit(failed_validation_err)


if __name__ == '__main__':
    input_prompt = input("Enter the prompt\n")
    input_prompt = input_prompt.strip()  # Trim whitespace

    prompt_tuple = lib.convert_json_to_object(input_prompt)  # Convert json input to a NamedTuple
    validate_input(prompt_tuple)

    lib.write_to_prompts_file(input_prompt)  # Save the json input to prompts file
    print(lib.TEMPLATE.format(number=prompt_tuple.number, unit_of_measure=prompt_tuple.unit_of_measure,
                              place=prompt_tuple.place, adjective=prompt_tuple.adjective, noun=prompt_tuple.noun))
