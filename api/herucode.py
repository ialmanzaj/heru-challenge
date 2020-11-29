
class HeruCode:
    ALPHA = "sxocqnmwpfyheljrdgui"
    FOO_LETTERS = "udxsmpf"
    ALPHABETH = {c: i for i, c in enumerate(ALPHA)}

    def __init__(self, text=None):
        self.words = text.split(" ") if text else None

    def get_total_prepositions(self):
        return sum(1 for w in self.words if self.is_preposition(w))

    def get_total_verbs(self):
        return sum(1 for w in self.words if self.is_a_verb(w))

    def get_vocabulary_list(self):
        # sort topologically
        return sorted(set(self.words), key=lambda word: [self.ALPHABETH[c] for c in word])

    def get_total_subjunctive_verbs(self):
        return sum(1 for w in self.words if self.is_subjunctive_verb(w))

    def is_a_verb(self, word: str) -> bool:
        return len(word) >= 6 and word[len(word) - 1] not in self.FOO_LETTERS

    def is_preposition(self, word: str) -> bool:
        return len(word) == 6 and word[len(word) - 1] in self.FOO_LETTERS and "u" not in word

    def is_subjunctive_verb(self, word: str) -> bool:
        return self.is_a_verb(word) and word[0] not in self.FOO_LETTERS

    def get_pretty_number(self, word: str) -> int:
        return 0

    def convert_word_to_number(self, word: str) -> int:
        # base conversion
        # alphabeth 0-19
        # sxocqnmwpfyheljrdgui
        # the Herucode word gxjrc represents the number 605637 ->(17 + 1 + 14 + 15 + 4)
        ans = 0
        for i, c in enumerate(word):
            base = 20
            ans *= base
            #print(i, c, base, ans, self.ALPHABETH[c])
            ans += self.ALPHABETH[c]
        return ans
