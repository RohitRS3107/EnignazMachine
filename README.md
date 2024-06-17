# Word to Number Converter
# Overview

# This project involves a Python program that converts a given string of words into a sequence of numbers based on their positions in the alphabet. The converted numbers can then be translated back to the original string using the same mapping.
# Features

    Converts words into numeric sequences based on alphabetical positions.
    Supports conversion of uppercase and lowercase letters.
    Handles multiple words and sentences.
    Provides a reverse operation to convert numbers back to the original text.

# Technologies Used

    Programming Language: Python
    Libraries: None (Pure Python implementation)
Getting Started
Prerequisites

    Python 3.7 or higher

Installation

Clone the repository:

bash

git clone https://github.com/rohitrs3107/EnignazMachine
cd EningnazMachine


Usage

    Convert Words to Numbers:
        Run Mains.py to convert words/sentences to numeric sequences.

    bash

python src/Mains.py

Output:

makefile

Input: Hello World
Output: 8 5 12 12 15 23 15 18 12 4

Convert Numbers to Words:

    Run Mains.py to convert numeric sequences back to words/sentences.

bash

python src/Mains.py --input "8 5 12 12 15 23 15 18 12 4"

Output:

makefile

    Input: 8 5 12 12 15 23 15 18 12 4
    Output: hello world

Example

python

from src.word_to_number import word_to_number
from src.number_to_word import number_to_word

# Convert words to numbers
input_text = "Hello World"
numeric_sequence = word_to_number(input_text)
print("Numeric Sequence:", numeric_sequence)

# Convert numbers back to words
output_text = number_to_word(numeric_sequence)
print("Output Text:", output_text)
