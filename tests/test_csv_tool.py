"""
    CSV tool class unit testing
"""

# --- Imports --- #
import csv
import string
import random

from csv_tool import CsvTool

# --- Rand parts & Constants --- #
rand_length=random.randint(1, 10)
LETTERS = string.ascii_lowercase
RANDOM_PART_STR = ''.join(random.choice(LETTERS) for i in range(rand_length))
VALID_EMAIL_ENTY=f"{RANDOM_PART_STR}@example.com"

INVALID_EMAIL_ENTY="invalid-email"
TEST_ENTRIES_PER_ITEM=random.randint(0, 10)

# --- Test cases --- #
def test_is_valid_email():
    """
        Valid email test
    """
    assert bool(CsvTool.is_valid_email(VALID_EMAIL_ENTY)) is True
    assert bool(CsvTool.is_valid_email(INVALID_EMAIL_ENTY)) is False

def test_multiply():
    """
        Multiply method test
    """
    input_file = "./input.csv"
    output_file = "./output.csv"

    # Create test file
    with open(input_file, 'w', encoding='UTF8', newline='') as csv_file:
        # create the csv writer
        writer = csv.writer(csv_file)

        # write a row to the csv file
        contents = [[VALID_EMAIL_ENTY, TEST_ENTRIES_PER_ITEM],
                    [INVALID_EMAIL_ENTY,TEST_ENTRIES_PER_ITEM]]
        for row in contents:
            writer.writerow(row)

    tool = CsvTool()
    tool.multiply(input_file, output_file)

    # Validate output file
    with open(output_file, 'r', encoding='UTF8') as csv_file:
        reader = csv.reader(csv_file)

        entires_cnt = 0
        for row in reader:
            entires_cnt += 1
            assert row[0] == VALID_EMAIL_ENTY

        assert entires_cnt == TEST_ENTRIES_PER_ITEM
