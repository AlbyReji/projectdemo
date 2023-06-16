from django.db import models

# Create your models here.

class emp(models.Model):
    Name = models.CharField(max_length = 20)
    Phone = models.CharField(max_length=11)
    Email = models.EmailField()
    Department = models.TextField(max_length=20)
    class Meta:
        db_table = "Employee"

    def __str__(self) -> str:
        return self.Name