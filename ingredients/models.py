from django.db import models

# Category model 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Ingredients model
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(Category, related_name="ingredients", on_delete=models.CASCADE)

    def __str__(self):
        return self.name