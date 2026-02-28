# def lookup(dictionary):
#     def decorator(func):
#         def wrapper(search_term, auto_print=False):
#             def single_lookup(term):
#                 str_term = str(term).lower()
#                 adjusted = {str(k).lower(): str(v).lower() for k, v in dictionary.items()}
#
#                 if str_term in adjusted:
#                     return dictionary[int(term)] if isinstance(term, int) else dictionary[term]
#                 elif str_term in adjusted.values():
#                     return [key for key, value in dictionary.items() if value.lower() == str_term][0]
#                 else:
#                     return f"Invalid ID or Name: {term}"
#
#             result = [single_lookup(term) for term in search_term] if isinstance(search_term, list) else single_lookup(
#                 search_term)
#
#             if auto_print:
#                 print(result)
#             else:
#                 return result
#
#         return wrapper
#
#     return decorator
"""Refactoring of RioStatConverter to a class. The lookup class allows for bidirectional conversion
(argument of 0 returns Mario; argument of "Mario" returns 0)."""
# should try to standardize the string version of these names if possible to match with dataframe(s)

# DO NOT IMPORT PANDAS HERE. WILL CAUSE OBS SCRIPTS TO FAIL
import pandas as pd

CAPTAINS = [
    'Mario',
    'Luigi',
    'DK',
    'Diddy',
    'Peach',
    'Daisy',
    'Yoshi',
    'Bowser',
    'Wario',
    'Waluigi',
    'Birdo',
    'Bowser Jr'
]

class LookupDicts():
    CHAR_NAME = {
        0: "Mario",
        1: "Luigi",
        2: "DK",
        3: "Diddy",
        4: "Peach",
        5: "Daisy",
        6: "Yoshi",
        7: "Baby Mario",
        8: "Baby Luigi",
        9: "Bowser",
        10: "Wario",
        11: "Waluigi",
        12: "Koopa(G)",
        13: "Toad(R)",
        14: "Boo",
        15: "Toadette",
        16: "Shy Guy(R)",
        17: "Birdo",
        18: "Monty",
        19: "Bowser Jr",
        20: "Paratroopa(R)",
        21: "Pianta(B)",
        22: "Pianta(R)",
        23: "Pianta(Y)",
        24: "Noki(B)",
        25: "Noki(R)",
        26: "Noki(G)",
        27: "Bro(H)",
        28: "Toadsworth",
        29: "Toad(B)",
        30: "Toad(Y)",
        31: "Toad(G)",
        32: "Toad(P)",
        33: "Magikoopa(B)",
        34: "Magikoopa(R)",
        35: "Magikoopa(G)",
        36: "Magikoopa(Y)",
        37: "King Boo",
        38: "Petey",
        39: "Dixie",
        40: "Goomba",
        41: "Paragoomba",
        42: "Koopa(R)",
        43: "Paratroopa(G)",
        44: "Shy Guy(B)",
        45: "Shy Guy(Y)",
        46: "Shy Guy(G)",
        47: "Shy Guy(Bk)",
        48: "Dry Bones(Gy)",
        49: "Dry Bones(G)",
        50: "Dry Bones(R)",
        51: "Dry Bones(B)",
        52: "Bro(F)",
        53: "Bro(B)",
    }

    CHAR_NAME_NO_VARIANT = {
        0: "Mario",
        1: "Luigi",
        2: "DK",
        3: "Diddy",
        4: "Peach",
        5: "Daisy",
        6: "Yoshi",
        7: "Baby Mario",
        8: "Baby Luigi",
        9: "Bowser",
        10: "Wario",
        11: "Waluigi",
        12: "Koopa",
        13: "Toad",
        14: "Boo",
        15: "Toadette",
        16: "Shy Guy",
        17: "Birdo",
        18: "Monty",
        19: "Bowser Jr",
        20: "Paratroopa",
        21: "Pianta",
        22: "Pianta",
        23: "Pianta",
        24: "Noki",
        25: "Noki",
        26: "Noki",
        27: "Bro",
        28: "Toadsworth",
        29: "Toad",
        30: "Toad",
        31: "Toad",
        32: "Toad",
        33: "Magikoopa",
        34: "Magikoopa",
        35: "Magikoopa",
        36: "Magikoopa",
        37: "King Boo",
        38: "Petey",
        39: "Dixie",
        40: "Goomba",
        41: "Paragoomba",
        42: "Koopa",
        43: "Paratroopa",
        44: "Shy Guy",
        45: "Shy Guy",
        46: "Shy Guy",
        47: "Shy Guy",
        48: "Dry Bones",
        49: "Dry Bones",
        50: "Dry Bones",
        51: "Dry Bones",
        52: "Bro",
        53: "Bro",
    }

    TEAM_NAME = {
        0: "Mario Sunshines",
        1: "Mario All Stars",
        2: "Mario Heroes",
        3: "Mario Fireballs",
        4: "Luigi Mansioneers",
        5: "Luigi Leapers",
        6: "Luigi Gentlemen",
        7: "Luigi Vacuums",
        8: "Peach Monarchs",
        9: "Peach Princesses",
        10: "Peach Roses",
        11: "Peach Dynasties",
        12: "Daisy Queen Bees",
        13: "Daisy Petals",
        14: "Daisy Lillies",
        15: "Daisy Cupids",
        16: "Yoshi Islanders",
        17: "Yoshi Flutters",
        18: "Yoshi Eggs",
        19: "Yoshi Speed Stars",
        20: "Birdo Bows",
        21: "Birdo Fans",
        22: "Birdo Beauties",
        23: "Birdo Models",
        24: "Wario Greats",
        25: "Wario Beasts",
        26: "Wario Garlics",
        27: "Wario Steakheads",
        28: "Waluigi Flankers",
        29: "Waluigi Mashers",
        30: "Waluigi Mystiques",
        31: "Waluigi Smart Alecks",
        32: "DK Kongs",
        33: "DK Animals",
        34: "DK Explorers",
        35: "DK Wild Ones",
        36: "Diddy Tails",
        37: "Diddy Red Caps",
        38: "Diddy Survivors",
        39: "Diddy Ninjas",
        40: "Bowser Monsters",
        41: "Bowser Black Stars",
        42: "Bowser Flames",
        43: "Bowser Blue Shells",
        44: "Jr Pixies",
        45: "Jr Rookies",
        46: "Jr Fangs",
        47: "Jr Bombers"
    }

    STADIUM = {
        0: "Mario Stadium",
        1: "Bowser Castle",
        2: "Wario Palace",
        3: "Yoshi Park",
        4: "Peach Garden",
        5: "DK Jungle",
        6: "Toy Field"
    }

    CONTACT_TYPE = {
        255: "Miss",
        0: "Sour - Left",
        1: "Nice - Left",
        2: "Perfect",
        3: "Nice - Right",
        4: "Sour - Right"
    }

    HAND = {
        0: "Left",
        1: "Right"
    }

    HAND_BOOL = {
        True: "Left",
        False: "Right"
    }

    INPUT_DIRECTION = {
        0: "",
        1: "Left",
        2: "Right",
        3: "Left+Right",
        4: "Down",
        5: "Left+Down",
        6: "Right+Down",
        7: "Left+Right+Down",
        8: "Up",
        9: "Left+Up",
        10: "Right+Up",
        11: "Left+Right+Up",
        13: "Left+Down+Up",
        14: "Right+Down+Up",
        15: "Left+Right+Down+Up"
    }

    PITCH_TYPE = {
        0: "Curve",
        1: "Charge",
        2: "ChangeUp"
    }

    CHARGE_TYPE = {
        0: "N/A",
        2: "Slider",
        3: "Perfect"
    }

    TYPE_OF_SWING = {
        0: "None",
        1: "Slap",
        2: "Charge",
        3: "Star",
        4: "Bunt"
    }

    POSITION = {
        0: "P",
        1: "C",
        2: "1B",
        3: "2B",
        4: "3B",
        5: "SS",
        6: "LF",
        7: "CF",
        8: "RF",
        255: "Inv",
        None: "None"
    }

    FIELDER_ACTIONS = {
        0: "None",
        2: "Sliding",
        3: "Walljump",
    }

    FIELDER_BOBBLES = {
        0: "None",
        1: "Slide/stun lock",
        2: "Fumble",
        3: "Bobble",
        4: "Fireball",
        16: "Garlic knockout",
        255: "None"
    }

    STEAL_TYPE = {
        0: "None",
        1: "Ready",
        2: "Normal",
        3: "Perfect",
        55: "None"
    }

    OUT_TYPE = {
        0: "None",
        1: "Caught",
        2: "Force",
        3: "Tag",
        4: "Force Back",
        16: "Strike-out",
    }

    PITCH_RESULT = {
        0: "HBP",
        1: "BB",
        2: "Ball",
        3: "Strike-looking",
        4: "Strike-swing",
        5: "Strike-bunting",
        6: "Contact",
        7: "Unknown"
    }

    PRIMARY_CONTACT_RESULT = {
        0: "Out",
        1: "Foul",
        2: "Fair",
        3: "Fielded",
        4: "Unknown"
    }

    SECONDARY_CONTACT_RESULT = {
        0: "Out-caught",
        1: "Out-force",
        2: "Out-tag",
        3: "foul",
        7: "Single",
        8: "Double",
        9: "Triple",
        10: "HR",
        11: "Error - Input",
        12: "Error - Chem",
        13: "Bunt",
        14: "SacFly",
        15: "Ground ball double Play",
        16: "Foul catch",
    }

    FINAL_RESULT = {
        0: "None",
        1: "Strikeout",
        2: "Walk (BB)",
        3: "Walk (HBP)",
        4: "Out",
        5: "Caught",
        6: "Caught line-drive",
        7: "Single",
        8: "Double",
        9: "Triple",
        10: "HR",
        11: "Error - Input",
        12: "Error - Chem",
        13: "Bunt",
        14: "SacFly",
        15: "Ground ball double Play",
        16: "Foul catch"
    }

    MANUAL_SELECT = {
        0: "No Selected Char",
        1: "Selected Other Char",
        2: "Selected This Char",
        None: "None"
    }

# todo - more complete error handling

class Lookup:
    def __init__(self):
        pass

    def _lookup(self, dictionary: dict, search_term):
        def single_lookup(term):
            original_term = term
            if isinstance(term, str) and term.isdigit():
                term = int(term)
            if isinstance(term, float) and term.is_integer():
                term = int(term)

            str_term = str(term).lower()
            adjusted_dict = {str(k).lower(): str(v).lower() for k, v in dictionary.items()}

            if str_term in adjusted_dict:
                return dictionary.get(term, f"Invalid ID or Name: {original_term}")
            elif str_term in adjusted_dict.values():
                return [key for key, value in dictionary.items() if value.lower() == str_term][0]
            else:
                return f"Invalid ID or Name: {original_term}"

        if isinstance(search_term, pd.Series):
            return search_term.apply(single_lookup)
        elif isinstance(search_term, pd.DataFrame):
            return search_term.applymap(single_lookup)
        elif isinstance(search_term, list):
            return [single_lookup(term) for term in search_term]
        else:
            return single_lookup(search_term)

    def lookup(self, dictionary: dict, search_term, auto_print: bool = False):
        result = self._lookup(dictionary, search_term)
        if auto_print:
            print(result)
        return result

    def translate_values(self, dictionary: dict, values):
        return self._lookup(dictionary, values)

    def create_translated_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        column_to_dict_map = {
            'batter_char_id': LookupDicts.CHAR_NAME,
            'pitcher_char_id': LookupDicts.CHAR_NAME,
            'fielder_char_id': LookupDicts.CHAR_NAME,
            'batting_hand': LookupDicts.HAND_BOOL,
            'fielder_jump': LookupDicts.FIELDER_ACTIONS,
            'fielder_position': LookupDicts.POSITION,
            'fielding_hand': LookupDicts.HAND_BOOL,
            'final_result': LookupDicts.FINAL_RESULT,
            'manual_select_state': LookupDicts.MANUAL_SELECT,
            'stick_input': LookupDicts.INPUT_DIRECTION,
            'type_of_contact': LookupDicts.CONTACT_TYPE,
            'type_of_swing': LookupDicts.TYPE_OF_SWING,
            'stadium': LookupDicts.STADIUM
        }

        for column, dict_name in column_to_dict_map.items():
            if column in df.columns:
                translated_values = self.lookup(dict_name, df[column])
                df[f'{column}_str'] = translated_values.astype('category')

        return df
    
    def get_character(self, search_term: str | int, output_format: str = "name"):
    
        # Look up a character and return their info in the specified format.

        # Args:
        #     search_term:   Character name (str) or ID (int)
        #     output_format: One of "name", "nameNoVariant", "ID", "IDHex"

        # Returns:
        #     Character info in the requested format.
        
        # First, resolve to the "other side" if needed
        # _lookup returns name if given ID, and ID if given name
        result = self._lookup(LookupDicts.CHAR_NAME, search_term)

        # Determine name and ID from the lookup result + original input
        if isinstance(result, int):  # input was a name, result is ID
            character_id = result
            character_name = search_term
        else:  # input was an ID, result is name
            character_name = result
            character_id = self._lookup(LookupDicts.CHAR_NAME, result)

        match output_format:
            case "name":
                return character_name
            case "nameNoVariant":
                parts = character_name.split()
                return self._lookup(LookupDicts.CHAR_NAME_NO_VARIANT, character_id)
            case "ID":
                return character_id
            case "IDHex":
                return hex(character_id)
            case _:
                raise ValueError(f"Invalid output_format '{output_format}'. Choose from: 'name', 'nameNoVariant', 'ID', 'IDHex'")

# lookup_instance = Lookup()

# sample usage
"""
print(lookup_instance.lookup(LookupDicts.CHAR_NAME, 'mario'))
"""