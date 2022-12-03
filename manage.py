#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from threading import Thread

def run_command():
    cmd = ''
    with open('rabbit_mq/pre_run_commands.txt', 'r') as f:
        cmd = f.readline()
    cmd = f"cd rabbit_mq & {cmd}"
    os.system(cmd)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    thead_main = Thread(target=run_command)
    thead_main.start()
    main()
