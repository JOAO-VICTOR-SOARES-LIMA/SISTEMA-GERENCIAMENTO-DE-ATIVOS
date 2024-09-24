from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import CargoSerializer, EntidadeLicencaSerializer, EntidadeDispositivoSerializer, EntidadeLicencaSerializer, LicencaSerializer, PerfilSerializer, PerfilDispositivoSerializer, SetorSerializer, TelefoniaSerializer, CampoAdicionalSerializer, CampoAdicionalTabelaSerializer, DepartamentoSerializer, DispositivoSerializer

from rest_framework import viewsets
from .models import Cargo, Entidade, EntidadeDispositivo, EntidadeLicenca, Licenca, Perfil, PerfilDispositivo, Setor, Telefonia, CampoAdicional, CampoAdicionalTabela, Departamento, Dispositivo
from .models import (
    CampoAdicional, CampoAdicionalTabela, Cargo, Departamento,
    Dispositivo, Entidade, EntidadeDispositivo, EntidadeLicenca, Licenca,
    Perfil, PerfilDispositivo, Setor, Telefonia, TipoLicenca
)
from .serializers import (
    CampoAdicionalSerializer, CampoAdicionalTabelaSerializer, CargoSerializer, 
    DepartamentoSerializer, DispositivoSerializer, EntidadeSerializer, 
    EntidadeDispositivoSerializer, EntidadeLicencaSerializer, LicencaSerializer, 
    PerfilSerializer, PerfilDispositivoSerializer, SetorSerializer, 
    TelefoniaSerializer, TipoLicencaSerializer
)

class CampoAdicionalViewSet(viewsets.ModelViewSet):
    queryset = CampoAdicional.objects.all()
    serializer_class = CampoAdicionalSerializer

class CampoAdicionalTabelaViewSet(viewsets.ModelViewSet):
    queryset = CampoAdicionalTabela.objects.all()
    serializer_class = CampoAdicionalTabelaSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class EntidadeViewSet(viewsets.ModelViewSet):
    queryset = Entidade.objects.all()
    serializer_class = EntidadeSerializer

class EntidadeDispositivoViewSet(viewsets.ModelViewSet):
    queryset = EntidadeDispositivo.objects.all()
    serializer_class = EntidadeDispositivoSerializer

class EntidadeLicencaViewSet(viewsets.ModelViewSet):
    queryset = EntidadeLicenca.objects.all()
    serializer_class = EntidadeLicencaSerializer

class LicencaViewSet(viewsets.ModelViewSet):
    queryset = Licenca.objects.all()
    serializer_class = LicencaSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilDispositivoViewSet(viewsets.ModelViewSet):
    queryset = PerfilDispositivo.objects.all()
    serializer_class = PerfilDispositivoSerializer

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

class TelefoniaViewSet(viewsets.ModelViewSet):
    queryset = Telefonia.objects.all()
    serializer_class = TelefoniaSerializer

class TipoLicencaViewSet(viewsets.ModelViewSet):
    queryset = TipoLicenca.objects.all()
    serializer_class = TipoLicencaSerializer





