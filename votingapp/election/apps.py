from django.apps import AppConfig
from django.db.models import signals


class ElectionConfig(AppConfig):
    name = 'election'

    def ready(self):
        import election.signals
        