from django.core.management.base import BaseCommand

from ._load_data_funcs import (load_users, load_genres,
                               load_categories, load_title,
                               load_genre_title, load_comments,
                               load_reviews, rating_update)


class Command(BaseCommand):
    """Создает комманду для django,
    предназначенную для выгрузки данных из csv файлов
    в папке /static/data/.
    Для запуска - python manage.py load_data.
    Собственно рабочий код находится в файле _load_data_funcs.py.
    В планах оптимизировать работу функций, т.к. много повторяющегося кода.
    """

    help = ('Загружает данные из csv файлов в',
            '"/static/data/" в соответствующие модели')

    def handle(self, *args, **options):
        try:
            load_users()
            load_genres()
            load_categories()
            load_title()
            load_genre_title()
            load_reviews()
            load_comments()
            rating_update()
        except Exception as error:
            print(error)
