from django.apps import AppConfig


class DataviewConfig(AppConfig):
    name = 'dataview'

    def ready(self):
        import dataview.signals
        