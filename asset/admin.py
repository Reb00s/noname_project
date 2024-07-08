from django.contrib import admin
from asset.models import AssetTemplate, Asset, RelationTemplate, Relation


admin.site.register(AssetTemplate)
admin.site.register(Asset)
admin.site.register(RelationTemplate)
admin.site.register(Relation)
