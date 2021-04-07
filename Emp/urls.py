from django.urls import path
from Emp import views

urlpatterns=[
path('',views.home,name="hm"),
path('abt/',views.about,name="ab"),
path('con/',views.contact,name="cn"),
path('log/',views.login,name="lg"),
path('reg/',views.register,name="rg"),
path('crud/',views.crud,name="cr"),
path('delete/<str:id>',views.delete,name="delete"),
path('dfy/',views.dform,name="df"),
path('show/',views.show,name="show"),
path('infodelete/<int:et>/',views.infodelete,name="infodelete"),
# path('edit/<int:id>',views.edit,name="editdata"),
path('e/<int:si>/',views.userupdate,name="ue"),
path('ui/<str:uname>/',views.userinfo,name="uif"),


]

