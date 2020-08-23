from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from companies.models import Company, BranchCompany, BranchServices, Qualification
from companies.serializers import CompanySerializer, BranchCompanySerializer, BranchServicesSerializer, \
    QualificationSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, DjangoFilterBackend]


class BranchCompanyViewSet(viewsets.ModelViewSet):
    queryset = BranchCompany.objects.all()
    serializer_class = BranchCompanySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, DjangoFilterBackend, ]

class BranchServicesViewSet(viewsets.ModelViewSet):
    queryset = BranchServices.objects.all()
    serializer_class = BranchServicesSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, DjangoFilterBackend, ]

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, DjangoFilterBackend, ]