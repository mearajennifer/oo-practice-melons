############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def __repr__(self):
        return f'<MelonType {self.name}>'


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, True, 'Muskmelon')
    muskmelon.add_pairing(["mint"])
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba.add_pairing(["strawberries", "mint"])
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing(["proscuitto"])
    all_melon_types.append(crenshaw)

    y_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    y_watermelon.add_pairing(['ice cream'])
    all_melon_types.append(y_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    r_c_dict = {}

    for melon in melon_types:
        r_c_dict[melon.code] = melon

    return r_c_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field_num,
                 harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_num = field_num
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Returns True or False based on whether the melon is able to be sold
        """

        is_highly_rated = self.shape_rating > 5 and self.color_rating > 5
        is_not_poisoned = self.field_num != 3

        return is_highly_rated and is_not_poisoned


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons = []

    melon_1 = Melon(melon_types['yw'].code, 8, 7, 2, 'Sheila')
    melons.append(melon_1)

    melon_2 = Melon(melon_types['yw'].code, 3, 4, 2, 'Sheila')
    melons.append(melon_2)

    melon_3 = Melon(melon_types['yw'].code, 9, 8, 3, 'Sheila')
    melons.append(melon_3)

    melon_4 = Melon(melon_types['cas'].code, 10, 6, 35, 'Sheila')
    melons.append(melon_4)

    melon_5 = Melon(melon_types['cren'].code, 8, 9, 35, 'Michael')
    melons.append(melon_5)

    melon_6 = Melon(melon_types['cren'].code, 8, 2, 35, 'Michael')
    melons.append(melon_6)

    melon_7 = Melon(melon_types['cren'].code, 2, 3, 4, 'Michael')
    melons.append(melon_7)

    melon_8 = Melon(melon_types['musk'].code, 6, 7, 4, 'Michael')
    melons.append(melon_8)

    melon_9 = Melon(melon_types['yw'].code, 7, 10, 3, 'Sheila')
    melons.append(melon_9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellable = "CAN BE SOLD"
        else:
            sellable = "NOT SELLABLE"
        print(f' Harvested by {melon.harvested_by} from field # {melon.field_num} {sellable}.')


x = make_melon_types()
y = make_melon_type_lookup(x)
z = make_melons(y)
get_sellability_report(z)
