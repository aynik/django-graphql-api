application = None

if __name__ == "__main__":
    import os
    import sys

    from django.core.management import execute_from_command_line

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
    execute_from_command_line(sys.argv)
else:
    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()
