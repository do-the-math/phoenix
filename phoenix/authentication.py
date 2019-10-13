# from django.contrib.auth import get_user_model
# from django.utils.translation import ugettext_lazy as _
# from rest_framework import exceptions
# from rest_framework.authentication import (SessionAuthentication,
#                                            TokenAuthentication)


# class PhoenixTokenAuthentication(TokenAuthentication):
#     def authenticate_credentials(self, key):
#         model = self.get_model()
#         try:
#             token = model.objects.get(key=key)
#         except model.DoesNotExist:
#             raise exceptions.AuthenticationFailed(_('Invalid token.'))

#         if not token.user.is_active:
#             raise exceptions.AuthenticationFailed(
#                 _('User inactive or deleted.'))

#         return (token.user, token)

#     def authenticate(self, request):
#         """
#         Returns a `User` if the request session currently has a logged in user.
#         Otherwise returns `None`.
#         """

#         # Get the session-based user from the underlying HttpRequest object
#         pass


# # class PhoenixSessionAuthentication(SessionAuthentication):

# #     def authenticate(self, request):
# #         """
# #         Returns a `User` if the request session currently has a logged in user.
# #         Otherwise returns `None`.
# #         """

# #         # Get the session-based user from the underlying HttpRequest object
# #         user = getattr(request._request, 'user', None)

# #         # Unauthenticated, CSRF validation not required
# #         if not user or not user.is_active:
# #             return None

# #         self.enforce_csrf(request)

# #         User = get_user_model()
# #         user = User.objects.get(pk=user.id)
# #         # CSRF passed with authenticated user
# #         return (user, None)
