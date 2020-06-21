from django import forms

import django_filters
from home.models import Product, Product_detail

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('name',)