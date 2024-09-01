import json

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from sims.core.models import Trait, Aspiration, Career, CareerBranch


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        traits_file_path = "C:\\Users\\PinkMarshmallow\\PycharmProjects\\sims_api\\sims\\seeds\\initial_traits.json"
        aspiration_file_path = "C:\\Users\\PinkMarshmallow\\PycharmProjects\\sims_api\\sims\\seeds\\initial_aspirations.json"
        career_file_path = "C:\\Users\\PinkMarshmallow\\PycharmProjects\\sims_api\\sims\\seeds\\initial_careers.json"

        with open(traits_file_path, "r+") as json_file:
            data = json.load(json_file)
            for trait_obj in data:
                trait, created = Trait.objects.get_or_create(
                    name=trait_obj["name"],
                    category=trait_obj["category"],
                    positivity=trait_obj["positivity"] if "positivity" in trait_obj else 0
                )
                print(trait, created)

        with open(aspiration_file_path, "r+") as json_file:
            data = json.load(json_file)
            for aspiration_obj in data:
                try:
                    reward_trait = Trait.objects.get(slug=slugify(aspiration_obj["reward_trait"]))
                except Trait.DoesNotExist:
                    print(f"Reward trait does not exist: {aspiration_obj['name']}, {aspiration_obj['reward_trait']}")
                    continue
                except KeyError:
                    continue

                try:
                    bonus_trait = Trait.objects.get(slug=slugify(aspiration_obj["bonus_trait"]))
                except Trait.DoesNotExist:
                    print(f"Bonus trait does not exist: {aspiration_obj['name']}, {aspiration_obj['bonus_trait']}")
                    continue
                except KeyError:
                    continue

                aspiration, created = Aspiration.objects.get_or_create(
                    name=aspiration_obj["name"],
                    category=aspiration_obj["category"],
                )
                if reward_trait:
                    aspiration.reward_trait = reward_trait

                if bonus_trait:
                    aspiration.bonus_trait = bonus_trait

                aspiration.save()

        with open(career_file_path, "r+") as json_file:
            data = json.load(json_file)
            for career_obj in data:
                career, created = Career.objects.get_or_create(
                    name=career_obj["name"],
                )
                print(career, created)

                for branch_obj in career_obj["branches"]:
                    branch, created = CareerBranch.objects.get_or_create(
                        name=branch_obj["name"],
                        career=career,
                    )
                    print(branch, created)

                for best_trait_obj in career_obj["best_traits"]:
                    try:
                        best_trait = Trait.objects.get(slug=slugify(best_trait_obj["name"]))
                    except Trait.DoesNotExist:
                        print(f"Best trait does not exist: {best_trait_obj['name']}")
                        continue
                    except KeyError:
                        continue

                    career.best_traits.add(best_trait)

                for best_aspiration_obj in career_obj["best_aspirations"]:
                    try:
                        best_aspiration = Aspiration.objects.get(slug=slugify(best_aspiration_obj["name"]))
                    except Aspiration.DoesNotExist:
                        print(f"Best aspiration does not exist: {best_aspiration_obj['name']}")
                        continue
                    except KeyError:
                        continue

                    career.best_aspirations.add(best_aspiration)
