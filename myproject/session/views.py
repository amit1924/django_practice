from django.shortcuts import render


# Create your views here.
################################
# Set session without method
# def setsession(request):
#     request.session["name"] = "Arsh"
#     request.session["value"] = "Amit"
#     return render(request, "students/setsession.html")


# def getsession(request):
#     # name = request.session["name"]
#     name = request.session.get("name", default="Guest")
#     value = request.session.get("value")
#     return render(request, "students/getsession.html", {"name": name, "value": value})


# def delsession(request):
#     if "name" in request.session:
#         del request.session["name"]
#     return render(request, "students/delsession.html")

################################
#  Set,get ,delete session with method
# def setsession(request):
#     request.session["name"] = "Arsh"
#     request.session["value"] = "Amit"

#     return render(request, "students/setsession.html")


# def getsession(request):

#     name = request.session.get("name")
#     value = request.session.get("value")
#     keys = request.session.keys()
#     items = request.session.items()
#     age = request.session.setdefault("age", "26")
#     return render(
#         request,
#         "students/getsession.html",
#         {"name": name, "value": value, "keys": keys, "items": items, "age": age},
#     )

# def delsession(request):
# request.session.flush()
# return render(request, "students/delsession.html")


##################################


# def setsession(request):
#     request.session["name"] = "Arsh"
#     request.session["value"] = "Amit"
#     # This below code will expire my session
#     request.session.set_expiry(600)
#     return render(request, "students/setsession.html")


# # Another Process of Methods
# def getsession(request):

#     name = request.session["name"]
#     value = request.session["value"]
# (request):
#     return render(
#         request,
#         "students/getsession.html",
#         {"name": name, "value": value},
#     )


# def delsession(request):
#     request.session.flush()
#     # below code will clear my  session from the database and from my browser
#     request.session.clear_expired()
#     return render(request, "students/delsession.html")


################################
# To Check Browser support cookies or not


# def set_test_cookie(request):
#     request.session.set_test_cookie()
#     return render(request, "students/getsession.html")


# def check_test_cookie(request):
#     request.session.test_cookie_worked()
#     return render(request, "students/getsession.html")


# def del_test_cookie(request):
#     request.session.delete_test_cookie()
#     return render(request, "students/delsession.html")


################################################################
# Set Session Settings


def setsession(request):
    request.session["name"] = "Arsh"
    request.session["value"] = "Amit"

    return render(request, "students/setsession.html")


def getsession(request):

    name = request.session.get("name")
    value = request.session.get("value")

    return render(
        request,
        "students/getsession.html",
        {"name": name, "value": value},
    )


def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, "students/delsession.html")
