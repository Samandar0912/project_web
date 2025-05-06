from rest_framework.serializers import ModelSerializer
from myapp.models import (
    BankModel, TashkilotModel, HududModel, JinoyatModel, 
    IlovaModel, XitrModel, ResultModel, UserModelInfo
)



# Har bir model uchun Serializer sinflarini aniqlash
class BankModelSerializer(ModelSerializer):
    class Meta:
        model = BankModel
        fields = '__all__'

class TashkilotModelSerializer(ModelSerializer):
    class Meta:
        model = TashkilotModel
        fields = '__all__'

class HududModelSerializer(ModelSerializer):
    class Meta:
        model = HududModel
        fields = '__all__'

class JinoyatModelSerializer(ModelSerializer):
    class Meta:
        model = JinoyatModel
        fields = '__all__'

class IlovaModelSerializer(ModelSerializer):
    class Meta:
        model = IlovaModel
        fields = '__all__'

class XitrModelSerializer(ModelSerializer):
    class Meta:
        model = XitrModel
        fields = '__all__'

class ResultModelSerializer(ModelSerializer):
    class Meta:
        model = ResultModel
        fields = '__all__'

class UserModelInfoSerializer(ModelSerializer):
    class Meta:
        model = UserModelInfo
        fields = '__all__'