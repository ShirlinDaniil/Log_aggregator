from rest_framework import viewsets
from .models import LogEntry
from .serializers import LogEntrySerializer

class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

    def get_queryset(self):
        queryset = LogEntry.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        ip = self.request.query_params.get('ip')
        if start_date and end_date:
            queryset = queryset.filter(timestamp__range=[start_date, end_date])
        if ip:
            queryset = queryset.filter(ip=ip)
        return queryset
