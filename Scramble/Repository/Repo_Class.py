from copy import deepcopy
from random import randint


class Repo:
    def __init__(self):
        f = open("text_file.txt", "r")
        lines = f.readlines()
        n = len(lines)
        f.close()
        self.sentence = lines[randint(0, n - 1)].split()

        self.score = 0
        self.compute_score()
        self.winning_sentence = deepcopy(self.get_sentence()[1])

    def compute_score(self):
        for i in range(0, len(self.sentence)):
            self.score = self.score + len(self.sentence[i])

    def get_score(self):
        return self.score

    def get_sentence(self):
        score = self.get_score()
        return score, ' '.join(self.sentence)

    def swap_letters(self, word1, ind1, word2, ind2):
        if len(self.sentence[word1]) > 2 and len(self.sentence[word2]) > 2:
            if word1 > len(self.sentence) - 1 or word1 < 0:
                raise ValueError
            elif ind1 > len(self.sentence[word1]) - 2 or ind1 < 1:
                raise ValueError
            elif word2 > len(self.sentence) - 1 or word2 < 0:
                raise ValueError
            elif ind2 > len(self.sentence[word2]) - 2 or ind2 < 1:
                raise ValueError
            else:
                if (word1 == word2 and ind1 != ind2):
                    aux = deepcopy(self.sentence[word1])
                    aux = list(aux)
                    aux[ind1], aux[ind2] = aux[ind2], aux[ind1]
                    self.sentence[word1] = ''.join(aux)
                else:
                    aux1 = deepcopy(self.sentence[word1])
                    aux2 = deepcopy(self.sentence[word2])
                    aux1 = list(aux1)
                    aux2 = list(aux2)

                    aux1[ind1], aux2[ind2] = aux2[ind2], aux1[ind1]

                    self.sentence[word1] = ''.join(aux1)
                    self.sentence[word2] = ''.join(aux2)

    def update_score(self):
        self.score = self.score - 1

    def scramble_letters(self):
        number_of_swaps = self.score * 2
        number_of_words = len(self.sentence)

        for i in range(0, number_of_swaps):
            word1 = randint(0, number_of_words)
            if word1 == number_of_words:
                word1 -= 1
            ind1 = randint(-3, len(self.sentence[word1]) - 2)
            if ind1 < 1:
                ind1 = 1
            word2 = randint(0, number_of_words)
            if word2 == number_of_words:
                word2 -= 1
            ind2 = randint(-3, len(self.sentence[word2]) - 2)
            if ind2 < 1:
                ind2 = 1
            self.swap_letters(word1, ind1, word2, ind2)

    def check_win(self):
        if self.get_sentence()[1] == self.winning_sentence:
            return True
        return False

    def check_lose(self):
        if self.score == 0:
            return True
        return False
