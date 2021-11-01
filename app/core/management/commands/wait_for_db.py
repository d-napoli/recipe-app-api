import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        ts = 1
        wait_msg = 'Waiting for database...'
        self.stdout.write(wait_msg)
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                op_err_msg = f"Database unavailable, waiting {ts} second..."
                self.stdout.write(op_err_msg)
                time.sleep(ts)

        self.stdout.write(self.style.SUCCESS('Database available!'))
