import sys
import lib
from collections import defaultdict


# Get number of invalid prompts
def get_num_errors():
    try:
        errors_file = open(lib.ERRORS_FILE, 'r')
        error_lines = errors_file.readlines()
        errors_file.close()
        return len(error_lines)
    except FileNotFoundError:
        return 0
    except Exception as e:
        sys.exit("Error opening errors file: {}".format(e))


if __name__ == '__main__':
    num_errors = get_num_errors()

    try:
        prompts_file = open(lib.PROMPTS_FILE, 'r')
    except FileNotFoundError:
        # This likely means that prompt.py has not been run yet with a valid input
        print("Statistics for past prompts\n")

        print("Total number of prompts is {}".format(num_errors))
        print("Total number of valid prompts is 0")
        print("Total number of prompts with errors is {}".format(num_errors))
        exit()
    except Exception as general_exception:
        sys.exit("Error opening prompts file: {}".format(general_exception))

    prompt_lines = prompts_file.readlines()
    num_valid_prompts = len(prompt_lines)

    # To track min and max numerical value encountered across prompts
    min_number = float('inf')
    max_number = float('-inf')

    # To track frequency of each prompt key
    number_frequency = defaultdict(int)
    unit_of_measure_frequency = defaultdict(int)
    place_frequency = defaultdict(int)
    adjective_frequency = defaultdict(int)
    noun_frequency = defaultdict(int)

    # Gather statistics from prompts file
    for line in prompt_lines:
        # Only valid prompts are stored, so it is not needed to validate them again
        prompt = lib.convert_json_to_object(line)

        min_number = min(min_number, prompt.number)
        max_number = max(max_number, prompt.number)
        number_frequency[prompt.number] += 1

        unit_of_measure_frequency[prompt.unit_of_measure] += 1
        place_frequency[prompt.place] += 1
        adjective_frequency[prompt.adjective] += 1
        noun_frequency[prompt.noun] += 1

    prompts_file.close()

    print("Statistics for past prompts\n")

    print("Total number of prompts is {}".format(num_valid_prompts + num_errors))
    print("Total number of valid prompts is {}".format(num_valid_prompts))
    print("Total number of prompts with errors is {}".format(num_errors))
    print()

    print("Minimum value for the numerical input is {}".format(min_number))
    print("Maximum value for the numerical input is {}".format(max_number))
    print("Most common value for number is {}".format(max(number_frequency, key=number_frequency.get)))

    print("Most common value for unit of measure is {}".format(
        max(unit_of_measure_frequency, key=unit_of_measure_frequency.get)))
    print("Most common value for place is {}".format(max(place_frequency, key=place_frequency.get)))
    print("Most common value for adjective is {}".format(max(adjective_frequency, key=adjective_frequency.get)))
    print("Most common value for noun is {}".format(max(noun_frequency, key=noun_frequency.get)))
