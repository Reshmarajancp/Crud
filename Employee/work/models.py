from django.db import models

class employee(models.Model):
    email=models.EmailField(null=True)
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.name

#python manage.py makemigrations --> ORM queriesine sql queriesilottu convert aakkan 

#python manage.py migrate--> query languagine sqlite lekk convert aakkan

#models : which is used to perform certain actions using data 

#Django default data base- SQLite3

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    email=models.EmailField(unique=True,null=True)
    place=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Emp(models.Model):
     name=models.CharField(max_length=20)
     place=models.CharField(max_length=20)
     salary=models.PositiveIntegerField()
     contact=models.PositiveIntegerField()

class book_models(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    publication_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=20)
        

class product_model(models.Model):
    price=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class stud_model(models.Model):
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    email=models.EmailField()

    
    def __str__(self):
        return self.name
    
    
class work(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    course=models.CharField(max_length=20)

    


