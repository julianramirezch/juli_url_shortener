from django.core.management.base import BaseCommand, CommandError
from shortener.models import JuliURL


class Command(BaseCommand):
    """ Class Command """ 
    help = 'Refresh all shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        """ Create new command """
        return JuliURL.objects.refresh_shortcodes(items=options['items'])
