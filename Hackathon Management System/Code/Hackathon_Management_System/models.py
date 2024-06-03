from django.db import models

class ParticipantModel(models.Model):
    part_id=models.BigIntegerField(primary_key=True)
    first_name=models.CharField(max_length=255, null=False)
    last_name=models.CharField(max_length=255,null=False)
    email_add=models.CharField(max_length=255, null=False)
    dob=models.DateField(null=False)
    student=models.CharField(max_length=255, null=False)
    college=models.CharField(max_length=255, null=False)
    cpi=models.FloatField(null=False)
    class Meta:
        db_table="participant"

class HackathonModel(models.Model):
    hack_id=models.BigIntegerField(primary_key=True)
    hack_name=models.CharField(max_length=255,null=False)
    name_type=models.CharField(max_length=255,null=False)
    date=models.DateField(null=False)
    time=models.TimeField(null=False)
    duration=models.BigIntegerField(null=False)
    class Meta:
        db_table="Hackathon"
