from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    path('', views.page_create, name='page_create'),
    path('page/', views.page_list, name='page_list'),
    path('member/', views.member_list, name='member_list'),
    path('member/add/', views.member_edit, name='member_add'),
    path('member/mod/<int:member_id>/', views.member_edit, name='member_mod'),
    path('member/del/<int:member_id>/', views.member_del, name='member_del'),
    path('attribute/<int:member_id>/', views.attributeList.as_view(), name='attribute_list'),
    path('attribute/add/<int:member_id>/', views.attribute_edit, name='attribute_add'),
    path('attribute/mod/<int:member_id>/<int:attribute_id>/', views.attribute_edit, name='attribute_mod'),
    path('attribute/del/<int:member_id>/<int:attribute_id>/', views.attribute_del, name='attribute_del'),
    path('team/', views.team_member_list, name='team_member_list'),
]
