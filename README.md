Запуск uWSGI 
``
uwsgi uwsgi.ini
``

Запуск Prometheus 
``
~/prometheus/prometheus --web.console.templates consoles/   --web.console.libraries ~/prometheus/console_libraries/
``

Django  консоль
``
http://localhost:9090/consoles/django.html
``

Для тестирования
``
ab -c 100 -n 1000 http://localhost:8080/
``