## Program Instructions

### Requirements

This application requires <code>Python 3.9+</code> which can be downloaded [here](https://www.python.org/downloads/).

### How to Run

To run the first command line application and print the story, run the following in the command line:

<code>python3 prompt.py</code>

The input to this prompt should be a json string with keys in lowercase.

Example input:

<code>{"number": 10, "unit_of_measure": "mile", "place": "school", "adjective": "blue", "noun": "rock"}</code>

To run the second command line application to print statistics about previous prompts, run the following in the command
line:

<code>python3 stats.py</code>

Valid prompts are saved in prompts.txt. Generated stories are printed to stdout.

Errors pertaining to invalid prompts are saved in errors.txt and printed to stdout.

## Improvements

1. Add unit tests. 
2. Accept json keys in both lowercase and uppercase.
3. Add more statistics, such as longest string overall and longest string for each string parameter.
4. Store invalid prompts in a file. Currently, only the errors for invalid prompts are saved.
5. Read constants from .env file so that they can be easily changed.
6. Print statistics about most common errors.
7. If there is a tie between most common value for a given statistic, print all tied values.

## Instructions

Thanks for doing this project as part of your interview process. We appreciate your time and want to make this a fun
experience. If you have any questions at all, please reach out to us and we'll get back to you.

Fork a copy of this repository to your Github account and when you have completed the project below, send a link to
ben@commonpaper.com.

## Project

### Story Prompt Generator

One day Anna was walking her {NUMBER} {UNIT_OF_MEASURE} commute to {PLACE} and found a {ADJECTIVE} {NOUN} on the ground.

Write a command line application in any language that accepts a json string of key-value inputs for the template above.
With valid input, the application sends to STDOUT the story using the inputs provided. For example, "One day Anna was
walking her 2 mile commute to school and found a blue rock on the ground." The application stores a record of valid
inputs locally in a file. For the template above, you can assume NUMBER to be numerical data and all other inputs to be
strings containing spaces, special characters, etc. Set sensible string validations for length. Validate all inputs and
handle validation errors gracefully.

Write a second command line application that sends to STDOUT statistics about the stored records, including the maximum
and minimum values for numerical inputs, the most common responses for string inputs, and anything else you think might
be relevant.

Instructions for installing and running your applications should be added to this README file.