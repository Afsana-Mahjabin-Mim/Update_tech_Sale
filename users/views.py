from rest_framework.views import APIView
from rest_framework import status,response
from django.views import View 
from users.serializers import CustomUserSerializer



class UserRegisterAPIView(APIView):
    def post(self,request,format=None):
        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"msg":"Account created successfully"},status=status.HTTP_201_CREATED)
        return response.Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)