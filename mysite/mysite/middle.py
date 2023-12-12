#Removing the CSRF checks to allow for the API and URL calling from React
class DisableCSRFMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #Removes the CSRF checks
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response