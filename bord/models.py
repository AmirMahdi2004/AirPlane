from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


# Create your models here.
class Airplane(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    airplane_name = models.CharField(max_length=100)
    ACreg = models.CharField(max_length=100)
    ACtype = models.CharField(max_length=100)
    ACSN = models.CharField(max_length=100)
    Date = models.DateField()
    ACTSN = models.IntegerField()
    ACCSN = models.IntegerField()
    LDNG = models.IntegerField()
    EngNo1Model = models.CharField(max_length=100)
    EngNo1SN = models.CharField(max_length=100)
    EngNo1TSN = models.IntegerField()
    EngNo1CSN = models.IntegerField()
    EngNo2Model = models.CharField(max_length=100)
    EngNo2SN = models.CharField(max_length=100)
    EngNo2TSN = models.IntegerField()
    EngNo2CSN = models.IntegerField()
    PropNo1Model = models.CharField(max_length=100)
    PropNo1SN = models.CharField(max_length=100)
    PropNo1TSN = models.IntegerField()
    PropNo1TSO = models.IntegerField()
    PropNo2Model = models.CharField(max_length=100)
    PropNo2SN = models.CharField(max_length=100)
    PropNo2TSN = models.IntegerField()
    PropNo2TSO = models.IntegerField()

    def get_sll_url(self):
        return reverse('bord:sll', args=[self.id])

    def get_mp_url(self):
        return reverse('bord:mp', args=[self.id])

    def get_flt_url(self):
        return reverse('bord:flt', args=[self.id])

    def __str__(self):
        return self.airplane_name


class ServiceLifeLimited(models.Model):
    IMPACT_CHOICES = (
        ('AircraftFlightHours', 'AircraftFlightHours'),
        ('AircraftCycles', 'AircraftCycles'),
        ('Landings', 'Landings'),
    )
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    No = models.IntegerField()
    TaskDescription = models.TextField()
    Source = models.TextField()
    PartNo = models.CharField(max_length=100, blank=True, null=True)
    SerialNo = models.CharField(max_length=100, blank=True, null=True)
    LDTime = models.IntegerField(blank=True, null=True)
    LDDate = models.DateField(blank=True, null=True)
    LDACCycle = models.IntegerField(blank=True, null=True)
    LDLDNG = models.IntegerField(blank=True, null=True)
    LDENC = models.CharField(max_length=100, blank=True, null=True)
    LTTime = models.IntegerField(blank=True, null=True)
    LTDate = models.DateField(blank=True, null=True)
    LTACCycle = models.IntegerField(blank=True, null=True)
    LTLDNG = models.IntegerField(blank=True, null=True)
    LTENC = models.CharField(max_length=100, blank=True, null=True)
    NDACTime = models.IntegerField(blank=True, null=True)
    NDDate = models.DateField(blank=True, null=True)
    NDACCycle = models.IntegerField(blank=True, null=True)
    NDLDNG = models.IntegerField(blank=True, null=True)
    NDENC = models.CharField(max_length=100, blank=True, null=True)
    RHours = models.IntegerField(blank=True, null=True)
    RDays = models.DateField(blank=True, null=True)
    RACCycle = models.IntegerField(blank=True, null=True)
    RLDNG = models.IntegerField(blank=True, null=True)
    RENC = models.CharField(max_length=100, blank=True, null=True)
    Description = models.CharField(max_length=100, blank=True, null=True)
    impact = models.CharField(max_length=100, choices=IMPACT_CHOICES, default='AircraftFlightHours')


class FltHrs(models.Model):
    IMPACT_CHOICES = (
        ('AircraftFlightHours', 'AircraftFlightHours'),
        ('AircraftCycles', 'AircraftCycles'),
        ('Landings', 'Landings'),
    )
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    Date = models.DateField()
    ACFltHrs = models.IntegerField()
    TotalACFItHrs = models.IntegerField()
    ACCyclesCSN = models.IntegerField()
    TotalACCyclesCSN = models.IntegerField()
    LDNG = models.IntegerField()
    TotalLDNG = models.IntegerField()
    EngNo1TimeTSN = models.IntegerField()
    TotalEngNo1TimeTSN = models.IntegerField()
    EngNo1CyclesCSN = models.IntegerField()
    TotalEngNo1CyclesCSN = models.IntegerField()
    EngNo2TimeTSN = models.IntegerField()
    TotalEngNo2TimeTSN = models.IntegerField()
    EngNo2CyclesCSN = models.IntegerField()
    TotalEngNo2CyclesCSN = models.IntegerField()
    PropNo1TimeTSN = models.IntegerField()
    TotalPropNo1TimeTSN = models.IntegerField()
    TotalPropNo1TimeTSO = models.IntegerField()
    PropNo2TimeTSN = models.IntegerField()
    TotalPropNo2TimeTSN = models.IntegerField()
    TotalPropNo2TimeTSO = models.IntegerField()
    impact = models.CharField(max_length=100, choices=IMPACT_CHOICES, default='AircraftFlightHours')


class MP(models.Model):
    IMPACT_CHOICES = (
        ('AircraftFlightHours', 'AircraftFlightHours'),
        ('AircraftCycles', 'AircraftCycles'),
        ('Landings', 'Landings'),
    )
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    No = models.CharField(max_length=20)
    Description = models.TextField()
    Source = models.TextField()
    INIHours = models.IntegerField(blank=True, null=True)
    INIDays = models.IntegerField(blank=True, null=True)
    INIACCycle = models.IntegerField(blank=True, null=True)
    INILDNG = models.IntegerField(blank=True, null=True)
    INTHours = models.IntegerField(blank=True, null=True)
    INTDays = models.IntegerField(blank=True, null=True)
    INTACCycle = models.IntegerField(blank=True, null=True)
    INTLDNG = models.IntegerField(blank=True, null=True)
    INTRENC = models.CharField(max_length=100, blank=True, null=True)
    LDHours = models.IntegerField(blank=True, null=True)
    LDDate = models.DateField(blank=True, null=True)
    LDACCycle = models.IntegerField(blank=True, null=True)
    LDLDNG = models.IntegerField(blank=True, null=True)
    LDENC = models.CharField(max_length=100, blank=True, null=True)
    NEACTime = models.IntegerField(blank=True, null=True)
    NEDate = models.DateField(blank=True, null=True)
    NEACCycle = models.IntegerField(blank=True, null=True)
    NELDNG = models.IntegerField(blank=True, null=True)
    NEENC = models.CharField(max_length=100, blank=True, null=True)
    REHours = models.IntegerField(blank=True, null=True)
    REDays = models.IntegerField(blank=True, null=True)
    REACCycle = models.IntegerField(blank=True, null=True)
    RELDNG = models.IntegerField(blank=True, null=True)
    REENC = models.CharField(max_length=100, blank=True, null=True)
    Remark = models.TextField(blank=True, null=True)
    impact = models.CharField(max_length=100, choices=IMPACT_CHOICES, default='AircraftFlightHours')


class InputBord(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    AircraftFlightHours = models.IntegerField()
    AircraftCycles = models.IntegerField()
    Landings = models.IntegerField()
