from django.shortcuts import render
from datetime import datetime, timedelta


# Without Signed Cookies.
# def setcookie(request):
#     response = render(request, "students/setCookie.html")
#     response.set_cookie("name", "arsh", expires=datetime.utcnow() + timedelta(days=2))

#     return response


# Without Signed Cookies.
# def getcookie(request):
#     # get_cookie = request.COOKIES["name"]
#     # get_cookie = request.COOKIES.get("name")
# amit value is default when cookie is not set
#     get_cookie = request.COOKIES.get("name", "amit")
#

#     return render(request, "students/getCookie.html", {"get": get_cookie})


# For signed cookies
def setcookie(request):
    response = render(request, "students/setCookie.html")
    response.set_signed_cookie(
        "name", "arsh", salt="nm", expires=datetime.utcnow() + timedelta(days=2)
    )

    return response


# for getting signed cookies
def getcookie(request):
    get_cookie = request.get_signed_cookie("name", salt="nm")
    return render(request, "students/getCookie.html", {"get": get_cookie})


# same for signed and unsigned cookies
def delcookie(request):
    response = render(request, "students/delCookie.html")
    response.delete_cookie("name")
    return response
