from django.shortcuts import render
from django.db.models.query_utils import Q
from .models import Account

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.


# Get user details 
class check_user(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        data ={}
        status_code = status.HTTP_200_OK

        # Try to get user details
        try:

            # Check if user exist in database
            if Account.objects.filter(email=request.user).exists() == True:
                account = Account.objects.get(email=request.user)
                data["username"]        = account.username
                data["email"]           = account.email
            else:
                data["error"]     = "User not found"
                status_code = status.HTTP_404_NOT_FOUND

        # If 400 error 
        except:
            data["error"]     = "Something when wrong"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


        # Return response 
        return Response(data=data, status=status_code)
