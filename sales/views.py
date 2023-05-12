from django.shortcuts import render
from sales.models import Sales
from sales.serializers import SalesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
# Create your views here.
from django.db.models import Count,Sum 
from .models import Sales
import json 
class SalesListView(APIView):

    def get(self, request, format=None):
        sales = Sales.objects.all()
        serializer = SalesSerializer(sales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesDetailView(APIView):
    def get_object(self, pk):
        try:
            return Sales.objects.get(pk=pk)
        except Sales.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sales = self.get_object(pk)
        serializer = SalesSerializer(sales)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sales = self.get_object(pk)
        serializer = SalesSerializer(sales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sales = self.get_object(pk)
        sales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    


class SaleReportView(View):
    def get(self, request):
          
        order_per_year=Sales.objects.values('order_date__year').annotate(
            order_count=Count('id')
            ).order_by("-order_date__year")
        
        all_customers=Sales.objects.values("customer_id").distinct().count() 
        top_customers=Sales.objects.values('customer_id',"customer_name").annotate(
            order_count=Count('pk'),
            sale_transaction=Sum("sales")).order_by("-sale_transaction")[:3]
        
        customer_transaction=Sales.objects.values('order_date__year').annotate(
            sale_transaction=Sum("sales")).order_by("-order_date__year")
        sub_catgory_count=Sales.objects.values('sub_category').annotate(count=Count('id')).order_by("-count")
        region_basis_sale_transation=Sales.objects.values('region').annotate(transaction=Sum("sales")).order_by("transaction")
        region=[]
        transaction=[]
        for region_transaction in region_basis_sale_transation:
            region.append(region_transaction["region"])
            transaction.append(float(region_transaction["transaction"]))
        region_transaction_data={"region":region,"transaction":transaction}
        
        order_year=[]
        transaction=[]
        for region_transaction in customer_transaction:
            order_year.append(region_transaction["order_date__year"])
            transaction.append(float(region_transaction["sale_transaction"]))
        customer_transaction_line_data={"order_year":order_year,"transaction":transaction}
       
        context={
             "order_per_year":order_per_year,
             "all_costomers":all_customers,
             "top_customers":top_customers,
             "customer_transaction":customer_transaction,
             "sub_catgory_count":sub_catgory_count,
             "region_transaction_data":region_transaction_data,
             "customer_transaction_line_data":customer_transaction_line_data
         }
        
        return render(request,("sale_report.html"),context)
    

