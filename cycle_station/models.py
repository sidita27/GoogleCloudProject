from django.db import models

class Station(models.Model):
    name = models.TextField()
    bikes_count = models.IntegerField()
    terminal_id = models.IntegerField()
    class Meta:
        db_table = "cycle_station"
        