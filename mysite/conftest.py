import sys
import os
import django

# Adicionar o caminho absoluto do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Adicionar o caminho absoluto do diretório mysite ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'mysite')))

# Definir a variável de ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Configurar o Django
django.setup()
