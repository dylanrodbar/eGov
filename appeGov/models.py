# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AppegovTabla1(models.Model):
    numero = models.IntegerField()
    letra = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'appegov_tabla1'


class AppegovTabla2(models.Model):
    numero2 = models.IntegerField()
    letra2 = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'appegov_tabla2'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fk_user = models.ForeignKey('User', models.DO_NOTHING, db_column='FK_User', blank=True, null=True)  # Field name made lowercase.
    fk_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='FK_Post', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Image(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='FK_Post', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'image'


class Lawproject(models.Model):
    fk_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='FK_Post', primary_key=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fk_stadistics = models.ForeignKey('Stadistic', models.DO_NOTHING, db_column='FK_Stadistics', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lawproject'


class Post(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    views = models.IntegerField(db_column='Views', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    fk_user = models.ForeignKey('User', models.DO_NOTHING, db_column='FK_User', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'post'


class Profilepicture(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profilepicture'


class Stadistic(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    yes = models.IntegerField(db_column='Yes', blank=True, null=True)  # Field name made lowercase.
    no = models.IntegerField(db_column='No', blank=True, null=True)  # Field name made lowercase.
    unknown = models.IntegerField(db_column='Unknown', blank=True, null=True)  # Field name made lowercase.
    fk_lawproject = models.ForeignKey(Lawproject, models.DO_NOTHING, db_column='FK_LawProject', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stadistic'


class Tag(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tag'


class Tagsxpost(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_post = models.ForeignKey(Post, models.DO_NOTHING, db_column='FK_Post', blank=True, null=True)  # Field name made lowercase.
    fk_tag = models.ForeignKey(Tag, models.DO_NOTHING, db_column='FK_Tag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tagsxpost'


class User(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=75, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=75, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200, blank=True, null=True)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', blank=True, null=True)  # Field name made lowercase.
    fk_tipousuario = models.ForeignKey('Usertype', models.DO_NOTHING, db_column='FK_TipoUsuario', blank=True, null=True)  # Field name made lowercase.
    fk_profilepicture = models.ForeignKey(Profilepicture, models.DO_NOTHING, db_column='FK_ProfilePicture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Usertype(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usertype'
