from rest_framework import serializers
from .models import (
    CampoAdicional, CampoAdicionalTabela, Cargo, Departamento,
    Dispositivo, Entidade, EntidadeDispositivo, EntidadeLicenca, Licenca,
    Perfil, PerfilDispositivo, Setor, Telefonia, TipoLicenca
)

class CampoAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoAdicional
        fields = '__all__'

class CampoAdicionalTabelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoAdicionalTabela
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class EntidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidade
        fields = '__all__'

class EntidadeDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadeDispositivo
        fields = '__all__'

class EntidadeLicencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadeLicenca
        fields = '__all__'

class LicencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenca
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class PerfilDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilDispositivo
        fields = '__all__'

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

class TelefoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefonia
        fields = '__all__'

class TipoLicencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLicenca
        fields = '__all__'


