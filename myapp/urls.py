from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', LoginView.as_view(), name='login'),

    path('main/', IndexView.as_view(template_name='index.html'), name='index'),
    path('main/create/', CreateView.as_view(), name='create'),
    path('main/table/', TableView.as_view(), name='table'),
    
    path('main/jinoyat_list/', JinoyatAllView.as_view(), name='jinoyat_list'),
    path('main/jinoyat_list/create', CreateArticleView.as_view(), name='create_article'),

    path('main/fosh-etilgan-list/', JinoyatAll_FEJ_View.as_view(), name='FEJ_list'),
    path('main/fosh-etilgan-list/create', CreateArticle_FEJ_View.as_view(), name='FEJ_create'),

    path('main/Boshqa-tashkilotlar-tomonidan-list/', Boshqa_tashkilot_View.as_view(), name='BTJ_list'),
    path('main/Boshqa-tashkilotlar-tomonidan-list/create', Boshqa_tashkilot_Create_View.as_view(), name='BTJ_create'),

    path('main/Targ\'ibot-list/', targibot_bulim_View.as_view(), name='targibot-bulim_list'),
    path('main/Targ\'ibot-list/create', targibot_bulim_Create_View.as_view(), name='targibot-bulim_create'),

    path('main/Targ\'ibot-boshqa-tashkilot-list/', targibot_boshqa_View.as_view(), name='targibot-boshqa_list'),
    path('main/Targ\'ibot-boshqa-tashkilot-list/create', targibot_boshqa_Create_View.as_view(), name='targibot-boshqa_create'),


]
