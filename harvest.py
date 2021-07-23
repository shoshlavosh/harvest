############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless 
        self.is_bestseller = is_bestseller
        self.name = name

    # def say_hi(self):
    #     print(self.name)

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    #add musk
    musk = MelonType(
        "musk",
        "Muskmelon",
        1998,
        "green",
        True,
        True
    )
    musk.add_pairing("mint")

    all_melon_types.append(musk)

    #add casaba
    casaba = MelonType("cas", "Casaba", 2003, "orange", True, False)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    all_melon_types.append(casaba)

    #add crenshaw
    crenshaw = MelonType("cren", "Crenshaw", 1996, "green", True, False)
    crenshaw.add_pairing("prosciutto")

    all_melon_types.append(crenshaw)

    #add yellow watermelon
    yellow_watermelon = MelonType("yw", "Yellow Watermelon", 2013, "yellow", True, True)
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # melon is the instance variable. 
    for melon in melon_types:
        print(f"{melon.name} pairs with \n - {melon.pairings}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    #take in the list from all_melon_types
    # key: code
    # values: melon object - make a for loop can goes over the list
    #grab 
    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict

# test = make_melon_type_lookup(make_melon_types())

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    #create __init__ and is_sellable methods


    def __init__(self, melon_type, shape, color, from_field, harvested_by):
        """Melon harvest results"""

        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.from_field = from_field
        self.harvested_by = harvested_by

    def is_sellable(self, shape, color, from_field):
        """Determine if melon is sellable"""

        if shape > 5 and color > 5 and from_field != 3:
            return True


Melon type: yw
Shape rating: 8
Color rating: 7
Harvested from Field 2
Harvested by Sheila
Melon 2

Melon type: yw
Shape rating: 3
Color rating: 4
Harvested from Field 2
Harvested by Sheila
Melon 3

Melon type: yw
Shape rating: 9
Color rating: 8
Harvested from Field 3
Harvested by Sheila
Melon 4

Melon type: cas
Shape rating: 10
Color rating: 6
Harvested from Field 35
Harvested by Sheila
Melon 5

Melon type: cren
Shape rating: 8
Color rating: 9
Harvested from Field 35
Harvested by Michael
Melon 6

Melon type: cren
Shape rating: 8
Color rating: 2
Harvested from Field 35
Harvested by Michael
Melon 7

Melon type: cren
Shape rating: 2
Color rating: 3
Harvested from Field 4
Harvested by Michael
Melon 8

Melon type: musk
Shape rating: 6
Color rating: 7
Harvested from Field 4
Harvested by Michael
Melon 9

Melon type: yw
Shape rating: 7
Color rating: 10
Harvested from Field 3
Harvested by Sheila
    # Needs __init__ and is_sellable methods



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



