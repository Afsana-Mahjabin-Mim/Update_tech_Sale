from django.db import models

#Create your models here.


from django.db import models

class Sales(models.Model):
    order_id =models.CharField(max_length=255)
    order_date=models.DateField(auto_now_add=True)
    ship_date =models.DateField()
    ship_mode =models.CharField(max_length=255, null=True, blank=True)
    customer_id=models.CharField(max_length=255)
    customer_name =models.CharField(max_length=255, null=True, blank=True)
    segment =models.CharField(max_length=255, null=True, blank=True)
    country =models.CharField(max_length=255, null=True, blank=True)
    city =models.CharField(max_length=255, null=True, blank=True)
    state =models.CharField(max_length=255, null=True, blank=True)
    postal_code =models.CharField(max_length=255)
    region =models.CharField(max_length=255, null=True, blank=True)
    product_id =models.CharField(max_length=255)
    category =models.CharField(max_length=255, null=True, blank=True)
    sub_category =models.CharField(max_length=255, null=True, blank=True)
    product_name =models.CharField(max_length=255, null=True, blank=True)
    sales =models.DecimalField(max_digits=10,decimal_places=2) 


    def __str__(self) -> str:
        return str(self.order_id)
    

    class Meta:
        db_table="sales_data" 

