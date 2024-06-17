import pytz
from datetime import datetime
from django.core.management import BaseCommand
from logs.models import LogEntry

class Command(BaseCommand):
    help = 'View logs based on filters'

    def add_arguments(self, parser):
        parser.add_argument('start_date', type=str, help='Start date in YYYY-MM-DD format')
        parser.add_argument('end_date', type=str, help='End date in YYYY-MM-DD format', nargs='?', default=None)
        parser.add_argument('filter', type=str, help='Filter by ip or status', nargs='?', default=None)

    def handle(self, *args, **kwargs):
        start_date_str = kwargs['start_date']
        end_date_str = kwargs.get('end_date')
        filter_type = kwargs.get('filter')

        # Преобразование строк в объекты datetime с учетом часового пояса
        timezone = pytz.timezone('UTC')  # Выберите нужный часовой пояс
        start_date = timezone.localize(datetime.strptime(start_date_str, '%Y-%m-%d'))
        if end_date_str:
            end_date = timezone.localize(datetime.strptime(end_date_str, '%Y-%m-%d'))
        else:
            end_date = None

        query = LogEntry.objects.filter(timestamp__gte=start_date)
        if end_date:
            query = query.filter(timestamp__lte=end_date)
        if filter_type == 'ip':
            query = query.values('ip').distinct()
        elif filter_type == 'status':
            query = query.values('status').distinct()

        for log in query:
            self.stdout.write(str(log))
