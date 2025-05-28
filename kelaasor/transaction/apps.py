from django.apps import AppConfig


class TransactionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transaction'

class WalletAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wallet'

    def ready(self):
        import transaction.signals