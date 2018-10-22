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
    list_display = ('purchase_order_no', 'supplier')
    inlines = [
        PurchaseOrderItemInline,
    ]
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)

#register supplier
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel_no', 'fax_no', 'contact_person')
admin.site.register(Supplier, SupplierAdmin)
