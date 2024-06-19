from django.contrib import admin
from django.urls import path

# from cookie import views
from session import views

# urlpatterns = [
# cookie url
# path("admin/", admin.site.urls),
# path("setcookie/", views.setcookie),
# path("getcookie/", views.getcookie),
# path("delcookie/", views.delcookie),
################################
# Session URL
# path("setsession/", views.setsession),
# path("getsession/", views.getsession),
# path("delsession/", views.delsession),
# ]


################################################################
# Browser support cookies or not

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("set_test_cookie/", views.set_test_cookie, name="set_test_cookie"),
#     path("check_test_cookie/", views.check_test_cookie, name="check_test_cookie"),
#     path("del_test_cookie/", views.del_test_cookie, name="del_test_cookie"),

# ]


################################################################
# Set Session Settings
# urlpatterns = [
#     path("setsession/", views.setsession),
#     path("getsession/", views.getsession),
#     path("delsession/", views.delsession),
# ]


################################################################
# Middleware urls
# from middleware import views

# urlpatterns = [
#     # path("admin/", admin.site.urls),
#     path("", views.home),
# ]


################################################################
# Many middlewares urls
from middlewares import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.home),
]
