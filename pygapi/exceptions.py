"""
pygapi.exceptions
~~~~~~~~~~~~~~~~~~

Exceptions used in pygapi.

"""


class UnSupportedExportFormat(Exception):
    """Raised when export format is not supported."""


class pygapiException(Exception):
    """A base class for pygapi's exceptions."""


class SpreadsheetNotFound(pygapiException):
    """Trying to open non-existent or inaccessible spreadsheet."""


class WorksheetNotFound(pygapiException):
    """Trying to open non-existent or inaccessible worksheet."""


class CellNotFound(pygapiException):
    """Cell lookup exception."""


class NoValidUrlKeyFound(pygapiException):
    """No valid key found in URL."""


class IncorrectCellLabel(pygapiException):
    """The cell label is incorrect."""


class InvalidInputValue(pygapiException):
    """The provided values is incorrect."""


class APIError(pygapiException):
    def __init__(self, response):
        super().__init__(self._extract_text(response))
        self.response = response

    def _extract_text(self, response):
        return self._text_from_detail(response) or response.text

    def _text_from_detail(self, response):
        try:
            errors = response.json()
            return errors["error"]
        except (AttributeError, KeyError, ValueError):
            return None
