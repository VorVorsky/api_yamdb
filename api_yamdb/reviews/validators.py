import re

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username(name):
    """Делает невозможным использовать <<me>> как имя"""
    if name.lower() == 'me':
        raise ValidationError('Нельзя использовать "me" как username')
    if not re.fullmatch(r'^[\w.@+-]+\Z', name):
        raise ValidationError('username может состоять только'
                              ' из букв, цифр и @/./+/-/_')


def validate_score_range(score):
    """Запрещает ставить оценку в отзыве не из промежутка (1, 10)"""
    if score not in range(1, 11):
        raise ValidationError('Оценка должна быть целым числом от 1 до 10!')


def validate_year(value):
    """Проверяет, что год выпуска не больше текущего"""
    if value > timezone.now().year:
        raise ValidationError(
            ('Год выпуска не может быть больше текущего: '
             f'{timezone.now().year}'
             f'Ваш год: {value}'),
        )
