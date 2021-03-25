from django.urls import path

from . import views

app_name = "food"
urlpatterns = [
    # /food/
    path('', views.index, name="index"),
    path('<int:item_id>/', views.detail, name="detail"),
    # add items
    path('add', views.create_item, name="create_item"),
    # update items
    path('update/<int:id>',views.update_item, name='update_item'),
    # delete items
    path('delete/<int:id>', views.delete_item, name='delete_item'),

]
