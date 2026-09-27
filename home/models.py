from django.db import models


class GenderOption(models.TextChoices):
    MALE = 'MALE', 'Male',
    FEMALE = 'FEMALE', 'Female'


class TransportOption(models.TextChoices):
    YES = 'YES', 'Yes',
    NO = 'NO', 'No'


class NIGERIAN_STATES(models.TextChoices):

    AB = 'AB', 'Abia',
    AD = 'AD', 'Adamawa',
    AK = 'AK', 'Akwa Ibom',
    AN = 'AN', 'Anambra',
    BA = 'BA', 'Bauchi',
    BY = 'BY', 'Bayelsa',
    BE = 'BE', 'Benue',
    BO = 'BO', 'Borno',
    CR = 'CR', 'Cross River',
    DE = 'DE', 'Delta',
    EB = 'EB', 'Ebonyi',
    ED = 'ED', 'Edo',
    EK = 'EK', 'Ekiti',
    EN = 'EN', 'Enugu',
    FC = 'FC', 'Federal Capital Territory',
    GO = 'GO', 'Gombe',
    IM = 'IM', 'Imo',
    JI = 'JI', 'Jigawa',
    KD = 'KD', 'Kaduna',
    KN = 'KN', 'Kano',
    KT = 'KT', 'Katsina',
    KE = 'KE', 'Kebbi',
    KO = 'KO', 'Kogi',
    KW = 'KW', 'Kwara',
    LA = 'LA', 'Lagos',
    NA = 'NA', 'Nasarawa',
    NI = 'NI', 'Niger',
    OG = 'OG', 'Ogun',
    ON = 'ON', 'Ondo',
    OS = 'OS', 'Osun',
    OY = 'OY', 'Oyo',
    PL = 'PL', 'Plateau',
    RI = 'RI', 'Rivers',
    SO = 'SO', 'Sokoto',
    TA = 'TA', 'Taraba',
    YO = 'YO', 'Yobe',
    ZA = 'ZA', 'Zamfara',


class Enquiry(models.Model):

    # Parent / Guardian
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Student
    student_first_name = models.CharField(max_length=255)
    student_last_name = models.CharField(max_length=255)
    student_age = models.DateField()

    gender = models.CharField(
        max_length=20,
        choices=GenderOption.choices,
        default=GenderOption.MALE
    )

    # Enquiry
    details = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student_first_name}"


class Apply(models.Model):
    # student BIO Data
    student_name = models.CharField(blank=False, max_length=255)
    student_lastname = models.CharField(blank=False, max_length=255)
    student_email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(blank=False)
    language_spoken_at_home = models.CharField()
    nationality = models.CharField(blank=False)
    state_of_origin = models.CharField(
        choices=NIGERIAN_STATES.choices, max_length=2)
    gender = models.CharField(
        choices=GenderOption.choices, default=GenderOption.MALE)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    family_size = models.IntegerField()
    name_of_last_school = models.CharField()
    last_school_startdate = models.DateField()
    last_school_enddate = models.DateField()
    position_in_last_school = models.CharField()
    reason_for_leaving = models.CharField()
    class_expexting_admission = models.CharField(blank=False)
    transport_service = models.CharField(
        choices=TransportOption.choices, default=TransportOption.NO)
    any_certificate = models.CharField(max_length=255)

    # Medical Report
    vision = models.CharField()
    hearing = models.CharField()
    speech = models.CharField()
    general_vitality = models.CharField()
    disability = models.CharField()

    # Parent Data(Father)
    father_title = models.CharField(blank=True,)
    father_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    office_address = models.CharField()
    home_address = models.CharField()
    father_phone = models.IntegerField()
    father_email = models.EmailField()

    # parent Data(Mother)
    mother_title = models.CharField()
    mother_name = models.CharField(max_length=255)
    mo_occupation = models.CharField(max_length=255)
    mo_office_address = models.CharField()
    mo_home_address = models.CharField()
    mother_phone = models.IntegerField()
    mother_email = models.EmailField()

    # Guardian Data
    gd_title = models.CharField()
    gd_name = models.CharField(max_length=255)
    gd_occupation = models.CharField(max_length=255)
    gd_office_address = models.CharField()
    gd_home_address = models.CharField()
    gd_phone = models.IntegerField()
    gd_email = models.EmailField()

    def __str__(self):
        return self.student_name, self.student_lastname,


class Stories(models.Model):
    img = models.ImageField(
        upload_to='stories_img/',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    parent_name = models.CharField(max_length=100)

    def __str__(self):
        return self.parent_name


class Gallery(models.Model):

    img = models.ImageField(
        upload_to='gallery/',
        null=True,
        blank=True
    )




