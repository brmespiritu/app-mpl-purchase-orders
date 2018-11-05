# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from enumfields import EnumField
from enumfields import Enum

class DeliveryStatus(Enum):
    IN_TRANSIT = "In Transit"
    AT_WAREHOUSE = "At Warehouse"
    DELIVERED = "Delivered"


class SupplierQuotationStatus(Enum):
    AWARDED = "Awarded"
    REJECTED = "Rejected"

class MPLQuotationStatus(Enum):
    PENDING = "Pending"
    AWARDED = "Awarded"
    LOST = "Lost"


class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False) #required
    tel_no = models.CharField(max_length=20, null=True, blank=True)
    fax_no = models.CharField(max_length=20, null=True, blank=True)
    contact_person = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return str(self.name)

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False) #required
    tel_no = models.CharField(max_length=20, null=True, blank=True)
    fax_no = models.CharField(max_length=20, null=True, blank=True)
    contact_person = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return str(self.name)


class ClientPurchaseRequest(models.Model):
    class Meta:
        verbose_name = ("Client Purchase Request")
        verbose_name_plural = ("Client Purchase Requests")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    request_no = models.CharField(max_length=20, null=False, blank=False)
    delivery_date = models.DateTimeField(default=now, null=True, blank=True)
    delivery_location = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return str(self.client)


class ClientPurchaseRequestItem(models.Model):
    purchase_request = models.ForeignKey(ClientPurchaseRequest, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    units = models.CharField(max_length=10, null=True, blank=True)
    item = models.CharField(max_length=200, null=True, blank=True)
    part_no = models.CharField(max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)


class SupplierQuotation(models.Model):
    class Meta:
        verbose_name = ("Supplier Quotation")
        verbose_name_plural = ("Supplier Quotations")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quotation_no = models.CharField(max_length=20, null=True, blank=True)
    quotation_date = models.DateTimeField(default=now, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    status = EnumField(SupplierQuotationStatus, max_length=1)
    net_total = models.DecimalField(default=0, max_digits=9, decimal_places=2)

    def __unicode__(self):
        return str(self.supplier)


class SupplierQuotationItem(models.Model):
    supplier_quotation = models.ForeignKey(SupplierQuotation, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    units = models.CharField(max_length=10, null=True, blank=True)
    item = models.CharField(max_length=200, null=True, blank=True)
    part_no = models.CharField(max_length=100, null=True, blank=True)
    unit_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    total_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    notes = models.CharField(max_length=200, null=True, blank=True)


class MPLQuotation(models.Model):
    class Meta:
        verbose_name = ("MPL Quotation")
        verbose_name_plural = ("MPL Quotations")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quotation_no = models.CharField(max_length=20, null=True, blank=True)
    quotation_date = models.DateTimeField(default=now, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    status = EnumField(MPLQuotationStatus, max_length=1)
    client_purchase_request = models.ForeignKey(ClientPurchaseRequest, null=True, on_delete=models.SET_NULL)
    net_total = models.DecimalField(default=0, max_digits=9, decimal_places=2)

    def __unicode__(self):
        return str(self.client)


class MPLQuotationItem(models.Model):
    mpl_quotation = models.ForeignKey(MPLQuotation, null=True, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    units = models.CharField(max_length=10, null=True, blank=True)
    item = models.CharField(max_length=200, null=True, blank=True)
    part_no = models.CharField(max_length=100, null=True, blank=True)
    unit_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    total_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    notes = models.CharField(max_length=200, null=True, blank=True)


class ClientPurchaseOrder(models.Model):
    class Meta:
        verbose_name = ("Client Purchase Order")
        verbose_name_plural = ("Client Purchase Orders")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    purchase_order_no = models.CharField(max_length=20, null=True, blank=True)
    mpl_quotation = models.ForeignKey(MPLQuotation, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200, null=True, blank=True)
    ordered_by = models.CharField(max_length=100, null=True, blank=True)
    order_date = models.DateTimeField(default=now, null=True, blank=True)
    requested_delivery_date = models.DateTimeField(default=now, null=True, blank=True)
    actual_delivery_date = models.DateTimeField(default=now, null=True, blank=True)
    status = EnumField(DeliveryStatus, max_length=1)
    notes = models.CharField(max_length=200, null=True, blank=True)
    net_total = models.DecimalField(default=0, max_digits=9, decimal_places=2)

    def __unicode__(self):
        return str(selt.client)


class ClientPurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(ClientPurchaseOrder, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    units = models.CharField(max_length=10, null=True, blank=True)
    item = models.CharField(max_length=200, null=True, blank=True)
    part_no = models.CharField(max_length=100, null=True, blank=True)
    unit_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    total_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    notes = models.CharField(max_length=200, null=True, blank=True)


class MPLPurchaseOrder(models.Model):
    class Meta:
        verbose_name = ("MPL Purchase Order")
        verbose_name_plural = ("MPL Purchase Orders")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_order_no = models.CharField(max_length=20, null=True, blank=True)
    supplier_quotation = models.ForeignKey(SupplierQuotation, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200, null=True, blank=True)
    ordered_by = models.CharField(max_length=100, null=True, blank=True)
    order_date = models.DateTimeField(default=now, null=True, blank=True)
    requested_delivery_date = models.DateTimeField(default=now, null=True, blank=True)
    actual_delivery_date = models.DateTimeField(default=now, null=True, blank=True)
    status = EnumField(DeliveryStatus, max_length=1)
    notes = models.CharField(max_length=200, null=True, blank=True)
    net_total = models.DecimalField(default=0, max_digits=9, decimal_places=2)

    def __unicode__(self):
        return str(self.supplier)


class MPLPurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(MPLPurchaseOrder, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    units = models.CharField(max_length=10, null=True, blank=True)
    item = models.CharField(max_length=200, null=True, blank=True)
    part_no = models.CharField(max_length=100, null=True, blank=True)
    unit_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    total_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    notes = models.CharField(max_length=200, null=True, blank=True)
