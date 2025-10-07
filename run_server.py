# run_server.py
import os
import sys
from django.core.management import execute_from_command_line 

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django import setup # type: ignore
        setup()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed."
        ) from exc
    # اجرا روی آی‌پی شبکه، پورت 8000
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
