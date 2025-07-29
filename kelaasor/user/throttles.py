from rest_framework.throttling import SimpleRateThrottle



class UserLogOutThrottle(SimpleRateThrottle):
    scope = "logout"