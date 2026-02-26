from django.urls import path
from .views import *

urlpatterns = [
   
    path("",show,name="show"),
    path("register/",register,name="register"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
    path("address/",address,name="address"),
    path("phone/",phone,name="phone"),
    path("Edit_addr/<int:id>",edit_addr,name="Edit_addr"),
    path("Edit_no/<int:id>",edit_no,name="Edit_no"),
    path("Delete_addr/<int:id>",delete_addr,name="Delete_addr"),
    path("Delete_no/<int:id>",delete_no,name="Delete_no"),

    

]