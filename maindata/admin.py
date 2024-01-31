from django.contrib import admin
from .models import Car, Category, Color, Client, SellOperation
from django.urls import reverse
from django.utils.html import format_html
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

class UnpaidFilter(admin.SimpleListFilter):
    title = _('كشف المديونيات')
    parameter_name = 'FinishedORNot'

    def lookups(self, request, model_admin):
        return (
            ('depit', _(' لم يكتمل السداد')),
            ('notdepit', _(' اكتمل السداد')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'depit':
            unpaid_ids = [selloperation.id for selloperation in queryset if selloperation.charge() > 0]
            return queryset.filter(id__in=unpaid_ids)
        if self.value() == 'notdepit':
            paid_ids = [selloperation.id for selloperation in queryset if selloperation.charge() <= 0]
            return queryset.filter(id__in=paid_ids)


class ClientInline(admin.StackedInline):
    model = Client
    extra = 1
    max_num = 1

# class CarInline(admin.TabularInline):
#     model = Car
#     extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color', )
    search_fields = ('color',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('category','is_out', 'code','manufacture_year', 'color','government','traffic','gawap_type',
                    'date_added', 'name','phone_number','garunty','get_garunty_file_url','followingcard')
    list_filter = ('category','government','is_out')
    search_fields = ('category__name', 'code', 'government')
    autocomplete_fields = ('category',)
    change_list_template = 'admin/maindata/Car/change_list.html'
    
    def get_garunty_file_url(self,obj):
        car_id = obj.id
        garunty_file_url = None
        if obj.garunty_file:
            garunty_file = obj.garunty_file
            garunty_file_url = garunty_file.url
        modal_html = render_to_string('admin/maindata/car/show_guarantee_image.html', {
            'garunty_file_url' : garunty_file_url,
        })
        return format_html(modal_html)
    

    
    def followingcard(self, obj):
        car_id = obj.id
        url = reverse('maindata:carfollowingcard', args=[car_id])
        return format_html('<a class="button rounded " href="{}">كارت متابعة </a>', url)
    
    followingcard.short_description = ' كارت متابعة '
    get_garunty_file_url.short_description = ' صورة الضمان '
    
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'national_id','date_added','file','notes')
    search_fields = ('name', 'phone_number', 'national_id')

class SellOperationAdmin(admin.ModelAdmin):
    list_display = ('car','getclientname', 'getclientphone_number','getcarownername','getcarownerphone_number',
                    'sell_price', 'paid','charge','sell_date','printinvoice')
    search_fields = ('car__category__name', 'car__code', 'car__government')
    list_filter = ('car__category','car__government','sell_date',UnpaidFilter)
    inlines = [ClientInline,]
    # autocomplete_fields = ('car',)
    raw_id_fields = ('car',)
    
    
    def getclientname(self, obj):
        client = Client.objects.get(selloperation = obj)
        if client.name:
            return client.name
        else:
            return 'غير معروف'
    def getclientphone_number(self, obj):
        client = Client.objects.get(selloperation = obj)
        if client.phone_number:
            return client.phone_number
        else:
            return 'غير معروف'
        
    def getcarownername(self, obj):

        if obj.car.name:
            return obj.car.name
        else:
            return 'غير معروف'
    def getcarownerphone_number(self, obj):
        try:
            if obj.car.phone_number:
                return obj.car.phone_number
            else:
                return 'غير معروف'
        except:
            return 'غير معروف'
    
    def printinvoice(self, obj):
        selloperation_id = obj.id
        url = reverse('maindata:invoice', args=[selloperation_id])
        return format_html('<a class="button rounded " href="{}">فاتورة </a>', url)
    
    printinvoice.short_description = ' فاتورة '
    getclientname.short_description = ' المشترى '
    getclientphone_number.short_description = 'تليفون المشترى '
    getcarownername.short_description = ' البائع '
    getcarownerphone_number.short_description = 'تليفون البائع '

admin.site.register(Category,CategoryAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(SellOperation,SellOperationAdmin)



