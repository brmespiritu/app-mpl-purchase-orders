# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
    Supplier, PurchaseOrder, PurchaseOrderItem
)

# register purchase order with items
class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem

class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [
        PurchaseOrderItemInline,
    ]
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)

#register supplier
admin.site.register(Supplier)
