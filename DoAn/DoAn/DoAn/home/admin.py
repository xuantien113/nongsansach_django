# from django.contrib import admin
# from .models import SanPham, LoaiSanPham,DatHang,KhachHang,ChiTietDatHang,GiaoHang
# # Register your models here.
# admin.site.register(SanPham)
# admin.site.register(LoaiSanPham)
# admin.site.register(DatHang)
# admin.site.register(KhachHang)
# admin.site.register(ChiTietDatHang)
# admin.site.register(GiaoHang)

from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
