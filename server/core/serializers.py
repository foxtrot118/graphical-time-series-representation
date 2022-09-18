from rest_framework import serializers
from .models import Sales, Client, Employee, Values ,Returns


class SalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sales
        fields = ['id','file']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id','FullName','Wilaya','Email','PhoneNumber','Function']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','FullName','Wilaya','Email','PhoneNumber','Function']



class ValuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Values
        fields = ['id','name','ticker','description','start_date','end_date','sector','industry','employees_count','sic_no','location','exchange_id','cik_no','cusip','currency_id','data_source_id','ckr_log','similar_fund_log','address','company_name','phone_no','website','is_Active','url_slug','delisted_date','delisted_reason','image_name','image_aspect_ratio','cumulative_return']

class ReturnsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Returns
        fields = ['equity_id','start_date','returns','equity_id','open','high','low','close','adj_close']

	