from django.db import models
from django.urls import reverse
from datetime import date 

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    habitat = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    conservation_status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def fed_for_today(self): 
        return self.feeding_set.filter(date=date.today()).count() == len(MEALS)


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        'feeding meal',
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    # Create a finch_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # get_meal_display where is it coming from 
        return f"{self.get_meal_display()} on {self.date}"
    
    # change the default sort
    class Meta:
      ordering = ['-date']

