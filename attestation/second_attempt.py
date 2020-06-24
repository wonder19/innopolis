"""Task for attestation 'zkdgjepks'."""
import itertools
from pprint import pprint
from typing import Any


class TooMuchParametersException(Exception):
    """Create Exception Class."""

    def __init__(self: Any, message: str) -> None:
        super().__init__(message)


def calculate(dictionary: dict):
    """Calculate possible combinations."""
    planet_list = []
    total = []
    for key in dictionary:
        key_values = dictionary.get(key)
        for item in key_values:
            planet_dict = {key: item}
            planet_list.append(planet_dict)
        total.append(planet_list)
        planet_list = []
        # print(total)

    result = list(itertools.product(*total))
    new_dict = {}
    new_result = []
    for item in result:
        for dicti in item:
            new_dict.update(dicti)
        new_result.append(new_dict)
        new_dict = {}

    if len(new_result) > 100:
        raise TooMuchParametersException("Too much params")
    else:
        return new_result


if __name__ == '__main__':
    a = {
        "атмосфера": ["кислородосодержащая", "отсутствует"],
        "размер": ["карлик", "средний", "великан"]
    }

    pprint(calculate(a))
