from django.db import models
from attribute.models import EntityType
from asset.enums import Direction, RelationType



class AssetTemplate(models.Model):
    """Класс описывающий шаблоны активов"""
    type = models.ForeignKey(EntityType, verbose_name='Тип актива', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование шаблона актива', max_length=256, blank=False)
    description = models.CharField(verbose_name='Описание шаблона актива', max_length=512, blank=True)


class Asset(models.Model):
    """Класс описывающий активы"""
    type = models.ForeignKey(EntityType, verbose_name='Тип актива', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование актива', max_length=256, blank=False)
    note = models.CharField(verbose_name='Описание актива', max_length=512, blank=True)


class RelationTemplate(models.Model):
    """Класс описывающий шаблоны связей между активами"""
    type = models.ForeignKey(EntityType, verbose_name='Тип актива', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование шаблона связи', max_length=256, blank=False)
    relation_type = models.CharField(verbose_name='Тип связи', max_length=50, choices=RelationType, blank=False)
    description = models.CharField(verbose_name='Описание шаблона связи', max_length=512, blank=True)
    direction = models.CharField(verbose_name='Направление связи', max_length=50, choices=Direction, default=Direction.NONE)
    required = models.BooleanField(verbose_name='Обязательный для ввода', default=False)


class Relation(models.Model):
    """Класс описывающий связи между активами"""
    type = models.ForeignKey(EntityType, verbose_name='Тип актива', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование связи', max_length=256, blank=False)
    relation_type = models.CharField(verbose_name='Тип связи', max_length=50, choices=RelationType, blank=False)
    left = models.ForeignKey(Asset, verbose_name='Левый актив', on_delete=models.CASCADE, related_name='left_asset')
    right = models.ForeignKey(Asset, verbose_name='Правый актив', on_delete=models.CASCADE, related_name='right_asset')
    note = models.CharField(verbose_name='Описание связи', max_length=512, blank=True)
    direction = models.CharField(verbose_name='Направление связи', max_length=50, choices=Direction, blank=False)
    required = models.BooleanField(verbose_name='Обязательный для ввода', default=False)
