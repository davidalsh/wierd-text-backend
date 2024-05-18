import random
import re
from typing import Tuple, List
from src.utilities.weird_text_handler import WeirdTextHandler


class Encoder(WeirdTextHandler):
    def __init__(self, text: str):
        super().__init__(text)
        self.words = self._get_text_words()
        self.changed_words: List[str] = []

    @staticmethod
    def shuffle_word(word: str) -> str:
        inner_part = list(word[1:-1])
        random.shuffle(inner_part)
        return f"{word[0]}{''.join(inner_part)}{word[-1]}"

    def add_separator(self) -> str:
        return self.weird_separator + self.text + self.weird_separator + " ".join(self.changed_words)

    def get_weird_text(self) -> str:
        for word_ind in range(len(self.words)):
            word = self.words[word_ind]
            weird_word, has_changed = self.make_weird(word)
            if has_changed:
                self.text = re.sub(word, weird_word, self.text)
                self.changed_words.append(word)
        return self.add_separator()

    def make_weird(self, word: str) -> Tuple[str, bool]:
        if len(word) < 3 or len(set(word[1:-1])) < 2:
            return word, False
        weird_word = self.shuffle_word(word)
        while weird_word == word:
            weird_word = self.shuffle_word(word)
        return weird_word, True
