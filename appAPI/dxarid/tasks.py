from __future__ import absolute_import, unicode_literals
from appAPI.celery import app
from .models import Main, Products



@app.task(name='post_test_api')
def post(request):
    objs_main = []
    obj_prods = []
    print(request)
    for item in request:
        m = Main(
            lot_id=item['lot_info']['id'],
            lot_name=item['lot_info']['name'],
            lot_status=item['lot_info']['status_name'],
            lot_dateini=item['lot_info']['dateini'],
            lot_date_end=item['lot_info']['date_end'],
            lot_group=item['lot_info']['item_group_name'],
            seller_name=item['seller']['name'],
            seller_inn=item['seller']['inn'],
            seller_region=item['seller']['region'],
            seller_rayon=item['seller']['rayon'],
            seller_address=item['seller']['address'],
            buyer_name=item['buyer']['name'],
            buyer_inn=item['buyer']['inn'],
            buyer_account=item['buyer']['account'],
            buyer_region=item['buyer']['region'],
            buyer_rayon=item['buyer']['rayon'],
            buyer_address=item['buyer']['address'],
        )
        objs_main.append(m)
    for prod in request:
        lot_id = prod['lot_info']['id']
        prods = prod['products']
        for i in prods:
            p = Products(
                lot_id=lot_id,
                art_id=i['art_id'],
                p_product_name=i['p_product_name'],
                measure_gnk=i['measure_gnk'],
                quantity=i['quantity'],
                one_price=i['one_price'],
                all_price=i['all_price'],
                descript=i['descript'],
                tnvd_code=i['tnvd_code'],
                expend_id=i['expend_id'],
                plan_position_id=i['plan_position_id']

            )
            obj_prods.append(p)

    print(objs_main)
    Main.objects.bulk_create(objs_main, 5000)
    Products.objects.bulk_create(obj_prods, 5000)
