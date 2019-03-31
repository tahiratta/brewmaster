# from django.conf import settings
# from django.contrib import auth
# from datetime import datetime, timedelta
#
# class AutoLogout(object):
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#
#         print('Requested user', request.user, datetime.now())
#
#         if not request.user.is_authenticated:
#             # Can't log out if not logged in
#             return self.get_response(request)
#
#         request.session['last_touch'] = datetime.now()
#
#         if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
#             print('console is here')
#             try:
#                 print('now here')
#                 auth.logout(request)
#                 del request.session['last_touch']
#             except KeyError:
#                 print('now here it is')
#                 pass
#             else:
#                 print('and now this is running')
#                 request.session['last_touch'] = datetime.now()
#         print('and it ends with it')
#         return self.get_response(request)