from django.urls import path
from api.views import (
    BankListApiView, BankCreateApiView, BankDetailApiView,
    TashkilotListApiView, TashkilotCreateApiView, TashkilotDetailApiView,
    HududListApiView, HududCreateApiView, HududDetailApiView,
    JinoyatListApiView, JinoyatCreateApiView, JinoyatDetailApiView,
    IlovaListApiView, IlovaCreateApiView, IlovaDetailApiView,
    XitrListApiView, XitrCreateApiView, XitrDetailApiView,
    ResultListApiView, ResultCreateApiView, ResultDetailApiView,
    UserModelInfoListApiView, UserModelInfoCreateApiView, UserModelInfoDetailApiView
)

urlpatterns = [
    # Bank
    path('banks/', BankListApiView.as_view(), name='bank-list'),
    path('banks/create/', BankCreateApiView.as_view(), name='bank-create'),
    path('banks/<int:id>/', BankDetailApiView.as_view(), name='bank-detail'),

    # Tashkilot
    path('tashkilotlar/', TashkilotListApiView.as_view(), name='tashkilot-list'),
    path('tashkilotlar/create/', TashkilotCreateApiView.as_view(), name='tashkilot-create'),
    path('tashkilotlar/<int:id>/', TashkilotDetailApiView.as_view(), name='tashkilot-detail'),

    # Hudud
    path('hududlar/', HududListApiView.as_view(), name='hudud-list'),
    path('hududlar/create/', HududCreateApiView.as_view(), name='hudud-create'),
    path('hududlar/<int:id>/', HududDetailApiView.as_view(), name='hudud-detail'),

    # Jinoyat
    path('jinoyatlar/', JinoyatListApiView.as_view(), name='jinoyat-list'),
    path('jinoyatlar/create/', JinoyatCreateApiView.as_view(), name='jinoyat-create'),
    path('jinoyatlar/<int:id>/', JinoyatDetailApiView.as_view(), name='jinoyat-detail'),

    # Ilova
    path('ilovalar/', IlovaListApiView.as_view(), name='ilova-list'),
    path('ilovalar/create/', IlovaCreateApiView.as_view(), name='ilova-create'),
    path('ilovalar/<int:id>/', IlovaDetailApiView.as_view(), name='ilova-detail'),

    # XITR
    path('xitlar/', XitrListApiView.as_view(), name='xitr-list'),
    path('xitlar/create/', XitrCreateApiView.as_view(), name='xitr-create'),
    path('xitlar/<int:id>/', XitrDetailApiView.as_view(), name='xitr-detail'),

    # Result
    path('natijalar/', ResultListApiView.as_view(), name='result-list'),
    path('natijalar/create/', ResultCreateApiView.as_view(), name='result-create'),
    path('natijalar/<int:id>/', ResultDetailApiView.as_view(), name='result-detail'),

    # User Info
    path('user-info/', UserModelInfoListApiView.as_view(), name='user-info-list'),
    path('user-info/create/', UserModelInfoCreateApiView.as_view(), name='user-info-create'),
    path('user-info/<int:id>/', UserModelInfoDetailApiView.as_view(), name='user-info-detail'),
]
