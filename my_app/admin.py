from django.contrib import admin
from .models import Owner, AllBlock


# Register your models here.


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    date_hierarchy = 'data_sales'
    actions_on_bottom = True
    # fields = ('number_block', 'number_kol', 'floor_kol', 'num_apart_per_floor', 'all_all')
    search_fields = ('fio', 'block', 'status')
    list_display = ('fio', 'data_sales', 'status', 'block', 'total_area', 'all_price')
    list_editable = ('data_sales',)

    def all_price(self):
        all_price = 3 * self.total_area
        return all_price

    def all_all(self):
        a = self.number_block * self.number_kol
        b = a * self.floor_kol
        all_all = b * self.num_apart_per_floor
        return all_all


admin.site.register(AllBlock)

