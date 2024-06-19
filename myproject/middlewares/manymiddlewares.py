from django.shortcuts import HttpResponse


class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Brother Initialization, Only execute one time")

    def __call__(self, request):
        print("This is before brotherview")
        response = self.get_response(request)
        print("This is after Brotherview")
        return response


class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Father Initialization, Only execute one time")

    def __call__(self, request):
        print("This is before fatherview")
        # response = self.get_response(request)
        # self.get_response() always call next middleware
        response = HttpResponse("Father Stopped Brother")
        print("This is after fatherview")
        return response


class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Mother Initialization, Only execute one time")

    def __call__(self, request):
        print("This is before motherview")
        response = self.get_response(request)
        print("This is after motherview")
        return response
