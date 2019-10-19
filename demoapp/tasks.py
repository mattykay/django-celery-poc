# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import subprocess

from logging import log

@shared_task
def perform_os_command(*args):
    return subprocess.check_output(args)
