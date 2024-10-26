# from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from .permissions import IsOwnerOrReadOnly


# view for handling project listing creation
class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        # get all open projects
        projects = Project.objects.filter(is_open=True)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
        
        
    def post(self, request):
        # only logged-in users can create a project
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# view for handling specific project details, updates, deletion       
class ProjectDetail(APIView):
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request,project)
            return project
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project,
            data=request.data, partial=True)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# view for handling pledges
class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(request, pledge)
            serializer = PledgeSerializer(pledge, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pledge.DoesNotExist:
            return Response({"error": "Pledge not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            pledge.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pledge.DoesNotExist:
            return Response({"error": "Pledge not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request):
        pledges = Pledge.objects.filter(supporter=request.user)  # Filter pledges by the authenticated user
        serializer = PledgeSerializer(pledges, many=True)  # Serialize the list of pledges
        return Response(serializer.data, status=status.HTTP_200_OK)

 
        
########## V1 ##########

# view for handling project listing creation
# class ProjectList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
#     def get(self, request):
#         # get all open projects
#         projects = Project.objects.filter(is_open=True)
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)
        
        
#     def post(self, request):
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             # serializer.save()
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, 
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
        
# class ProjectDetail(APIView):
    
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly
#     ]
    
#     def get_object(self, pk):
#         try:
#             project = Project.objects.get(pk=pk)
#             self.check_object_permissions(self.request,project)
#             return project
#         except Project.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         project = self.get_object(pk)
#         # serializer = ProjectSerializer(project)
#         serializer = ProjectDetailSerializer(project)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         project = self.get_object(pk)
#         serializer = ProjectDetailSerializer(
#             instance=project,
#             data=request.data,
#             partial=True
#         )
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
    
# class PledgeList(APIView):
    
#     def get(self, request):
#         pledges = Pledge.objects.all()
#         serializer = PledgeSerializer(pledges, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PledgeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
 
        

