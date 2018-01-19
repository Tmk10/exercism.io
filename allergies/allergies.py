class Allergies(object):
    allergens = {'eggs': 1,
                 'peanuts': 2,
                 'shellfish': 4,
                 'strawberries': 8,
                 'tomatoes': 16,
                 'chocolate': 32,
                 'pollen': 64,
                 'cats': 128}

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return Allergies.allergens.get(item) & self.score > 0

    @property
    def lst(self):
        return [key for key in Allergies.allergens.keys() if Allergies.allergens.get(key) & self.score > 0]


a = Allergies(254)
print(a.lst)

