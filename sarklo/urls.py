from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="shop-index"),
    url(r'^oglas/(?P<id>[0-9]+)/$', views.oglas_detalji, name="oglas_detalji"),
    path('delikates/', views.deli, name="shop-delikates"),
    path('skolske/', views.skolske, name="shop-skolske"),
    path('beletristika/', views.beletristika, name="shop-beletristika"),
    path('komentari/', views.comments, name="shop-comments"),
    path('postavi_oglas/', views.create_oglas, name="shop-add-oglas"),
    path('odeca_zenska/', views.odeca_zenska, name="shop-odeca-zenska"),
    path('odeca_muska/', views.odeca_muska, name="shop-odeca-muska"),
    path('osn_1_razred/', views.osn_1_razred, name="osn_1_razred"),
    path('osn_2_razred/', views.osn_2_razred, name="osn_2_razred"),
    path('osn_3_razred/', views.osn_3_razred, name="osn_3_razred"),
    path('osn_4_razred/', views.osn_4_razred, name="osn_4_razred"),
    path('osn_5_razred/', views.osn_5_razred, name="osn_5_razred"),
    path('osn_6_razred/', views.osn_6_razred, name="osn_6_razred"),
    path('osn_7_razred/', views.osn_7_razred, name="osn_7_razred"),
    path('osn_8_razred/', views.osn_8_razred, name="osn_8_razred"),
    path('sred_1_razred/', views.sred_1_razred, name="sred_1_razred"),
    path('sred_2_razred/', views.sred_2_razred, name="sred_2_razred"),
    path('sred_3_razred/', views.sred_3_razred, name="sred_3_razred"),
    path('sred_4_razred/', views.sred_4_razred, name="sred_4_razred"),

]