# images/management/commands/createsu.py

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='complexpassword123'
                username = 'sony.mathew.thomas'
                first_name = 'Sony''
                last_name = 'Thomas''
                phone_number = '+966555682150''
                email = 'sony.mathew.thomas@gmail.com'
                password = 'Sony@80170174'
                

            )
        print('Superuser has been created.')
