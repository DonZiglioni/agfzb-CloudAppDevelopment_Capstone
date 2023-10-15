from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    car_name = models.CharField(null=False, max_length=30, default='Honda')
    car_description = models.CharField(null=False, max_length=30, default='Sudan')
       
    # Create a toString method for object string representation
    def __str__(self):
        return self.car_name + " " + self.car_description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    car_name = models.CharField(null=False, max_length=30, default='Honda')
    car_type = models.CharField(null=False, max_length=30, default='SUV')
    car_year = models.DateField(null=False, default=2005)
    # Create a toString method for object string representation
    def __str__(self):
        return "Car Make: " + self.car_make + ", " + \
               "Dealer ID: " + str(self.dealer_id) + ", " + \
               "Car Name: " + self.car_name + ", " + \
               "Car Type: " + self.total_learners + ", " + \
               "Car Year: " + str(self.total_learners)
                
# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
