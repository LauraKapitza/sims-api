import json

from django.core.management.base import BaseCommand, CommandError

from sims.core.models import Traits


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, *args, **options):
        path = options["path"][0]

        with open(path, "r+") as json_file:
            # Reading from a file
            data = json.load(json_file)
            for trait_obj in data:
                trait, created = Traits.objects.get_or_create(
                    name=trait_obj["name"],
                    category=trait_obj["category"],
                    positivity=trait_obj["positivity"] if "positivity" in trait_obj else 0
                )
                print(trait, created)