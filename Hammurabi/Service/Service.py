from Repository.Repository import Repository
import random

class Service:
    def __init__(self):
        self.repository = Repository()

    def set_the_data_for_the_next_year(self, planted_acres):
        next_year = self.repository.get_next_year()
        current_year = self.repository.get_current_year()
        next_year.set_population(current_year.get_population() + next_year.get_new_people() - next_year.get_people_starved())
        next_year.set_harvest_units(random.randint(1, 6))
        next_year.set_grain_stocks(current_year.get_grain_stocks() + planted_acres * next_year.get_harvest_units())
        next_year.set_land_price(random.randint(15, 25))
        next_year.set_owned_acres(current_year.get_owned_acres())
        next_year.set_units_lost(self.random_units_lost(next_year.get_grain_stocks()))
        next_year.set_grain_stocks(next_year.get_grain_stocks() - next_year.get_units_lost())
        self.repository.advance_year()


    def get_current_year(self):
        return self.repository.get_current_year()

    # function to set the random harvest units for the next year
    def random_harvest_units(self):
        harvest_units = random.randint(1, 6)
        self.repository.get_next_year().set_harvest_units(harvest_units)

    def buy_sell_land(self, acres):
        current_year = self.repository.get_current_year()
        if acres < 0:
            if acres > current_year.get_owned_acres():
                raise ValueError("You can't sell more acres than you own")
            else:
                current_year.set_owned_acres(current_year.get_owned_acres() + acres)
                current_year.set_grain_stocks(current_year.get_grain_stocks() - acres * current_year.get_land_price())
        else:
            if current_year.get_grain_stocks() < acres * current_year.get_land_price():
                raise ValueError("You can't buy more acres than you have grain for")
            else:
                current_year.set_owned_acres(current_year.get_owned_acres() + acres)
                current_year.set_grain_stocks(current_year.get_grain_stocks() - acres * current_year.get_land_price())

    def feed_the_population(self, units):
        current_year = self.repository.get_current_year()
        next_year = self.repository.get_next_year()
        if units > current_year.get_grain_stocks():
            raise ValueError("You can't feed the population with more grain than you have")
        else:
            current_year.set_grain_stocks(current_year.get_grain_stocks() - units)
            deficit = current_year.get_population()*20 - units
            if deficit > 0:
                next_year.set_people_starved(deficit//20)
            else:
                next_year.set_new_people(self.random_new_people())

    def plant_acres(self, planted_acres):
        current_year = self.repository.get_current_year()
        if planted_acres > current_year.get_owned_acres():
            raise ValueError("You can't plant more acres than you own")
        elif planted_acres > current_year.get_grain_stocks():
            raise ValueError("You can't plant more acres than you have grain for")
        elif planted_acres > current_year.get_population()*10:
            raise ValueError("You can't plant more acres than you have people for")
        else:
            current_year.set_grain_stocks(current_year.get_grain_stocks() - planted_acres)
            self.set_the_data_for_the_next_year(planted_acres)

    def random_new_people(self):
        new_people = random.randint(0, 11)
        return new_people

    def random_units_lost(self, stock):
        chance = random.randint(1, 100)
        if chance <= 20:
            units_lost = random.randint(0, 10) * stock // 100
        else:
            units_lost = 0

        return units_lost

    def check_if_game_over(self):
        current_year = self.repository.get_current_year()
        if current_year.get_year() == 5:
            if current_year.get_population() > 100 and current_year.get_grain_stocks() > 1000:
                print("Congratulations! You won!")
                exit()
            else:
                print("You lost! Womp Womp!")
                exit()
        elif current_year.get_population() <= current_year.get_people_starved():
            print("Too many people died, you lost! Womp Womp!")
            exit()
        else:
            pass
