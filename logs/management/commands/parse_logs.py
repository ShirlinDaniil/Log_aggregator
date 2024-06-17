import os
import re
from datetime import datetime
from django.core.management.base import BaseCommand
from logs.models import LogEntry

LOG_PATTERN = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>.*?)\] "(?P<request>.*?)" (?P<status>\d{3}) (?P<size>\S+)')

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        data = match.groupdict()
        data['timestamp'] = datetime.strptime(data['timestamp'], '%d/%b/%Y:%H:%M:%S %z')
        data['size'] = int(data['size']) if data['size'] != '-' else 0
        return data
    return None

class Command(BaseCommand):
    help = 'Parse Apache logs and save to the database'

    def handle(self, *args, **kwargs):
        log_dir = '/PycharmProjects/Log_aggregator'
        for filename in os.listdir(log_dir):
            if filename.endswith('log'):
                filepath = os.path.join(log_dir, filename)
                with open(filepath) as f:
                    for line in f:
                        data = parse_log_line(line)
                        if data:
                            log_entry = LogEntry(**data)
                            log_entry.save()
        self.stdout.write(self.style.SUCCESS('Successfully parsed logs'))
