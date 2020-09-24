from django.core.management.base import BaseCommand
from django.db import IntegrityError

from ...models import Material
from ._import_materials import rows_from_csv


class Command(BaseCommand):
    help = 'Import beads data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1)
        parser.add_argument('--dry-run', '-n', action='store_true')

    def handle(self, *args, **options):
        count = 0
        for row in rows_from_csv(options['path'][0]):
            if Material.objects.filter(sku=row.row['sku']['sanitized_value']).count() == 0:
                kwargs = {k: v['sanitized_value'] for k, v in row.row.items()}
                m = Material(**kwargs)
                if options['dry_run']:
                    self.stdout.write(self.style.SUCCESS(f'To be imported {m.name}'))
                else:
                    m.save()
                    self.stdout.write(self.style.SUCCESS(f'Imported {m.name}'))
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} materials'))
