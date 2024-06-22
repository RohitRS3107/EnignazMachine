# Word to Number Converter
# Overview

This project involves a Python program that converts a given string of words into a sequence of numbers based on their positions in the alphabet. The converted numbers can then be translated back to the original string using the same mapping.
# Features

- Converts words into numeric sequences based on alphabetical positions.
- Supports conversion of uppercase and lowercase letters.
- Handles multiple words and sentences.
- Provides a reverse operation to convert numbers back to the original text.

# Technologies Used

- Programming Language: Python
- Libraries: None (Pure Python implementation)
# Getting Started
- Prerequisites

Python 3.7 or higher

- Installation

Clone the repository:



    git clone https://github.com/rohitrs3107/EnignazMachine
    cd EningnazMachine



    python src/Mains.py



# Convert words to numbers
input_text = "Hello World"
numeric_sequence = word_to_number(input_text)
print("Numeric Sequence:", numeric_sequence)

# Convert numbers back to words
output_text = number_to_word(numeric_sequence)
print("Output Text:", output_text)
