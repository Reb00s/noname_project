from django.contrib import admin
from attribute.models import DictionaryAttribute, DictionaryAttributeValue, Attribute, EntityType


admin.site.register(DictionaryAttribute)
admin.site.register(DictionaryAttributeValue)
admin.site.register(Attribute)
admin.site.register(EntityType)
