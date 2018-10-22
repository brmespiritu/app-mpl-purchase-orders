# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False) #required
    tel_no = models.CharField(max_length=20, null=True, blank=True)
    fax_no = models.CharField(max_length=20, null=True, blank=True)
    contact_person = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_order_no = models.CharField(max_length=20, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ordered_by = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    supplier_ref_no = models.CharField(max_length=20, null=True, blank=True)


class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    units = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    unit_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    net_total = models.DecimalField(default=0, max_digits=9, decimal_places=2)
