# Function Based Middleware


# def my_middleware(get_response):
#     # get_response work as next in express js
#     # initalized one time
#     print("One Time Initialization")

#     def middleware_function(request):
#         print("This is before view")
#         response = get_response(request)
#         #  response = get_response(request) this will work after executing view
#         print("This is after view")
#         return response

# return middleware_function


################################################################
# class Based Middleware


class Mymiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization, Only execute one time")

    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response
