from .models import Club, Candidate
from .serializers import ClubSerializer, CandidateSerializer
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView 

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Club.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()

#         return Response(self.get_serializer(user).data, status=status.HTTP_201_CREATED)


    
class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save the user instance
        refresh = RefreshToken.for_user(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# class CandidateViewSet(viewsets.ModelViewSet):
#     queryset = Candidate.objects.all()
#     serializer_class = CandidateSerializer


# class ClubRegistrationView(CreateAPIView):
#     serializer_class = ClubSerializer
#     permission_classes = [AllowAny]
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         club = serializer.save()  # Save the user instance
#         # Generate token
#         refresh = RefreshToken.for_user(club)

#         data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
#         return Response(data, status=status.HTTP_200_OK)