from django.db  import models
# myapp/models
class Animal(models.Model):
    TYPE_CHOICES = [
        ('cow', 'Cow'),
        ('goat', 'Goat'),
        ('camel', 'Camel'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    REMOVAL_REASON_CHOICES = [
        ('sold', 'Sold'),
        ('death', 'Death'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    tag_number = models.CharField(max_length=50, unique=True)
    removal_reason = models.CharField(max_length=50, null=True, blank=True)
    sold_date = models.DateField(null=[True], blank=True)
    death_date = models.DateField(null=[True], blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    
    def __str__(self):
        return f"{self.type} - {self.tag_number}"







