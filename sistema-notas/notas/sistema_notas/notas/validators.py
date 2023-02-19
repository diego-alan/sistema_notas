from django.core.exceptions import ValidationError


def validar_maximo(value):
    if value <= 100:
        raise ValidationError(
            '%(value)s la nota debe estar contemplada de 1 al 100',
            params={'value': value}
        )
