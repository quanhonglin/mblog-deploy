# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ mysql_name }}',
        'USER': '{{ mysql_user }}',
        'PASSWORD': '{{ mysql_password }}',
        'HOST': '{{ mysql_host }}',
        'PORT': '{{ mysql_port }}',
    }
}

LOGGING_FILE = '{{ app_log_dir_path }}/django.log'
