from django.urls import path, include
from dataview import views
from dataview.models import Patient, Donor, Donation
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include



class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('url', 'first_name', 'last_name', 'telephone', 'date_of_birth', 
        'address', 'sex', 'blood_group', 'blood_rh', 'remarks')

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        fields = ('url', 'first_name', 'last_name', 'address', 'date_of_birth', 
        'sex', 'blood_group', 'blood_rh')

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'donors', DonorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
]