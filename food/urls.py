from django.urls import path

from . import views

app_name = "food"
urlpatterns = [
    # /food/
    path('', views.IndexClassView.as_view(), name="index"),
    path('<int:pk>/', views.FoodDetail.as_view(), name="detail"),
    # add items
    path('add', views.CreateItem.as_view(), name="create_item"),
    # update items
    path('update/<int:id>',views.update_item, name='update_item'),
    # delete items
    path('delete/<int:id>', views.delete_item, name='delete_item'),

]
