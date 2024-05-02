
from django.shortcuts import render, redirect
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from .models import CustomToken, U_user, role, permission, Internal_User, role_permission, user_meta
from .serializers import U_userSerializer, RoleSerializer, PermissionSerializer, InternalUserSerializer, RolePermissionSerializer, MetaUserSerializer, UserSerializer
from .models import Property_Owner_meta, Property_Owner, Property, Property_meta, Property_Bills, Bills, Sector, Zone, Society, Property_Type
from .serializers import Property_OwnerSerializer, Property_Owner_metaSerializer, PropertySerializer, Property_metaSerializer, Property_BillsSerializer, BillsSerializer, SectorSerializer, SocietySerializer, ZoneSerializer, Property_TypeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import Internal_User
from django.utils import timezone
from django.contrib.auth.hashers import check_password

from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

# Corrected import statement in studybud/urls.py
#from base import views

def generate_hashed_password(request):
    raw_password = "03162400202**//"  # Assuming the raw password is sent via a POST request
    hashed_password = make_password(raw_password)
    return JsonResponse({'hashed_password': hashed_password})
 


class U_userCreateAPIView(generics.ListCreateAPIView):
    queryset = U_user.objects.all()
    serializer_class = U_userSerializer
    permission_classes = [AllowAny]

class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]

class RoleRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]

class PermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [AllowAny]

class PermissionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [AllowAny]

class InternalUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Internal_User.objects.all()
    serializer_class = InternalUserSerializer
    permission_classes = [AllowAny]

class RolePermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = role_permission.objects.all()
    serializer_class = RolePermissionSerializer
    permission_classes = [AllowAny]

class MetaUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = user_meta.objects.all()
    serializer_class = MetaUserSerializer
    permission_classes = [AllowAny]




class PropertyOwnerListCreatAPIView(generics.ListCreateAPIView):
    queryset = Property_Owner.objects.all()
    serializer_class = Property_OwnerSerializer
    permission_classes = [AllowAny]
        
    
class PropertyOwnerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_Owner.objects.all()
    serializer_class = Property_OwnerSerializer
    permission_classes = [AllowAny]

class PropertyOwnermetaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_Owner_meta.objects.all()
    serializer_class = Property_Owner_metaSerializer
    permission_classes = [AllowAny]

class PropertyOwnermetaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_Owner_meta.objects.all()
    serializer_class = Property_Owner_metaSerializer
    permission_classes = [AllowAny]


class PropertyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

class PropertyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]



class PropertymetaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_meta.objects.all()
    serializer_class = Property_metaSerializer
    permission_classes = [AllowAny]

class PropertymetaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_meta.objects.all()
    serializer_class = Property_metaSerializer
    permission_classes = [AllowAny]


class PropertyBillsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_Bills.objects.all()
    serializer_class = Property_BillsSerializer
    permission_classes = [AllowAny]

class PropertyBillsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]

class BillsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [AllowAny]
    
class BillsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]

class SectorListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [AllowAny]

class SectorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]


class ZoneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [AllowAny]

class ZoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]


class SocietyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]

class SocietyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]


class PropertyTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]

class PropertyTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]




class LoginView(APIView):
    authentication_classes = []  # Remove any authentication classes
    permission_classes = [AllowAny]

    def post(self, request):
        cnic = request.data.get('cnic')
        password = request.data.get('password')
        
        # Query the Internal_User model for a user with the given CNIC
        user = Internal_User.objects.filter(CNIC=cnic).first()

        # Check if a user with the given CNIC exists and the password matches
        if user is not None and check_password(password, user.HashPassword):
        # Authentication successful, return success response
            user.last_login = timezone.now()  # Update last_login timestamp
            user.save()  # Save user object to update last_login field
            token = CustomToken.objects.create(user=user)
            return Response({'token': token.key, 'message': "success"}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials', 'message': "failed"}, status=status.HTTP_401_UNAUTHORIZED)
        





class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Get the token key from the request
        token_key = request.data.get('token')

        # Check if the token exists
        try:
            token = CustomToken.objects.get(key=token_key)
        except CustomToken.DoesNotExist:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the token
        token.delete()

        # Return a success response
        return Response({'detail': 'Logged out successfully','message':"success"}, status=status.HTTP_200_OK)
    

