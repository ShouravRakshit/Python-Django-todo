
from django.contrib import admin
from django.urls import path
from todoapp.views import HomePage, Edittodo, Updatetodo, Update

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePage),
    # dynamic link so that I can get the id when it comes to update and delete.
    path("delete/<int:id>/", Edittodo),
    path("update/<int:id>/", Updatetodo),
    path("updatedata/<int:id>/", Update)
]
