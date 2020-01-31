from rpg_namer.word_lists import *
from random import choice


class RPGItems(object):
    def __init__(self, item_set="all", items="", adjectives="", nouns=""):
        self.item_list = self.__setup_item_list(item_set)
        self.adjectives = list(adjective_list)
        self.nouns = list(creature_list)

        if items:
            self.item_list = items
        if adjectives:
            self.adjectives = adjectives
        if nouns:
            self.nouns = nouns

    @staticmethod
    def __setup_item_list(selector):
        if selector == "all":
            return list(helmet_list +
                        body_list +
                        leg_list +
                        boot_list +
                        shield_list +
                        gauntlet_list)
        elif selector == "helmet":
            return list(helmet_list)
        elif selector == "body":
            return list(body_list)
        elif selector == "legs":
            return list(leg_list)
        elif selector == "boots":
            return list(boot_list)
        elif selector == "shield":
            return list(shield_list)
        elif selector == "gauntlets":
            return list(gauntlet_list)
        else:
            raise ValueError("Incorrect value for keyword item_list, accepted keywords: "
                             "[all, helmet, body, legs, boots, shield, gauntlets]")

    @staticmethod
    def __create_item_string(adj, item, noun):
        formats = [
            f"{adj} {item} of the {noun}",
            f"{adj} {item}",
            f"The {adj} {item}",
            f"{noun}'s {item}",
            f"{item} of the {noun}",
            f"{item} of the {adj} {noun}"
        ]
        return choice(formats).replace('\n', '')

    def random_item(self):
        adj = choice(self.adjectives).capitalize()
        item = choice(self.item_list).title()
        creature = choice(self.nouns).title()
        final_item = self.__create_item_string(adj, item, creature)
        return final_item
