from django.urls import path
from . import views
urlpatterns = [
    path('', views.showemp, name='showemp'),
    path('insert', views.insertemp, name='insertemp'),
    path('edit/<int:id>', views.edittemp, name='edittemp'),
    path('update/<int:id>', views.updatetemp, name='updatetemp'),
    path('delete/<int:id>', views.deleteemp, name='deleteemp'),
]
