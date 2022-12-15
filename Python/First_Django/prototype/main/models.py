# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Model(models.Model):
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tooltype = models.CharField(db_column='Tooltype', max_length=255, blank=True, null=True)  # Field name made lowercase.
    excel = models.CharField(db_column='Excel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(max_length=255, blank=True, null=True)
    point = models.CharField(db_column='Point', max_length=255, blank=True, null=True)  # Field name made lowercase.
    toolname = models.CharField(db_column='Toolname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shift = models.CharField(max_length=255, blank=True, null=True)
    machine_line = models.CharField(db_column='Machine_Line', max_length=250, blank=True, null=True)  # Field name made lowercase.
    machine_no = models.CharField(db_column='Machine_No', max_length=250, blank=True, null=True)  # Field name made lowercase.
    machine_process = models.CharField(db_column='Machine_Process', max_length=250, blank=True, null=True)  # Field name made lowercase.
    processname = models.CharField(db_column='Processname', max_length=250, blank=True, null=True)  # Field name made lowercase.
    partname = models.CharField(db_column='Partname', max_length=250, blank=True, null=True)  # Field name made lowercase.
    wid = models.AutoField(primary_key=True)
    point_no = models.FloatField(db_column='Point_No', blank=True, null=True)  # Field name made lowercase.
    sheet = models.TextField(db_column='Sheet', blank=True, null=True)  # Field name made lowercase.
    min = models.FloatField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    max = models.FloatField(db_column='Max', blank=True, null=True)  # Field name made lowercase.
    wi = models.IntegerField(blank=True, null=True)
    pattern=models.CharField(max_length=255,blank=True, null=True)
    cstart = models.IntegerField(db_column='Cstart', blank=True, null=True)  # Field name made lowercase.
    rstart = models.IntegerField(db_column='Rstart', blank=True, null=True)  # Field name made lowercase.
    # def __str__(self) :
    #     return (self.model,self.partname)
    class Meta:
        managed = True
        db_table = 'Model'


class Tool(models.Model):
    tid = models.AutoField(primary_key=True)
    toolname = models.CharField(db_column='Toolname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ttid = models.IntegerField(blank=True, null=True)
    tooltype = models.CharField(db_column='Tooltype', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tool'


class Toollist(models.Model):
    tid = models.CharField(max_length=255, blank=True, null=True)
    codename = models.CharField(db_column='CodeName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True 
        db_table = 'Tool_'


class Tooltype(models.Model):
    ttid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tooltype'


class Work(models.Model):
    man = models.CharField(db_column='Man', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timein = models.CharField(db_column='Timein', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timeout = models.CharField(db_column='Timeout', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', max_length=255, blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    wid = models.IntegerField(blank=True, null=True)
    result = models.CharField(db_column='Result', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shift = models.CharField(max_length=255, blank=True, null=True)
    partno = models.CharField(db_column='PartNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    point = models.CharField(db_column='Point', max_length=255, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)  # Field name made lowercase.
    machine_process = models.CharField(db_column='MachineProcess', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processname = models.CharField(db_column='Processname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    machine_line = models.CharField(db_column='Machine_Line', max_length=255, blank=True, null=True)  # Field name made lowercase.
    machine_no = models.CharField(db_column='Machine_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    point_no = models.CharField(db_column='Point_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    toolname = models.CharField(db_column='Toolname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result_gonogo = models.CharField(db_column='Result_gonogo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    partname = models.TextField(db_column='Partname', blank=True, null=True)  # Field name made lowercase.
    rid = models.AutoField(primary_key=True)
    max = models.FloatField(db_column='Max', blank=True, null=True)  # Field name made lowercase.
    min = models.FloatField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    wi = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'Work'
        
class Pattern(models.Model):
    pattern_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255, blank=False, null=False)
    direction=models.CharField( max_length=255, blank=False, null=False)
    cstart = models.IntegerField(  blank=True, null=True)  # Field name made lowercase.
    rstart = models.IntegerField(  blank=True, null=True)  # Field name made lowercase.
    interval=models.IntegerField( blank=True, null=True)
    num_shift=models.IntegerField(  blank=True, null=True)
    name_shift=models.CharField( max_length=20, blank=True, null=True)
    shift_type=models.CharField( max_length=20, blank=True, null=True)
    timestart=models.CharField( max_length=20, blank=True, null=True)
    timeend=models.CharField( max_length=20, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'Pattern'
        

