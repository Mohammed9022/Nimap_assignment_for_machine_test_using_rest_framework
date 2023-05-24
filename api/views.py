from rest_framework import generics
from .serializers import UserSerializer,ClientSerializer, ProjectSerializer
from .models import Client,Project,User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# API for creating clients.
class ClientCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer

    #Function to fetch all the clients info 
    def get_queryset(self):
        return Client.objects.all()
    
    def perform_create(self, serializer):
       serializer.save(created_by=self.request.user)


# API for retrieve all the clients information.
class ClientInfoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()
    

#For Edit the client info
class UpdateClientView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

# another way of doing the delete task
# class DeleteClientView(APIView):
#     def delete(self,request, id=None):
#         client_data = Client.objects.get(id=id)
#         client_data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class DeleteClientView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    lookup_url_kwarg = 'id'
    queryset = Client.objects.all()


# API for creating a new project
class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer

    #Function for create a project
    def perform_create(self,serializer):
        client_id = self.kwargs.get('client_id') # To fetch client id
        client = Client.objects.get(pk=client_id)
        serializer.save(client=client, created_by=self.request.user)

# For another way of doing retrieve. 
# class ProjectDetailView(generics.RetrieveAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# For project details
class ProjectDetailView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)


# For deatils of projects assigned to the clients.
class ClientWithProjectDetail(generics.RetrieveAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()
    
    def retrieve(self):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        projects_serializer = ProjectSerializer(instance.project_set.all(), many=True)
        data = serializer.data
        data['projects'] = projects_serializer.data
        return Response(data)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    