from random import randrange
import os
import json

from django.db import models
from django.utils.text import slugify


class Aspiration(models.Model):
    name = models.CharField(max_length=250)
    #reward_trait = models.CharField(max_length=250)
    #bonus_trait = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    #pack: "Cats & Dogs",
    #restriction: []


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


class Traits(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, blank=True, null=True)
    category = models.CharField(max_length=250)
    #aspiration: []
    #pack: null
    #conflict: ["lazy"]
    positivity = models.IntegerField(default=0)

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super().save(**kwargs)

