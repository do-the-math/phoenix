from rest_framework.permissions import BasePermission, SAFE_METHODS


# class ReadOnlyPermission(BasePermission):
#     """
#     Global permission check for blacklisted IPs.
#     """

#     def has_permission(self, request, view):
#         if (
#             request.user.is_authenticated
#             and request.user.userprofile.read_only_user
#             and request.method not in SAFE_METHODS
#         ):
#             return False

#         return True
