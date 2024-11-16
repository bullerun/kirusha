from django.apps import AppConfig


class CoursovayaConfig(AppConfig):
    name = 'coursovaya'

    def ready(self):
        import coursovaya.signals
