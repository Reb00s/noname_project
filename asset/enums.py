from django.db.models import TextChoices


class Direction(TextChoices):
    """Список направлений связи"""

    LEFT_TO_RIGHT = 'left_to_right', 'Слева на право'
    RIGHT_TO_LEFT = 'right_to_left', 'Справа на лево'
    BOTH = 'both', 'В обе стороны'
    NONE = 'none', 'Без направления'


class RelationType(TextChoices):
    """Список типов отношений"""

    APPLIES = 'applies', 'Отностится'
    DEPENDS = 'depends', 'Зависит'
    CONSISTS = 'consists', 'Состоит'
    PARENT = 'parent', 'Родитель'
    SUBSIDIARY = 'subsidiary', 'Дочерний'
    PART = 'part', 'Часть'
