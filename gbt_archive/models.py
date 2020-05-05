"""Models!"""
from pathlib import Path
import re
import glob

from django.db import models
from django.urls import reverse

from gbt_archive.utils import get_archive_path

class Observer(models.Model):
    observerid = models.AutoField(db_column="observerID", primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = "Observer"

    def __str__(self):
        return f"{self.name}"


class Coordinates(models.Model):
    coordinateid = models.AutoField(db_column="coordinateID", primary_key=True)
    ra = models.FloatField(db_column="RA")
    dec = models.FloatField(db_column="DEC")
    coordinatesystem = models.CharField(
        db_column="coordinateSystem",
        max_length=64,
        blank=True,
        choices=(
            ("RADEC", "RADEC"),
            ("OTHER", "OTHER"),
            ("GALACTIC", "GALACTIC"),
            ("AZEL", "AZEL"),
            ("HADEC", "HADEC"),
            ("ENCODERAZEL", "ENCODERAZEL"),
            ("", "Blank"),
        ),
    )
    # TODO: Always 0; delete?
    equinox = models.IntegerField()
    # TODO: Always 0; delete?
    radesys = models.IntegerField()
    # TODO: Always 0; delete?
    planetary = models.IntegerField()
    # Used
    obsaz = models.FloatField()
    # Used
    obsel = models.FloatField()
    # Used
    raj2000 = models.FloatField(db_column="RAJ2000")
    # Used
    decj2000 = models.FloatField(db_column="DECJ2000")

    class Meta:
        managed = False
        db_table = "coordinates"


class Error(models.Model):
    errorid = models.AutoField(db_column="errorID", primary_key=True)
    errormsg = models.CharField(db_column="errorMsg", max_length=64)
    severity = models.IntegerField()

    class Meta:
        managed = False
        db_table = "error"

    def __str__(self):
        return f"{self.severity}: {self.errormsg}"


class File(models.Model):
    fileid = models.AutoField(db_column="fileID", primary_key=True)
    name = models.CharField(max_length=256)
    date = models.DateTimeField()
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = "file"

    def __str__(self):
        return f"{self.name}"


class History(models.Model):
    """Stores history of CSV exports, intended for AAT consumption"""

    historyid = models.AutoField(db_column="historyID", primary_key=True)
    archivaldate = models.DateField(db_column="archivalDate")
    aatfilename = models.CharField(db_column="aatFilename", max_length=256)
    version = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = "history"
        verbose_name_plural = "Histories"


class ObsParameter(models.Model):
    obsparameterid = models.AutoField(db_column="obsParameterID", primary_key=True)
    backend = models.CharField(
        max_length=64,
        choices=(
            ("", "UNKNOWN"),
            ("CCB26_40", "CCB26_40"),
            ("DCR", "DCR"),
            ("DCR, CCB26_40", "DCR, CCB26_40"),
            ("DCR, SpectralProcessor", "DCR, SpectralProcessor"),
            ("DCR, Spectrometer", "DCR, Spectrometer"),
            ("GUPPI", "GUPPI"),
            ("MUSTANG", "MUSTANG"),
            ("SpectralProcessor", "SpectralProcessor"),
            ("SpectralProcessor, CCB26_40", "SpectralProcessor, CCB26_40"),
            ("SpectralProcessor, DCR", "SpectralProcessor, DCR"),
            ("Spectrometer", "Spectrometer"),
            ("Spectrometer, DCR", "Spectrometer, DCR"),
            ("Spectrometer, SpectralProcessor", "Spectrometer, SpectralProcessor"),
            ("SPIGOT", "SPIGOT"),
            ("VEGAS", "VEGAS"),
            ("VLBA_DAR", "VLBA_DAR"),
            ("Zpectrometer", "Zpectrometer"),
        ),
    )
    receiver = models.CharField(
        max_length=1024,
        blank=True,
        choices=(
            ("", "UNKNOWN"),
            ("Holography", "Holography"),
            ("Rcvr12_18", "Rcvr12_18"),
            ("Rcvr18_26", "Rcvr18_26"),
            ("Rcvr1_2", "Rcvr1_2"),
            ("Rcvr26_40", "Rcvr26_40"),
            ("Rcvr2_3", "Rcvr2_3"),
            ("Rcvr40_52", "Rcvr40_52"),
            ("Rcvr4_6", "Rcvr4_6"),
            ("Rcvr68_92", "Rcvr68_92"),
            ("Rcvr8_10", "Rcvr8_10"),
            ("Rcvr_342", "Rcvr_342"),
            ("Rcvr_800", "Rcvr_800"),
            ("Rcvr_PAR", "Rcvr_PAR"),
            ("RcvrArray18_26", "RcvrArray18_26"),
            ("RcvrPF_1", "RcvrPF_1"),
            ("RcvrPF_2", "RcvrPF_2"),
        ),
    )
    nchan = models.CharField(max_length=1024)
    bandwidth = models.CharField(max_length=1024)
    velocity = models.FloatField()
    velocitydef = models.CharField(db_column="velocityDef", max_length=64)
    restfreq = models.CharField(max_length=1024)
    poln = models.CharField(
        max_length=64,
        blank=True,
        choices=(
            ("XX,YY", "XX,YY"),
            ("", "Blank"),
            ("LL,RR", "LL,RR"),
            ("LL,RR,LR,RL", "LL,RR,LR,RL"),
            ("XX,YY,XY,YX", "XX,YY,XY,YX"),
            ("UNKNOWN", "UNKNOWN"),
            ("LL", "LL"),
            ("I", "I"),
            ("I,Q,U,V", "I,Q,U,V"),
        ),
    )
    poln_num = models.CharField(max_length=64)
    mode = models.CharField(max_length=64)
    recband = models.CharField(
        db_column="recBand",
        max_length=12,
        choices=(
            ("L", "L"),
            ("Unknown", "Unknown"),
            ("X", "X"),
            ("C", "C"),
            ("K", "K"),
            ("U", "U"),
            ("P", "P"),
            ("S", "S"),
            ("Q", "Q"),
            ("Ka", "Ka"),
            ("W", "W"),
        ),
    )

    class Meta:
        managed = False
        db_table = "obsParameter"
        verbose_name = "Obs. Parameter"

    def __str__(self):
        return f"{self.backend if self.backend else 'UNKNOWN'} : {self.receiver if self.receiver else 'UNKNOWN'}"


class ObsProcedure(models.Model):
    obsprocedureid = models.AutoField(db_column="obsProcedureID", primary_key=True)
    name = models.CharField(max_length=64)
    type = models.CharField(
        max_length=64,
        choices=(
            ("POINTING", "POINTING"),
            ("SIMPLE", "SIMPLE"),
            ("CALIBRATION", "CALIBRATION"),
            ("MAP", "MAP"),
            ("UNKNOWN", "UNKNOWN"),
            ("OOFMAP", "OOFMAP"),
        ),
    )
    obstype = models.CharField(
        db_column="obsType",
        max_length=64,
        choices=[
            ("CONTINUUM", "CONTINUUM"),
            ("LINE", "LINE"),
            ("PTIMING", "PTIMING"),
            ("UNKNOWN", "UNKNOWN"),
            ("PSEARCH", "PSEARCH"),
            ("PMONITOR", "PMONITOR"),
            ("Radar", "Radar"),
            ("Pulsar", "Pulsar"),
            ("VLBI", "VLBI"),
            ("PCAL", "PCAL"),
        ],
    )
    procscan = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = "obsProcedure"
        verbose_name = "Obs. Procedure"

    def __str__(self):
        return f"{self.name} ({self.type}/{self.obstype})"


class Project(models.Model):
    projectid = models.AutoField(db_column="projectID", primary_key=True)
    # Not unique
    propname = models.CharField(max_length=64)
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        managed = False
        db_table = "project"

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("project_detail", args=[str(self.pk)])


class Scan(models.Model):
    scanid = models.AutoField(db_column="scanID", primary_key=True)
    number = models.IntegerField()
    object = models.CharField(max_length=64)
    obsidentifier = models.CharField(db_column="obsIdentifier", max_length=64)
    project = models.ForeignKey(
        "Project", db_column="projectID", on_delete=models.CASCADE, related_name="scans"
    )
    observer = models.ForeignKey(
        "Observer",
        db_column="observerID",
        on_delete=models.CASCADE,
        related_name="scans",
    )
    obsprocedure = models.ForeignKey(
        "ObsProcedure",
        db_column="obsProcedureID",
        on_delete=models.CASCADE,
        related_name="scans",
    )
    obsparameter = models.ForeignKey(
        "ObsParameter",
        db_column="obsParameterID",
        on_delete=models.CASCADE,
        related_name="scans",
    )
    coordinate = models.ForeignKey(
        "Coordinates",
        db_column="coordinateID",
        on_delete=models.CASCADE,
        related_name="scans",
    )
    # NOTE: 0 is used as NULL here
    error = models.ForeignKey(
        "Error", db_column="errorID", on_delete=models.CASCADE, related_name="scans"
    )
    history = models.ForeignKey(
        "History", db_column="historyID", on_delete=models.CASCADE, related_name="scans"
    )
    file = models.OneToOneField(
        "File", db_column="fileID", on_delete=models.CASCADE, related_name="scans"
    )
    session = models.ForeignKey(
        "Session", db_column="sessionID", on_delete=models.CASCADE, related_name="scans"
    )
    dateobserved = models.DateTimeField(db_column="dateObserved")
    integrationtime = models.FloatField(db_column="integrationTime")
    scanlength = models.IntegerField()
    archived = models.IntegerField()

    class Meta:
        managed = False
        db_table = "scan"

    def __str__(self):
        return (
            f"Scan {self.number} of '{self.obsidentifier}' "
            f"('{self.object}') [{self.scanlength}s]"
        )


class Session(models.Model):
    sessionid = models.AutoField(db_column="sessionID", primary_key=True)
    project = models.ForeignKey(
        "Project",
        db_column="projectID",
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    name = models.CharField(max_length=64)
    gofitsversion = models.CharField(db_column="GOFitsVersion", max_length=64)
    msgflag = models.CharField(db_column="MSGFLAG", max_length=1024)
    msglevel = models.CharField(db_column="MSGLEVEL", max_length=4)

    class Meta:
        managed = False
        db_table = "session"

    def __str__(self):
        return f"Session {self.name}"

    def get_data_path(self):
        return get_archive_path(self.project.name, self.name)

# class TestOfflineOld(models.Model):
#     errorid = models.AutoField(db_column="errorID", primary_key=True)
#     errormsg = models.CharField(db_column="errorMsg", max_length=64)
#     severity = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = "test_offline_old"
