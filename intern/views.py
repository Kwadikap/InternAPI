
from logging import exception
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InternSerializer
from .models import Intern
from intern import serializers

class InternList(APIView):
    def get(self, request):
        interns = Intern.objects.all()
        serializer = InternSerializer(interns, many=True)
        return Response(serializer.data)
        
class InternCreate(APIView):
    def post(self, request):
        serializer = InternSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "error": "Invalid fields"
            }, status=status.HTTP_400_BAD_REQUEST)
            
class InternDetail(APIView):
    def get_intern_by_pk(self, pk):
        try:
            return Intern.objects.get(pk=pk)
        except exception:
            return Response({
                "error":"This intern does not exist"
            }, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        intern = self.get_intern_by_pk(pk)
        serializer = InternSerializer(intern)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        intern = self.get_intern_by_pk(pk)
        serializer = InternSerializer(intern, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        intern = self.get_intern_by_pk(pk)
        intern.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)