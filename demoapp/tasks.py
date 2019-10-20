# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import subprocess

from logging import log


@shared_task
def perform_os_command(*args):
    process = subprocess.Popen(args,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    output, errors = process.communicate()
    return {"result": output, "errors": errors}
