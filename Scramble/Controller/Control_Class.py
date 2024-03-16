from Repository.Repo_Class import Repo


class Controller:
    def __init__(self):
        self.repo = Repo()

    def controller_get_sentence(self):
        return self.repo.get_sentence()

    def controller_scramble_letters(self):
        self.repo.scramble_letters()

    def controller_swap_letters(self, word1, ind1, word2, ind2):
        self.repo.swap_letters(word1, ind1, word2, ind2)

    def controller_update_score(self):
        self.repo.update_score()

    def controller_check_win(self):
        return self.repo.check_win()

    def controller_check_lose(self):
        return self.repo.check_lose()