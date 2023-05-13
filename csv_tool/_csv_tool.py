"""
    Tool, for managing CSV files
"""

# --- Imports --- #
import re
import csv

# --- Print Utils --- #
class CsvTool():
    """
        docstring for CsvTool
    """
    def __init__(self):
        pass

    @staticmethod
    def is_valid_email(address: str) -> bool:
        """
            Validates an email address
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, address)

    def multiply(self, input_file: str, output_file: str):
        """
            Reads the contents provided by `input_file.csv`, multiplies
            email addresses from row0 by N times defined by row1. Stores
            the results into `output_file.csv`

            @input_file: Input CSV file in the format of email_address,int
            @output_file: Output file path (results)
        """
        print(f"--- Info: Processing input file {input_file}")
        with open(input_file, 'r', encoding="utf8") as reader_fd, \
            open(output_file, 'w+', encoding="utf8") as writer_fd:
            reader = csv.reader(reader_fd, delimiter=',')
            writer = csv.writer(writer_fd, delimiter=',',
                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                for row in reader:
                    email = row[0]
                    multiplier = int(row[1])

                    if self.is_valid_email(email):
                        print(f"--- Info: Adding entry for {email} (x{multiplier})")
                        for _ in range(multiplier):
                            writer.writerow([email])
                    else:
                        print(f"--- Err: Invalid email address: {email}!")
            except csv.Error as err:
                raise f'file {input_file}, line {reader.line_num}: {err}'

        print(f"--- Info: Output saved in: {output_file}")

class CsvToolException(Exception):
    """
        Exception fo CsvTool class
    """
