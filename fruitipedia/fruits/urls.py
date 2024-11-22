from django.urls import path, include

from fruitipedia.fruits import views

urlpatterns = (
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create-fruit", views.create_fruit, name="create_fruit"),
    path("create-category", views.create_category, name="create_category"),
    path("<int:fruit_id>/",
         include([
             path("details-fruit", views.details_fruit, name="details_fruit"),
             path("edit-fruit", views.edit_fruit, name="edit_fruit"),
             path("delete-fruit", views.delete_fruit, name="delete_fruit"),

         ])),
)

