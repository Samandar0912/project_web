from rest_framework import generics
from rest_framework.permissions import AllowAny
from myapp.models import (
    BankModel, TashkilotModel, HududModel, JinoyatModel,
    IlovaModel, XitrModel, ResultModel, UserModelInfo
)
from api.serializer import (
    BankModelSerializer, TashkilotModelSerializer, HududModelSerializer,
    JinoyatModelSerializer, IlovaModelSerializer, XitrModelSerializer,
    ResultModelSerializer, UserModelInfoSerializer
)

# Reusable Base View
class BaseRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    lookup_field = 'id'

# Bank
class BankListApiView(generics.ListAPIView):
    queryset = BankModel.objects.all()
    serializer_class = BankModelSerializer
    permission_classes = [AllowAny]

class BankCreateApiView(generics.CreateAPIView):
    queryset = BankModel.objects.all()
    serializer_class = BankModelSerializer
    permission_classes = [AllowAny]

class BankDetailApiView(BaseRUDView):
    queryset = BankModel.objects.all()
    serializer_class = BankModelSerializer

# Tashkilot
class TashkilotListApiView(generics.ListAPIView):
    queryset = TashkilotModel.objects.all()
    serializer_class = TashkilotModelSerializer
    permission_classes = [AllowAny]

class TashkilotCreateApiView(generics.CreateAPIView):
    queryset = TashkilotModel.objects.all()
    serializer_class = TashkilotModelSerializer
    permission_classes = [AllowAny]

class TashkilotDetailApiView(BaseRUDView):
    queryset = TashkilotModel.objects.all()
    serializer_class = TashkilotModelSerializer

# Hudud
class HududListApiView(generics.ListAPIView):
    queryset = HududModel.objects.all()
    serializer_class = HududModelSerializer
    permission_classes = [AllowAny]

class HududCreateApiView(generics.CreateAPIView):
    queryset = HududModel.objects.all()
    serializer_class = HududModelSerializer
    permission_classes = [AllowAny]

class HududDetailApiView(BaseRUDView):
    queryset = HududModel.objects.all()
    serializer_class = HududModelSerializer

# Jinoyat
class JinoyatListApiView(generics.ListAPIView):
    queryset = JinoyatModel.objects.all()
    serializer_class = JinoyatModelSerializer
    permission_classes = [AllowAny]

class JinoyatCreateApiView(generics.CreateAPIView):
    queryset = JinoyatModel.objects.all()
    serializer_class = JinoyatModelSerializer
    permission_classes = [AllowAny]

class JinoyatDetailApiView(BaseRUDView):
    queryset = JinoyatModel.objects.all()
    serializer_class = JinoyatModelSerializer

# Ilova
class IlovaListApiView(generics.ListAPIView):
    queryset = IlovaModel.objects.all()
    serializer_class = IlovaModelSerializer
    permission_classes = [AllowAny]

class IlovaCreateApiView(generics.CreateAPIView):
    queryset = IlovaModel.objects.all()
    serializer_class = IlovaModelSerializer
    permission_classes = [AllowAny]

class IlovaDetailApiView(BaseRUDView):
    queryset = IlovaModel.objects.all()
    serializer_class = IlovaModelSerializer

# Xitr
class XitrListApiView(generics.ListAPIView):
    queryset = XitrModel.objects.all()
    serializer_class = XitrModelSerializer
    permission_classes = [AllowAny]

class XitrCreateApiView(generics.CreateAPIView):
    queryset = XitrModel.objects.all()
    serializer_class = XitrModelSerializer
    permission_classes = [AllowAny]

class XitrDetailApiView(BaseRUDView):
    queryset = XitrModel.objects.all()
    serializer_class = XitrModelSerializer

# Result
class ResultListApiView(generics.ListAPIView):
    queryset = ResultModel.objects.all()
    serializer_class = ResultModelSerializer
    permission_classes = [AllowAny]

class ResultCreateApiView(generics.CreateAPIView):
    queryset = ResultModel.objects.all()
    serializer_class = ResultModelSerializer
    permission_classes = [AllowAny]

class ResultDetailApiView(BaseRUDView):
    queryset = ResultModel.objects.all()
    serializer_class = ResultModelSerializer

# User Info
class UserModelInfoListApiView(generics.ListAPIView):
    queryset = UserModelInfo.objects.all()
    serializer_class = UserModelInfoSerializer
    permission_classes = [AllowAny]

class UserModelInfoCreateApiView(generics.CreateAPIView):
    queryset = UserModelInfo.objects.all()
    serializer_class = UserModelInfoSerializer
    permission_classes = [AllowAny]

class UserModelInfoDetailApiView(BaseRUDView):
    queryset = UserModelInfo.objects.all()
    serializer_class = UserModelInfoSerializer
