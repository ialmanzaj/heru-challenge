
class HeruCode:
    ALPHA = "sxocqnmwpfyheljrdgui"
    FOO_LETTERS = "udxsmpf"
    ALPHABETH = {c: i for i, c in enumerate(ALPHA)}

    def __init__(self, text=""):
        self.words = text.split(" ")

    def get_total_prepositions(self) -> int:
        return sum(1 for w in self.words if self.is_preposition(w))

    def get_total_verbs(self) -> int:
        return sum(1 for w in self.words if self.is_a_verb(w))

    def sort_topo(self, word: str) -> List[str]:
        return [self.ALPHABETH[c] for c in word]

    def sort_word_topo(self, word: str) -> str:
        # sort topologically
        return "".join(sorted(word, key=self.sort_topo))

    def get_vocabulary_list(self) -> List[str]:
        # sort list of words
        return sorted(set(self.words), key=self.sort_topo)

    def get_total_subjunctive_verbs(self) -> int:
        return sum(1 for w in self.words if self.is_subjunctive_verb(w))

    def is_a_verb(self, word: str) -> bool:
        return len(word) >= 6 and word[len(word) - 1] not in self.FOO_LETTERS

    def is_preposition(self, word: str) -> bool:
        return len(word) == 6 and word[len(word) - 1] in self.FOO_LETTERS and "u" not in word

    def is_subjunctive_verb(self, word: str) -> bool:
        return self.is_a_verb(word) and word[0] not in self.FOO_LETTERS

    def get_pretty_number(self) -> int:
        words_as_numbers = [self.convert_word_to_number(
            word) for word in self.words]
        return sum(1 for number in words_as_numbers if number >= 81827 and number % 3 == 0)

    def convert_word_to_number(self, word: str) -> int:
        # base conversion
        # alphabeth 0-19
        # the Herucode word gxjrc represents the number 605637 ->(17 + 20 + 5600 + 120000 + 480000)
        return sum(20 ** i * self.ALPHABETH[letter] for i, letter in enumerate(word))
