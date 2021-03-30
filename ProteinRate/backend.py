import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProteinRate.settings')
django.setup()
from protein.models import *
print(ProteinShake.objects.all())