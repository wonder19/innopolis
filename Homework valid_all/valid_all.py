"""Program for creating decorators."""
import functools
import json
import random
import re
from typing import Any

import jsonschema


class InputParameterVerificationError(Exception):
    """My oun Exeption Class."""

    def __init__(self: Any, message: str) -> None:
        """Create my oun exeption."""
        super().__init__(message)


class ResultVerificationError(Exception):
    """My oun Exeption Class."""

    def __init__(self: Any, message: str) -> None:
        """Create my oun exeption."""
        super().__init__(message)


def valid_all(input_validation, result_validation, on_fail_repeat_times=1, default_behavior=None):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            valid = input_validation()
            if not valid:
                raise InputParameterVerificationError("Not valid input parametr")
            else:
                if on_fail_repeat_times > 1:
                    for i in range(on_fail_repeat_times+1):
                        result = result_validation(func(valid))
                        if result is True:
                            return result
                        else:
                            continue

                    if default_behavior is not None:
                        default_behavior()
                    else:
                        raise ResultVerificationError("Not valid result")

                elif on_fail_repeat_times < 0:
                    result = False
                    while not result:
                        result = result_validation(func(valid))
                        print('we are in looop')

        return wrapper

    return decorate


def regex_validation() -> Any:
    """Validation regex."""
    str_list = ['hhh', 'jjj']
    random_str = random.choice(str_list)
    regex = '[a-z]'
    if re.match(regex, random_str) is not None:
        print("really easy homework")
        return random_str
    else:
        return False


def json_validation(new_dict: dict) -> Any:
    """"""
    with open('new.txt') as scheme:
        parsed_scheme = json.load(scheme)
    try:
        valid = jsonschema.validate(new_dict, parsed_scheme)
        print(new_dict)
        return new_dict
    except jsonschema.ValidationError:
        return False


def default_function():
    """Default function."""
    print("We use default function")


@valid_all(input_validation=regex_validation, result_validation=json_validation, on_fail_repeat_times=-5,
           default_behavior=None)
def main_function(random_str) -> dict:
    """Main Function."""
    if random_str:
        json = {"Key": random_str}
        return json


if __name__ == '__main__':
    main_function()
