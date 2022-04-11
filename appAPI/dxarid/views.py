from django.shortcuts import render
from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from dxarid.models import Main, Products


class DxaridAPIView(APIView, APIException):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated, )
    def get(self, request, format=None):
        lst = Main.objects.all().values()
        return Response({
            'data': 'empty' if len(list(lst)) == 0 else lst
        })

    def post(self, request):

        objs_main = []
        obj_prods = []
        for item in request.data:
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
        for prod in request.data:
            lot_id = prod['lot_info']['id']
            prods = prod['products']
            for i in prods:
                p = Products(
                        lot_id=lot_id,
                        art_id = i['art_id'],
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

        return Response({'message': [ids['lot_info']['id'] for ids in request.data]})
