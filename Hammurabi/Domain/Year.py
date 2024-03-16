class Year:

    def __init__(self, year=1, new_people=0, people_starved=0, population=100, owned_acres=1000, harvest_units=3,
                 units_lost=200, land_price=20, grain_stocks=2800):
        self._year = year
        self._new_people = new_people
        self._people_starved = people_starved
        self._population = population
        self._owned_acres = owned_acres
        self._harvest_units = harvest_units
        self._units_lost = units_lost
        self._land_price = land_price
        self._grain_stocks = grain_stocks

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_new_people(self):
        return self._new_people

    def set_new_people(self, new_people):
        self._new_people = new_people

    def get_people_starved(self):
        return self._people_starved

    def set_people_starved(self, people_starved):
        self._people_starved = people_starved

    def get_population(self):
        return self._population

    def set_population(self, population):
        self._population = population

    def get_owned_acres(self):
        return self._owned_acres

    def set_owned_acres(self, owned_acres):
        self._owned_acres = owned_acres

    def get_harvest_units(self):
        return self._harvest_units

    def set_harvest_units(self, harvest_units):
        self._harvest_units = harvest_units

    def get_units_lost(self):
        return self._units_lost

    def set_units_lost(self, units_lost):
        self._units_lost = units_lost

    def get_land_price(self):
        return self._land_price

    def set_land_price(self, land_price):
        self._land_price = land_price

    def get_grain_stocks(self):
        return self._grain_stocks

    def set_grain_stocks(self, grain_stocks):
        self._grain_stocks = grain_stocks

    def to_string(self):
        return (f'In year {self._year}, {self._people_starved} people starved, {self._new_people} came to the city. \n'
                f'City population is {self._population}. \n'
                f'City owns {self._owned_acres} acres of land. \n'
                f'Harvest was {self._harvest_units} units per acre. \n'
                f'Rats ate {self._units_lost} units. \n'
                f'Land price is {self._land_price} units per acre. \n'
                f'Grain stocks are {self._grain_stocks} units. \n')