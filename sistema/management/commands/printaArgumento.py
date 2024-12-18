from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Inicializa o sistema com dados padrão'

    def add_arguments(self, parser):
        parser.add_argument('argumento', type=str, help='Nome do argumento a ser criado')

    def handle(self, *args, **options):
        argumento = options['argumento']
        self.stdout.write(self.style.SUCCESS(f'o argumento digitado foi: {argumento}'))