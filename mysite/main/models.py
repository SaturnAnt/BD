# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'area'


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


class Cementing(models.Model):
    id_cementing = models.AutoField(primary_key=True)
    column = models.ForeignKey('Columns', models.DO_NOTHING)
    well = models.ForeignKey('Well', models.DO_NOTHING)
    cementing_quality = models.CharField(max_length=20, blank=True, null=True)
    cementing_start_date = models.DateField()
    cementing_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cementing'


class Columns(models.Model):
    id_column = models.AutoField(primary_key=True)
    type_column = models.CharField(max_length=20)
    date_installation = models.DateField()
    external_diameter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'columns'


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


class DownholeEquipment(models.Model):
    id_equipment = models.AutoField(primary_key=True)
    type_equipment = models.CharField(max_length=20)
    inner_diameter = models.IntegerField(blank=True, null=True)
    external_diameter = models.IntegerField(blank=True, null=True)
    well = models.ForeignKey('Well', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'downhole_equipment'


class Perforation(models.Model):
    id_perforation = models.AutoField(primary_key=True)
    well = models.ForeignKey('Well', models.DO_NOTHING)
    сreation_date = models.DateField()
    perforation_densityint = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perforation'


class Tubing(models.Model):
    id_tubing = models.AutoField(primary_key=True)
    well = models.ForeignKey('Well', models.DO_NOTHING)
    descent_date = models.DateField()
    rise_date = models.DateField(blank=True, null=True)
    inner_diameter = models.IntegerField(blank=True, null=True)
    external_diameter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tubing'


class Well(models.Model):
    id_well = models.AutoField(primary_key=True)
    date_start = models.DateField()
    wellhead_coordinate_y = models.IntegerField(db_column='wellhead_coordinate_Y')  # Field name made lowercase.
    wellhead_coordinate_x = models.IntegerField(db_column='wellhead_coordinate_X')  # Field name made lowercase.
    altitude = models.IntegerField()
    area = models.ForeignKey(Area, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'well'