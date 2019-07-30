# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Observer(models.Model):
    observerid = models.AutoField(db_column='observerID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'Observer'


class Coordinates(models.Model):
    coordinateid = models.AutoField(db_column='coordinateID', primary_key=True)  # Field name made lowercase.
    ra = models.FloatField(db_column='RA')  # Field name made lowercase.
    dec = models.FloatField(db_column='DEC')  # Field name made lowercase.
    coordinatesystem = models.CharField(db_column='coordinateSystem', max_length=64)  # Field name made lowercase.
    equinox = models.IntegerField()
    radesys = models.IntegerField()
    planetary = models.IntegerField()
    obsaz = models.FloatField()
    obsel = models.FloatField()
    raj2000 = models.FloatField(db_column='RAJ2000')  # Field name made lowercase.
    decj2000 = models.FloatField(db_column='DECJ2000')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coordinates'


class Error(models.Model):
    errorid = models.AutoField(db_column='errorID', primary_key=True)  # Field name made lowercase.
    errormsg = models.CharField(db_column='errorMsg', max_length=64)  # Field name made lowercase.
    severity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'error'


class File(models.Model):
    fileid = models.AutoField(db_column='fileID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=256)
    date = models.DateTimeField()
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'file'


class History(models.Model):
    historyid = models.AutoField(db_column='historyID', primary_key=True)  # Field name made lowercase.
    archivaldate = models.DateField(db_column='archivalDate')  # Field name made lowercase.
    aatfilename = models.CharField(db_column='aatFilename', max_length=256)  # Field name made lowercase.
    version = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'history'


class Obsparameter(models.Model):
    obsparameterid = models.AutoField(db_column='obsParameterID', primary_key=True)  # Field name made lowercase.
    backend = models.CharField(max_length=64)
    receiver = models.CharField(max_length=1024)
    nchan = models.CharField(max_length=1024)
    bandwidth = models.CharField(max_length=1024)
    velocity = models.FloatField()
    velocitydef = models.CharField(db_column='velocityDef', max_length=64)  # Field name made lowercase.
    restfreq = models.CharField(max_length=1024)
    poln = models.CharField(max_length=64)
    poln_num = models.CharField(max_length=64)
    mode = models.CharField(max_length=64)
    recband = models.CharField(db_column='recBand', max_length=12)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'obsParameter'


class Obsprocedure(models.Model):
    obsprocedureid = models.AutoField(db_column='obsProcedureID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    obstype = models.CharField(db_column='obsType', max_length=64)  # Field name made lowercase.
    procscan = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'obsProcedure'


class Project(models.Model):
    projectid = models.AutoField(db_column='projectID', primary_key=True)  # Field name made lowercase.
    propname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'project'


class Scan(models.Model):
    scanid = models.AutoField(db_column='scanID', primary_key=True)  # Field name made lowercase.
    number = models.IntegerField()
    object = models.CharField(max_length=64)
    obsidentifier = models.CharField(db_column='obsIdentifier', max_length=64)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    observerid = models.IntegerField(db_column='observerID')  # Field name made lowercase.
    obsprocedureid = models.IntegerField(db_column='obsProcedureID')  # Field name made lowercase.
    obsparameterid = models.IntegerField(db_column='obsParameterID')  # Field name made lowercase.
    coordinateid = models.IntegerField(db_column='coordinateID')  # Field name made lowercase.
    errorid = models.IntegerField(db_column='errorID')  # Field name made lowercase.
    historyid = models.IntegerField(db_column='historyID')  # Field name made lowercase.
    fileid = models.IntegerField(db_column='fileID')  # Field name made lowercase.
    sessionid = models.IntegerField(db_column='sessionID')  # Field name made lowercase.
    dateobserved = models.DateTimeField(db_column='dateObserved')  # Field name made lowercase.
    integrationtime = models.FloatField(db_column='integrationTime')  # Field name made lowercase.
    scanlength = models.IntegerField()
    archived = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scan'


class Session(models.Model):
    sessionid = models.AutoField(db_column='sessionID', primary_key=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    name = models.CharField(max_length=64)
    gofitsversion = models.CharField(db_column='GOFitsVersion', max_length=64)  # Field name made lowercase.
    msgflag = models.CharField(db_column='MSGFLAG', max_length=1024)  # Field name made lowercase.
    msglevel = models.CharField(db_column='MSGLEVEL', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'session'


class TestOfflineOld(models.Model):
    errorid = models.AutoField(db_column='errorID', primary_key=True)  # Field name made lowercase.
    errormsg = models.CharField(db_column='errorMsg', max_length=64)  # Field name made lowercase.
    severity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test_offline_old'
