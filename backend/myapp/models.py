from django.db import models

# Create your models here.
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CampoAdicional(models.Model):
    nome_campo = models.CharField(max_length=255)
    tabela_origem = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'campo_adicional'


class CampoAdicionalTabela(models.Model):
    conteudo = models.CharField(max_length=255)
    id_campo_adicional = models.ForeignKey(CampoAdicional, models.DO_NOTHING, db_column='id_campo_adicional')

    class Meta:
        managed = False
        db_table = 'campo_adicional_tabela'


class Cargo(models.Model):
    nome = models.CharField(max_length=255)
    id_setor = models.ForeignKey('Setor', models.DO_NOTHING, db_column='id_setor')
    centro_custo = models.CharField(max_length=50)
    id_centro_de_custo = models.ForeignKey('CentroDeCusto', models.DO_NOTHING, db_column='id_centro_de_custo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'


class CentroDeCusto(models.Model):
    centro_de_custo = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centro_de_custo'


class Departamento(models.Model):
    nome = models.CharField(max_length=255)
    id_centro_de_custo = models.ForeignKey(CentroDeCusto, models.DO_NOTHING, db_column='id_centro_de_custo', blank=True, 
null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class Dispositivo(models.Model):
    nome = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    serial_numero = models.CharField(max_length=255)
    memoria = models.CharField(max_length=255)
    processador = models.CharField(max_length=255)
    data_compra = models.DateField()
    id_campo_adicional_tabela = models.ForeignKey(CampoAdicionalTabela, models.DO_NOTHING, db_column='id_campo_adicional_tabela')
    id_perfio_dispositivo = models.ForeignKey('PerfilDispositivo', models.DO_NOTHING, db_column='id_perfio_dispositivo')
    solucao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dispositivo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Entidade(models.Model):
    id_rh = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    id_perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='id_perfil')
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')
    id_telefonia = models.ForeignKey('Telefonia', models.DO_NOTHING, db_column='id_telefonia')
    campo_adicional = models.ForeignKey(CampoAdicionalTabela, models.DO_NOTHING, db_column='campo_adicional')
    situacao = models.CharField(max_length=255)
    id_campo_adcional_tabela = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'entidade'


class EntidadeDispositivo(models.Model):
    id_entidade = models.ForeignKey(Entidade, models.DO_NOTHING, db_column='id_entidade')
    id_dispositivo = models.ForeignKey(Dispositivo, models.DO_NOTHING, db_column='id_dispositivo')
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidade_dispositivo'


class EntidadeLicenca(models.Model):
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    id_licenca = models.ForeignKey('Licenca', models.DO_NOTHING, db_column='id_licenca')
    id_entidade = models.ForeignKey(Entidade, models.DO_NOTHING, db_column='id_entidade')

    class Meta:
        managed = False
        db_table = 'entidade_licenca'


class EntidadeProjeto(models.Model):
    id_entidade = models.ForeignKey(Entidade, models.DO_NOTHING, db_column='id_entidade', blank=True, null=True)
    id_projeto = models.ForeignKey('Projeto', models.DO_NOTHING, db_column='id_projeto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidade_projeto'


class Licenca(models.Model):
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    data_inicio_suporte = models.DateField(blank=True, null=True)
    qualidade = models.CharField(max_length=255, blank=True, null=True)
    id_entidade_licenca = models.IntegerField()
    part_number = models.CharField(max_length=255)
    situacao = models.CharField(max_length=255)
    id_tipo_licenca = models.ForeignKey('TipoLicenca', models.DO_NOTHING, db_column='id_tipo_licenca')
    id_campo_adicional_tabela = models.ForeignKey(CampoAdicionalTabela, models.DO_NOTHING, db_column='id_campo_adicional_tabela')

    class Meta:
        managed = False
        db_table = 'licenca'


class Perfil(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'perfil'


class PerfilDispositivo(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'perfil_dispositivo'


class Projeto(models.Model):
    numero_projeto = models.CharField(max_length=50, blank=True, null=True)
    id_centro_de_custo = models.ForeignKey(CentroDeCusto, models.DO_NOTHING, db_column='id_centro_de_custo', blank=True, 
null=True)

    class Meta:
        managed = False
        db_table = 'projeto'


class Setor(models.Model):
    nome = models.CharField(max_length=255)
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento')
    centro_de_custo = models.CharField(max_length=50, blank=True, null=True)
    id_centro_de_custo = models.ForeignKey(CentroDeCusto, models.DO_NOTHING, db_column='id_centro_de_custo', blank=True, 
null=True)

    class Meta:
        managed = False
        db_table = 'setor'


class Telefonia(models.Model):
    nome_operadora = models.CharField(max_length=255)
    nome_planonumero = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefonia'


class TipoLicenca(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_licenca'


class Usuario(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Vm(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    zona = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    disco = models.CharField(max_length=50, blank=True, null=True)
    vcpu = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    so = models.CharField(max_length=50, blank=True, null=True)
    rede = models.CharField(max_length=50, blank=True, null=True)
    ip_externo = models.CharField(max_length=50, blank=True, null=True)
    licenca = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    id_projeto = models.ForeignKey(Projeto, models.DO_NOTHING, db_column='id_projeto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vm'