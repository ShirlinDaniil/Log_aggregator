from django.db import models

class LogEntry(models.Model):
    ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField()
    request = models.TextField()
    status = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return f"{self.ip} - {self.timestamp}"
