from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Main(models.Model):
    lot_id = models.CharField(max_length=255, null=True)
    lot_name = models.CharField(max_length=255, null=True)
    lot_status = models.CharField(max_length=255, null=True)
    lot_dateini = models.DateTimeField(null=True)
    lot_date_end = models.DateTimeField(null=True)
    lot_group = models.CharField(max_length=255, null=True)
    seller_name =  models.CharField(max_length=255, null=True)
    seller_inn = models.CharField(max_length=255, null=True)
    seller_region = models.CharField(max_length=255, null=True)
    seller_rayon = models.CharField(max_length=255, null=True)
    seller_address = models.CharField(max_length=255, null=True)
    buyer_name = models.CharField(max_length=255, null=True)
    buyer_inn = models.CharField(max_length=255, null=True)
    buyer_account = models.CharField(max_length=255, null=True)
    buyer_region = models.CharField(max_length=255, null=True)
    buyer_rayon = models.CharField(max_length=255, null=True)
    buyer_address = models.CharField(max_length=255, null=True)
    # user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)


    def __str__(self):
        return self.lot_id

    class Meta():
        managed = True
        db_table = 'dxarid\".\"main'

class Products(models.Model):
    lot_id = models.CharField(max_length=255, null=True)
    art_id = models.IntegerField( null=True)
    p_product_name =  models.CharField(max_length=255, null=True)
    measure_gnk = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(null=True)
    one_price = models.IntegerField(null=True)
    all_price = models.IntegerField(null=True)
    descript = models.CharField(max_length=255, null=True)
    tnvd_code = models.CharField(max_length=255, null=True)
    expend_id = models.CharField(max_length=255, null=True)
    plan_position_id = models.IntegerField(null=True)
    # user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.art_id

    class Meta():
        managed = True
        db_table = 'dxarid\".\"products'


