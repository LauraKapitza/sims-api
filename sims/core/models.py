from random import randrange
import os
import json

from django.db import models


class Aspiration:
    aspirations = []

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.load_list()

    def __repr__(self):
        return repr(self.aspirations)

    def load_list(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, './data/aspirations.json')
        with open(file_path, "r") as f:
            self.aspirations = json.load(f)

    # add pack restriction to condition
    # difficulty "super-easy" should get aspirations with career restriction
    def get_random_aspiration(self):
        filtered_aspirations = []
        for asp in self.aspirations:
            for res in asp["restriction"]:
                if self.difficulty == "moderate":
                    if res["type"] != "career":
                        filtered_aspirations.append(asp)

        random_num = (randrange(len(filtered_aspirations) - 1))
        return filtered_aspirations[random_num]


class Career:
    careers = []

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.load_list()

    def __repr__(self):
        return repr(self.careers)

    def load_list(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, './data/careers.json')
        with open(file_path, "r") as f:
            self.careers = json.load(f)

    # add pack restriction to condition
    # difficulty "moderate" should have best_aspiration restriction for career choice
    def get_random_career(self):
        random_num = randrange(len(self.careers) - 1)
        return self.careers[random_num]


class Sim:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.aspiration = self.get_aspiration()
        self.career = self.get_career()
        self.traits = self.get_traits()
        self.num_children = randrange(7)

    def get_aspiration(self):
        aspiration = Aspiration(self.difficulty)
        return aspiration.get_random_aspiration()

    def get_career(self):
        career = Career(self.difficulty)
        return career.get_random_career()

    def get_traits(self):
        traits = Traits(self.difficulty)
        return traits.get_random_traits()


class Traits:
    traits = []

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.load_list()

    def __repr__(self):
        return repr(self.traits)

    def load_list(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, './data/traits.json')
        with open(file_path, "r") as f:
            self.traits = json.load(f)

    def get_random_traits(self):
        filtered_traits = []
        for tr in self.traits:
            if tr["category"] not in ["Reward", "Bonus", "child-reward", "toddler", "Career"]:
                filtered_traits.append(tr)

        chosen_traits = []
        for _ in range(3):
            random_num = randrange(len(filtered_traits) - 1)
            chosen_trait = filtered_traits[random_num]
            chosen_traits.append(chosen_trait)

        return chosen_traits
