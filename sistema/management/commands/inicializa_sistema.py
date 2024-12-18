from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from cadastros.models import Departamento, Perfil

class Command(BaseCommand):
    help = 'Inicializa o sistema com dados padrão'

    def handle(self, *args, **options):
        #cria um departamento
        departamento, created = Departamento.objects.get_or_create(nome='Geral', sigla='Geral')
        if created:
            self.stdout.write(self.style.SUCCESS(f'Departamento criado: {departamento.nome}'))

        #cria um perfil de adm
        perfil_administrador, created = Perfil.objects.get_or_create(id = 1, nome='Administrador')
        if created:
            self.stdout.write(self.style.SUCCESS(f'Perfil criado: {perfil_administrador.nome}'))

        #cria um perfil de estoquista
        perfil_estoquista, created = Perfil.objects.get_or_create(id = 2, nome='Estoquista')
        if created:
            self.stdout.write(self.style.SUCCESS(f'Perfil criado: {perfil_estoquista.nome}'))

        #cria um perfil de vendedor
        perfil_vendedor, created = Perfil.objects.get_or_create(id = 3, nome='Vendedor')
        if created:
            self.stdout.write(self.style.SUCCESS(f'Perfil criado: {perfil_vendedor.nome}'))

        #cria um adm principal
        User = get_user_model()
        if not User.objects.filter(email='adm@gmail.com').exists():
            usuario = User(
                email = 'adm@gmail.com',
                nome = 'Administrador',
                is_admin = True,
                departamento = departamento
            )

            usuario.set_password('123456')
            usuario.save()

            usuario.perfis.add(perfil_administrador)
            usuario.save()

            self.stdout.write(self.style.SUCCESS('Usuario administrador criado'))

        else:
            self.stdout.write(self.style.WARNING('DEU RUIM'))
