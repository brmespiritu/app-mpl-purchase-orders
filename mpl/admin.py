# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (
    Client,
    Supplier,
    ClientPurchaseRequest,
    ClientPurchaseRequestItem,
    SupplierQuotation,
    SupplierQuotationItem,
    MPLQuotation,
    MPLQuotationItem,
    ClientPurchaseOrder,
    ClientPurchaseOrderItem,
    MPLPurchaseOrder,
    MPLPurchaseOrderItem
)
from .export import export_csv

class MPLAdminSite(AdminSite):
    site_header = 'MPL Administration'

mpl_admin_site = MPLAdminSite(name='mpl_admin_site')

# Customize admin site header and title
mpl_admin_site.site_title = 'MPL Admin'
mpl_admin_site.site_header = 'MPL Purchase Orders'

#register Client
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel_no', 'fax_no', 'contact_person')
    search_fields = ('name', 'contact_person')
mpl_admin_site.register(Client, ClientAdmin)

#register supplier
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel_no', 'fax_no', 'contact_person')
    search_fields = ('name', 'contact_person')
mpl_admin_site.register(Supplier, SupplierAdmin)

# register Client purchase request with items
class ClientPurchaseRequestItemInline(admin.TabularInline):
    model = ClientPurchaseRequestItem

class ClientPurchaseRequestAdmin(admin.ModelAdmin):
    actions = [export_csv]
    list_display = ('client', 'request_no')
    list_filter = ('client__name', 'delivery_date')
    inlines = [
        ClientPurchaseRequestItemInline,
    ]
    search_fields = (
        'clientpurchaserequestitem__item',
        'clientpurchaserequestitem__part_no',
        'clientpurchaserequestitem__notes'
    )
mpl_admin_site.register(ClientPurchaseRequest, ClientPurchaseRequestAdmin)

# register supplier quotation with items
class SupplierQuotationItemInline(admin.TabularInline):
    model = SupplierQuotationItem

class SupplierQuotationAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'quotation_no', 'status')
    list_filter = ('supplier__name', 'status', 'quotation_date')
    inlines = [
        SupplierQuotationItemInline,
    ]
    search_fields = (
        'quotation_no',
        'supplierquotationitem__item',
        'supplierquotationitem__part_no',
        'supplierquotationitem__notes'
    )
mpl_admin_site.register(SupplierQuotation, SupplierQuotationAdmin)

# register MPL Quotations with items
class MPLQuotationItemInline(admin.TabularInline):
    model = MPLQuotationItem

class MPLQuotationAdmin(admin.ModelAdmin):
    list_display = ('client', 'quotation_no', 'status')
    list_filter = ('client__name', 'status', 'quotation_date')
    inlines = [
        MPLQuotationItemInline,
    ]
    search_fields = (
        'quotation_no',
        'mplquotationitem__item',
        'mplquotationitem__part_no',
        'mplquotationitem__notes'
    )
mpl_admin_site.register(MPLQuotation, MPLQuotationAdmin)

# register Client purchase order with items
class ClientPurchaseOrderItemInline(admin.TabularInline):
    model = ClientPurchaseOrderItem

class ClientPurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'purchase_order_no', 'status')
    list_filter = ('client__name', 'status')
    inlines = [
        ClientPurchaseOrderItemInline,
    ]
    search_fields = (
        'purchase_order_no',
        'clientpurchaseorderitem__item',
        'clientpurchaseorderitem__part_no',
        'clientpurchaseorderitem__notes'
    )
mpl_admin_site.register(ClientPurchaseOrder, ClientPurchaseOrderAdmin)


# register MPL purchase order with items
class MPLPurchaseOrderItemInline(admin.TabularInline):
    model = MPLPurchaseOrderItem

class MPLPurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'purchase_order_no', 'status')
    list_filter = ('supplier__name', 'status')
    inlines = [
        MPLPurchaseOrderItemInline,
    ]
    search_fields = (
        'purchase_order_no',
        'mplpurchaseorderitem__item',
        'mplpurchaseorderitem__part_no',
        'mplpurchaseorderitem__notes'
    )
mpl_admin_site.register(MPLPurchaseOrder, MPLPurchaseOrderAdmin)
