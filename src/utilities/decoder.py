import re
from typing import List
from src.utilities.weird_text_handler import WeirdTextHandler


class WeirdTextDecodeError(Exception):
    pass


class Decoder(WeirdTextHandler):
    """
    A class used to decode text which is 'weird'.
    """

    def __init__(self, text: str):
        super().__init__()
        self.input_data = text
        self.original_words: List[str] = []
        self._parse_data()
        self.words = self._get_text_words()

    def _parse_data(self):
        """Parses the input data to separate the weird
        text and the list of original words."""
        input_split = self.input_data.split(self.weird_separator)
        if input_split[0] or len(input_split) != 3:
            raise WeirdTextDecodeError("Invalid input format.")
        self.text = input_split[1]
        self.original_words = input_split[2].split()

    def get_original_text(self) -> str:
        """Decodes the weird text back to its original
        form using the list of original words."""
        for word in self.words:
            for original_word in self.original_words:
                if len(word) == len(original_word) \
                        and set(word) == set(original_word) \
                        and word[0] == original_word[0] \
                        and word[-1] == original_word[-1]:
                    self.text = re.sub(word, original_word, self.text)
                    break
        return self.text
