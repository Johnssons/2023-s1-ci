from abc import ABC, abstractmethod
from string import ascii_lowercase, ascii_uppercase, punctuation

from .exceptions import (
    EspecialCharacterException,
    MinimumLengthException,
    NoDigitException,
    NoLowerCaseException,
    NoUpperCaseException,
)


class Validator(ABC):
    @abstractmethod
    def validate(self, content) -> None:
        """
        This is the interface of the validation interface.
        :param content: the text to be validated
        :return: None if the text is valid or raise an Exception otherwise.
        """


class LengthValidator(Validator):
    def __init__(self):
        self.minimum_length = 8

    def validate(self, content):
        if self.minimum_length > len(content):
            msg = f"Passwords must have at least {self.minimum_length} characters!"
            raise MinimumLengthException(detail=msg)


class DigitValidator(Validator):
    def __init__(self):
        self.digit_set = set("0123456789")

    def validate(self, content):
        content_set = set(content)
        if self.digit_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 digit!"
            raise NoDigitException(detail=msg)


class LowerCaseValidator(Validator):
    def __init__(self):
        self.lower_case_set = set(ascii_lowercase)

    def validate(self, content):
        content_set = set(content)
        if self.lower_case_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 lower case letter!"
            raise NoLowerCaseException(detail=msg)


class EspecialCharacterValidator(Validator):
    def __init__(self):
        self.especial_set = set(punctuation)

    def validate(self, content):
        content_set = set(content)
        if self.especial_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 especial character!"
            raise EspecialCharacterException(detail=msg)
        if not content_set.isdisjoint(set("/^~")):
            msg = "Passwords must not have any of the following characters: /^~"
            raise EspecialCharacterException(detail=msg)


class UpperCaseValidator(Validator):
    def __init__(self):
        self.upper_case_set = set(ascii_uppercase)

    def validate(self, content):
        content_set = set(content)
        if self.upper_case_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 upper case letter!"
            raise NoUpperCaseException(detail=msg)
