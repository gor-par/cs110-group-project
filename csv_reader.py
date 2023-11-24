import os
import csv
from utils import get_input, InvalidFilenameError


class CsvReader:

    def __init__(self, path):
        '''
        Creates a CsvReader instance, opens the data and parses it
        '''
        try:
            CsvReader.verify_path(path)
            self.path = path
            self.filename = os.path.basename(path)

            self.__file = (open(self.filename, 'r'))
            self.__parse_csv()
            self.__file.close()

            self.length = len(self.rows)
            self.column_count = len(self.fieldnames)

        except InvalidFilenameError:
            # re-raises the errors for the caller to handle
            raise

    def verify_path(path):
        '''
        Checks the path to be a csv file and raises an error if not

        Args:
        path (str): pahth to verify
        '''

        if path[-3:].lower() != 'csv':
            raise InvalidFilenameError("File is not CSV")
        elif not os.path.isfile(path):
            raise InvalidFilenameError("File does not exist")
        elif not os.access(path, os.R_OK):
            raise InvalidFilenameError("Need permission to read the file")

    def __parse_csv(self):
        '''
        Parses and stores the rows and fieldnames of the dataset
        '''
        reader = csv.DictReader(self.__file)

        rows = []
        for row in reader:
            for column in row:
                row[column] = self.__round_if_numeric(row[column])
            rows.append(row)

        self.rows = rows
        self.fieldnames = reader.fieldnames

    def __round_if_numeric(self, string):
        '''
        Args:
        string (str): The data entry to be rounded

        Returns:
        unchanged string or float rounded to 0.001
        '''
        try:
            return round(float(string), 3)
        except ValueError:
            return string
