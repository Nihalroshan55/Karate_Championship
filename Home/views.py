from .models import Club, Candidate
from .serializers import ClubSerializer, CandidateSerializer, UserSerializer
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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(self.get_serializer(user).data, status=status.HTTP_201_CREATED)
    
class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer



class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)

    #     # Extract the values of kumite and kata from the request data
    #     kumite = serializer.validated_data.get('kumite', instance.kumite)
    #     kata = serializer.validated_data.get('kata', instance.kata)

    #     old_entry_fee = instance.entry_fee

    #     # Recalculate entry fee based on kumite and kata
    #     entry_fee = self.calculate_entry_fee(kumite, kata)
        
    #     instance.club.fees -=old_entry_fee
    #     instance.club.fees +=entry_fee
    #     # Update the instance and save
    #     serializer.save(entry_fee=entry_fee)
    #     instance.club.save()

        
    #     # Update the corresponding Club's fees
    #     # if instance.club:
    #     #     difference = entry_fee - old_entry_fee
    #     #     if difference:
    #     #         print(difference,"inside > 0")
                
    #     #         instance.club.fees += difference

    #         # elif difference < 0:
    #         #     print(difference,"inside < 0")

    #         #     instance.club.fees += difference
                

    #     return Response(serializer.data)

    # def calculate_entry_fee(self, kumite, kata):
    #     if (kata and not kumite) or (kumite and not kata):
    #         return 1000
    #     else:
    #         return 1500
