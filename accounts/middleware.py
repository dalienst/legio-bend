class StreakMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Call update_streak on the authenticated user on each request
            request.user.update_streak()

        response = self.get_response(request)
        return response
