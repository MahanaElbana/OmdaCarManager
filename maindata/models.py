from django.db import models
from datetime import datetime
import random
class Category(models.Model):
    name = models.CharField(verbose_name = " نوع السيارة",max_length=200,null=True,blank=True)
    class Meta:
        verbose_name_plural = '   انواع السيارات '
        verbose_name='   نوع سيارة'
    def __str__(self) :
        try:
            return self.name
        except:
            return 'غير معروف'
        
class Color(models.Model):
    color = models.CharField(verbose_name = "اللون",max_length=100,null=True,blank=True)
    class Meta:
        verbose_name_plural = 'الالوان '
        verbose_name='    لون'
    def __str__(self) :
        try:
            return self.color
        except:
            return 'غير معروف'

class Car(models.Model):
    garunties = (
        ('1','موجود'),
        ('2','غير موجود'),
    )
    gawap_types = (
        ('1','بصرى'),
        ('2',' سمعى'),
        ('2',' ذهنى'),
        ('2',' حركى'),
    )
    
    governments = (
        ('1','القاهرة'),
        ('2','الغربية'),
        ('3','كفر الشيخ'),
        ('4','المنوفية'),
        ('5','الدقهلية'),
        ('6','الإسكندرية'),
        ('7','البحيرة'),
        ('8','الإسماعيلية'),
        ('9','الجيزة'),
        ('10','السويس'),
        ('11','الشرقية'),
        ('12','القليوبية'),
        ('13','بني سويف'),
        ('14','الفيوم'),
        ('15','دمياط'),
        ('16','البحر الأحمر'),
        ('17','بورسعيد'),
        ('18','أسوان'),
        ('19','أسيوط'),
        ('20','الأقصر'),
        ('21','سوهاج'),
        ('22','قنا'),
        ('23','مطروح'),
        ('24','المنيا'),
        ('25','الوادي الجديد'),
        ('26','جنوب سيناء'),
        ('27','شمال سيناء'),
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " نوع السيارة") 
    manufacture_year = models.CharField(verbose_name = " سنة الصنع",max_length=10,null=True,blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL,verbose_name = "اللون" ,null=True,blank=True)
    government = models.CharField(verbose_name = "  المحافظة ",choices = governments,default='1',max_length=50,null=True,blank=True )
    traffic = models.CharField(verbose_name = "  المرور ",max_length=200,null=True,blank=True )
    gawap_type = models.CharField(verbose_name = "  نوع الجواب ",choices = gawap_types,default='1',max_length=200,null=True,blank=True )
    date_added = models.DateTimeField(verbose_name = " تاريخ دخول المعرض",auto_now_add=True,null=True,blank=True) 
    native_price = models.FloatField(verbose_name = "السعر الشراء ",default = 0 ,null=True,blank=True)
    
    garunty = models.CharField(verbose_name = " الضمان ",choices = garunties,default='1',max_length=50,null=True,blank=True )
    garunty_file = models.FileField(upload_to='garunty_files/',null=True,blank=True,verbose_name = "  صورة من الضمان")
    code = models.CharField(verbose_name="كود السيارة", max_length=12, editable=False, null=True, blank=True)
    name = models.CharField(verbose_name = " اسم المعاق",max_length=200,null=True,blank=True)
    phone_number = models.CharField(verbose_name = "  رقم التليفون",max_length=50 ,null=True,blank=True)
    is_out = models.BooleanField(verbose_name = " تم الخروج؟",default=False , editable=False)
    notes = models.CharField(verbose_name = "  ملاحظات ",max_length=200,null=True,blank=True )
    def save(self, *args, **kwargs):
        if not self.code:
            # Generate the code
            current_date = datetime.now()
            year = current_date.strftime("%y")
            month = current_date.strftime("%m")
            day = current_date.strftime("%d")
            random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
            self.code = f"{year}{month}{day}{random_numbers}"


        super().save(*args, **kwargs)
    
    # def expectedprofet(self):
    #     if self.native_price and self.sell_price:
    #         return self.native_price - self.sell_price
    # expectedprofet.short_description = ' الربح المتوقع '
    class Meta:
        verbose_name_plural = '  السيارات '
        verbose_name='   سيارة'
    def __str__(self) :
        try:
            return self.category.name + '-' +self.manufacture_year
        except:
            return 'غير معروف'

class Client(models.Model):
    selloperation = models.ForeignKey('SellOperation', on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " عملية بيع")  
    name = models.CharField(verbose_name = " اسم العميل",max_length=200,null=True,blank=True)
    phone_number = models.CharField(verbose_name = "  رقم التليفون",max_length=50 ,null=True,blank=True)
    national_id = models.CharField(verbose_name = "  رقم البطاقة ",max_length=200,null=True,blank=True )
    date_added = models.DateTimeField(verbose_name = " تاريخ الاضافة",auto_now_add=True,null=True,blank=True) 
    notes = models.CharField(verbose_name = "  ملاحظات ",max_length=200,null=True,blank=True )
    file = models.FileField(upload_to='client_files/',null=True,blank=True,verbose_name = "  ملف")
    class Meta:
        verbose_name_plural = '  العميل '
        verbose_name='   عميل'
    def __str__(self) :
        try:
            return self.name
        except:
            return 'غير معروف'

class SellOperation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = "  السيارة") 
    sell_date = models.DateTimeField(verbose_name = " تاريخ الخروج",default=datetime.now(),null=True,blank=True)
    sell_price = models.FloatField(verbose_name = " سعر البيع ",default = 0 ,null=True,blank=True)
    paid = models.FloatField(verbose_name = " المدفوع" ,default = 0 ,null=True,blank=True)
    sellprocess_file = models.FileField(upload_to='sellprocess_files/',null=True,blank=True,verbose_name = " ملف")
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.car:
            self.car.is_out = True
            self.car.save()
        
    def charge(self):
        if self.sell_price and self.paid :
            return self.sell_price - self.paid
        else:
            return 'غير معروف'
    def profit(self):
        if self.sell_price and self.car.native_price :
            return self.sell_price - self.car.native_price
        else:
            return 0
    charge.short_description = ' الباقى '
    profit.short_description = ' المكسب '
    # def getoperationprice(self):
    #     return (self.product.sell_price + self.added_value_for_deposite)* self.quantity
    # getoperationprice.short_description = 'مجموع سعر العملية' 
    # getsellpriceforoneitem.short_description = ' سعر البيع للوحده ' 
    class Meta:
        verbose_name_plural = '  عمليات البيع'
        verbose_name='   عملية'
    def __str__(self) :
        try:
            return self.car.car_type
        except:
            return 'غير معروف'

