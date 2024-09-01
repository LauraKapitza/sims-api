from random import randrange
import os
import json

from django.db import models
from django.utils.text import slugify


class SimsApiModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super().save(**kwargs)

    def __str__(self):
        return f"{self.__class__.__name__},{self.id}; name: {self.name}; slug: {self.slug}"


class Aspiration(SimsApiModel):
    reward_trait = models.ForeignKey("Trait", null=True, on_delete=models.CASCADE, related_name="reward_trait_set")
    bonus_trait = models.ForeignKey("Trait", null=True, on_delete=models.CASCADE, related_name="bonus_trait_set")
    category = models.CharField(max_length=250)
    # pack: "Cats & Dogs",
    # restriction: []


# class Sim:
#     def __init__(self, difficulty):
#         self.difficulty = difficulty
#         self.aspiration = self.get_aspiration()
#         self.career = self.get_career()
#         self.traits = self.get_traits()
#         self.num_children = randrange(7)
#
#     def get_aspiration(self):
#         aspiration = Aspiration(self.difficulty)
#         return aspiration.get_random_aspiration()
#
#     def get_career(self):
#         career = Career(self.difficulty)
#         return career.get_random_career()
#
#     def get_traits(self):
#         traits = Trait(self.difficulty)
#         return traits.get_random_traits()


class Trait(SimsApiModel):
    category = models.CharField(max_length=250)
    # aspiration: []
    # pack: null
    # conflict: ["lazy"]
    positivity = models.IntegerField(default=0)


class Career(SimsApiModel):
    best_aspirations = models.ManyToManyField(Aspiration)
    best_traits = models.ManyToManyField(Trait)


class CareerBranch(SimsApiModel):
    career = models.ForeignKey("Career", on_delete=models.CASCADE)
