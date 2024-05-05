from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.crypto import get_random_string


class role(models.Model):
    title = models.CharField(max_length=75)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    active = models.TextField(max_length=1)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()


class U_user(models.Model):
    role_ID = models.ForeignKey(role, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    passwordHash = models.CharField(max_length=255)
    CNIC = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField() #max_length=20,
    registered = models.DateTimeField()
    LastLogin = models.DateTimeField()


class Internal_User(models.Model):
    role_ID = models.ForeignKey(role, on_delete=models.CASCADE)  
    name = models.CharField(max_length=255)
    Emp_ID = models.PositiveBigIntegerField()
    CNIC = models.CharField(max_length=255)
    Data = models.TextField()
    is_active = models.BooleanField()
    HashPassword = models.TextField()
    created_at = models.DateTimeField(  default='2024-05-03T01:55:00Z')
    updated = models.DateTimeField(  null=True)

    @property
    def is_authenticated(self):
        # Implement authentication logic here
        # For example, return True if the user is authenticated, False otherwise
        return True  # Placeholder implementation


class user_meta(models.Model):
    used = models.ForeignKey(U_user, on_delete=models.CASCADE)
    key = models.CharField(max_length=75) 
    value = models.CharField(max_length=75)



class permission(models.Model):
    title = models.CharField(max_length=75)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    active = models.TextField(max_length=1) 
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()


class role_permission(models.Model):
    roleId = models.ForeignKey(role, on_delete=models.CASCADE) #max_length=20,
    permissionId = models.ForeignKey(permission, on_delete=models.CASCADE)
    createdAT = models.DateTimeField()
    updatedAt = models.DateTimeField()


class Property_Owner(models.Model):
    Owner_Name = models.CharField(max_length=255)
    CNIC = models.CharField(max_length=255)
    Edit_by = models.BigIntegerField() #max_length=20,
    Created_at = models.DateTimeField()
    Uploaded_at = models.DateTimeField()


class Property_Owner_meta(models.Model):
    Key = models.CharField(max_length=255)
    Value = models.TextField()
    Owner_ID = models.ForeignKey(Property_Owner, on_delete=models.CASCADE)
    Edit_by = models.PositiveBigIntegerField() #max_length=20,

class Property(models.Model):
    Property_key = models.CharField(max_length=255)
    Sector = models.PositiveBigIntegerField() #max_length=255
    Owner = models.PositiveBigIntegerField() #max_length=20,
    Property_Type = models.PositiveBigIntegerField() #max_length=20,
    Plot_No = models.CharField(max_length=255)
    Society = models.PositiveBigIntegerField() #max_length=20,
    Street_No = models.CharField(max_length=255)
    Phase = models.CharField(max_length=255)
    Gali_No = models.CharField(max_length=255)
    Society_Sector = models.CharField(max_length=255)
    Flat_No = models.CharField(max_length=255)
    Block_No = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField() #max_length=20,
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Property_meta(models.Model):
    Key = models.CharField(max_length=255)
    Value = models.TextField()
    Property_ID = models.PositiveBigIntegerField() #max_length=20,
    Edit_by = models.PositiveBigIntegerField() #max_length=20,
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Property_Bills(models.Model):
    Consumer_ID = models.CharField(max_length=255)
    Bill_Type = models.PositiveBigIntegerField() #max_length=20,
    Property_key = models.CharField(max_length=255)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Bills(models.Model):
    Name = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField() #max_length=20,
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

    
class Zone(models.Model):
    Name = models.CharField(max_length=255)
    Created_by = models.PositiveBigIntegerField() #max_length=20,
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()


class Sector(models.Model):
    ParentID = models.PositiveBigIntegerField()
    Name = models.CharField(max_length=255)
    Zone_ID = models.ForeignKey(Zone, on_delete=models.CASCADE) #max_length=20,
    Created_by = models.PositiveBigIntegerField() #max_length=20,
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()



class Society(models.Model):
    Image = models.TextField()
    Name = models.CharField(max_length=255)
    Created_by = models.ForeignKey(Internal_User, on_delete=models.CASCADE) #max_length=20,
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()

class Property_Type(models.Model):
    Name = models.CharField(max_length=255)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()


class CustomToken(models.Model):
    user = models.ForeignKey(Internal_User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return get_random_string(40)

    def __str__(self):
        return f"Token for {self.user.name}"