from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('photo_view/',views.photo_view,name='photo_view'),
    path('photo/<int:photo_id>',views.detail,name='detail'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]