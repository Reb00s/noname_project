
from django.db.models import TextChoices


class Entity(TextChoices):
    """Список сущностей, которые могут использовать аттрибуты"""

    ASSET = 'asset', 'Активы'
    RELATION = 'relation', 'Связи'
    TASK = 'task', 'Задачи'


class AttributeType(TextChoices):
    """Список типов аттрибутов"""

    INTEGER = 'integer', 'Целое число'
    STRING = 'string', 'Строка'
    BOOLEAN = 'boolean', 'Булевый тип'
    LIST = 'list', 'Список'
