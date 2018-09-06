from django.db import models


# Create your models here.

#Choice definitions
MALE = 'M'
FEMALE = 'F'
OTHER = 'O'
SEX_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
)
A_TYPE = 'A'
B_TYPE = 'B'
AB_TYPE = 'AB'
O_TYPE = 'O'
BLOOD_GROUP_CHOICES = (
    (A_TYPE, 'A'),
    (B_TYPE, 'B'),
    (AB_TYPE, 'AB'),
    (O_TYPE, 'O'),
)
POSITIVE = '+'
NEGATIVE = '-'
RH_CHOICES = (
    (POSITIVE, 'Positive'),
    (NEGATIVE, 'Negative'),
)



class Patient(models.Model):
    """Model representing the Patient"""
    date_of_entry = models.DateField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=400)
    sex = models.CharField(
        max_length = 1,
        choices = SEX_CHOICES,
        default = MALE,
    )
    blood_group = models.CharField(
        max_length=2,
        choices = BLOOD_GROUP_CHOICES,
        default = A_TYPE,
    )
    blood_rh = models.CharField(
        max_length =1,
        choices = RH_CHOICES,
        default = POSITIVE,
    )
    remarks = models.TextField()
    def __str__(self):
        """String to represent the object"""
        return f'{self.first_name} {self.last_name}'

class Donor(models.Model):
    """Model representing the Donor"""
    #Choice definitions
    

    #Field definitions
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    date_of_birth = models.DateField()
    sex = models.CharField(
        max_length = 1,
        choices = SEX_CHOICES,
        default = MALE,
    )
    blood_group = models.CharField(
        max_length=2,
        choices = BLOOD_GROUP_CHOICES,
        default = A_TYPE,
    )
    blood_rh = models.CharField(
        max_length =1,
        choices = RH_CHOICES,
        default = POSITIVE,
    )


    def __str__(self):
        """String to represent the object"""
        return f'{self.first_name} {self.last_name}'

class Donation(models.Model):
    """Model representing the donation of blood"""
    #Choice definitions
    BLOOD_BAG_TYPE_CHOICES = (
        ('Single 350', 'Single 350'),
        ('Single 450', 'Single 450'),
        ('Double 350', 'Double 350'),
        ('Double 450', 'Double 450'),
        ('Triple 350', 'Triple 350'),
        ('Triple 450', 'Triple 450'),
        ('Segum 450', 'Segum 450'),
        ('Segum 450', 'Segum 450'),
    )
    TYPE_OF_DONATION_CHOICES = (
        ('VOL', 'Voluntary'),
        ('REP', 'Replacement'),
    )
    
    #Field definitions
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    date_of_bleeding = models.DateField()
    segment_number = models.CharField(max_length=10)
    blood_bag_type = models.CharField(
        max_length = 20,
        choices = BLOOD_BAG_TYPE_CHOICES,
        default = 'Single 350'
    )
    quantity = models.IntegerField()
    type_of_donation = models.CharField(
        max_length = 3,
        choices = TYPE_OF_DONATION_CHOICES,
        default = 'VOL'
    )
    hb_gram_percent = models.FloatField()
    weight = models.FloatField()
    blood_pressure = models.FloatField()
    pulse = models.FloatField()
    temperature = models.FloatField()
    replaced_for = models.ForeignKey(Patient, blank=True, null=True, on_delete=models.SET_NULL)
    remarks = models.TextField()

    def __str__(self):
        """String to represent the object"""
        return f'{self.donor} : {self.blood_bag_type}, {self.quantity} ml'


class Serology(models.Model):
    """Model representing the donation of blood"""
    date_time = models.DateTimeField()
    donation = models.ForeignKey(Donation, null=True, on_delete=models.SET_NULL)
    hiv = models.NullBooleanField()
    hbsag = models.NullBooleanField()
    hcv = models.NullBooleanField()
    vdrl = models.NullBooleanField()
    mp = models.NullBooleanField()
    def __str__(self):
        """String to represent the object"""
        return f'{self.donation}'
