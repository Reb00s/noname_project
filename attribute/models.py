from django.db import models
from attribute.enums import AttributeType, Entity


class EntityType(models.Model):
    """Класс описывающий типы активов"""
    entity = models.CharField(verbose_name='Тип сущности', max_length=50, choices=Entity, blank=False)
    name = models.CharField(verbose_name='Наименование типа актива', max_length=256, blank=False)
    description = models.CharField(verbose_name='Описание типа актива', max_length=512, blank=True)


class DictionaryAttribute(models.Model):
    """Класс описывающий шаблоны аттрибутов"""
    type = models.ForeignKey(EntityType, verbose_name='Тип актива', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование шаблона аттрибута', max_length=256, blank=False)
    attribute_type = models.CharField(verbose_name='Тип аттрибута', max_length=50, choices=AttributeType, blank=False)
    is_dictionary = models.BooleanField(verbose_name='Словарь', default=False)
    description = models.CharField(verbose_name='Описание шаблона аттрибута', max_length=512, blank=True)
    required = models.BooleanField(verbose_name='Обязательный для ввода', default=False)


class DictionaryAttributeValue(models.Model):
    attribute_template = models.ForeignKey(DictionaryAttribute, verbose_name='Шаблон аттрибута', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование значения', max_length=256, blank=False)
    description = models.CharField(verbose_name='Описание значения', max_length=512, blank=True)


class Attribute(models.Model):
    """Класс описывающий аттрибуты для активов"""
    type = models.ForeignKey(EntityType, verbose_name='Тип актива', on_delete=models.CASCADE)
    entity_id = models.IntegerField(verbose_name='Идентификатор актива', blank=False)
    name = models.CharField(verbose_name='Наименование аттрибута', max_length=256, blank=False)
    attribute_type = models.CharField(verbose_name='Тип аттрибута', max_length=50, choices=AttributeType, blank=False)
    value = models.BinaryField(verbose_name='Значение аттрибута', blank=True, null=True)
    note = models.CharField(verbose_name='Комментарий аттрибута', max_length=512, blank=True)
    required = models.BooleanField(verbose_name='Обязательный для ввода', blank=False)
