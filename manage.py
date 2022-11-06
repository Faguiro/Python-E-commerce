#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
           "Não foi possível importar o Django. Tem certeza de que está instalado e "
            "disponível em sua variável de ambiente PYTHONPATH? Você "
            "esquecer de ativar um ambiente virtual?"
        ) from exc
    execute_from_command_line(sys.argv)
