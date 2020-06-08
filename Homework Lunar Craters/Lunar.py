"""Program for counting lunar craters."""
import os
import re


class File:
    """Create file object from json and parse it."""

    def __init__(self, file_path: str) -> None:
        """"Create new file for parse."""
        self.file_path = os.path.join(os.path.dirname(__file__), file_path)
        self.file = None
        self.matrix = []
        self.list = []

    def file_parser(self) -> list:
        """Create matrix from file."""
        try:
            self.file = open(self.file_path, 'r')
            for line in self.file.readlines():
                line = line.replace(' ', '')
                line = line.replace('\n', '')
                self.matrix.append(list(line))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] == "1":
                        self.matrix[i][j] = 1
                    else:
                        self.matrix[i][j] = 0
            print("File parsed preaty good")
        except (Exception, TypeError) as err:
            print(err)
        finally:
            self.file.close()

    def calculate(self) -> int:
        """Function calculate number of Lunar Craters."""
        number = 0
        while len(self.list) != len(self.matrix) ** 2:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] == 1 and (i, j) not in self.list:
                        coord = (i, j)
                        num = self.find_next((coord))
                        number =number + num
            return number

    def find_next(self, coord: tuple) -> int:
        """Function for looking for next coordinate."""
        if coord not in self.list:
            self.list.append((coord[0], coord[1]))

            if coord[0] != len(self.matrix) - 1:
                value = self.matrix[coord[0] + 1][coord[1]]
                if value == 1:
                    coord_else = (coord[0] + 1, coord[1])
                    self.find_next(coord_else)

            if coord[1] != len(self.matrix[coord[0]]) - 1:
                value = self.matrix[coord[0]][coord[1] + 1]
                if value == 1:
                    coord_else = (coord[0], coord[1] + 1)
                    self.find_next(coord_else)
        return 1


def input_file_fun() -> str:
    """Input file name function."""
    input_file = input("Input name of file from VENV directory ")
    regex = "(?<=)txt"
    if len(input_file) == 0:
        print('input nothing')
        input_file_fun()
    if re.search(regex, input_file) is not None:
        return input_file
    else:
        print('not a file name')
        input_file_fun()


def exit_function() -> bool:
    """Close program or continue."""
    list_of_answer = ['y', 'n']
    answer = input("Please input y for continue, and n for exit ")
    if len(answer) <= 0:
        exit_function()
    if answer in list_of_answer:
        if answer == 'y':
            return True
        else:
            return False
    else:
        print("Please input y or n")
        exit_function()


if __name__ == '__main__':
    answer = True
    while answer is True:
        file_path = input_file_fun()
        new = File(file_path)
        new.file_parser()
        print("There are ", new.calculate(), "Lunar Craters")
        answer = exit_function()
