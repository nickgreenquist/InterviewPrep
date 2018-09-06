
class Person:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death

def max_alive(people, start_year, end_year):
    births = {}
    deaths = {}
    for person in people:
        birth = person.birth
        death = person.death 

        if birth in births:
            births[birth] += 1
        else:
            births[birth] = 1

        if death in deaths:
            deaths[death] += 1
        else:
            deaths[death] = 1
    
    population = 0
    max_pop = float('-inf')
    max_year = None
    for year in range(start_year, end_year + 1):
        if year in births:
            population += births[year]
        
        if population > max_pop:
            max_pop = population
            max_year = year
        
        if year in deaths:
            population -= deaths[year]
    
    return max_year

people = [Person(1800, 1901), Person(1901, 1945), Person(1960, 2000)]
print(max_alive(people, 1800, 2000))