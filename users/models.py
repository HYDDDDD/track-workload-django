from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    ROLE = {
        "ADMIN": "admin",
        "USER": "users"
    }

    BRANCH = {
        "DB": "สาขาวิชาธุรกิจดิจิทัล",
        "IT": "สาขาวิชาเทคโนโลยีสารสนเทศ",
        "GIS": "สาขาวิชาภูมิสารสนเทศศาสตร์",
        "CS": "สาขาวิชาวิทยาการคอมพิวเตอร์",
        "DSA": "สาขาวิชาวิทยาการข้อมูลและการประยุกต์",
        "CPE": "สาขาวิชาวิศวกรรมคอมพิวเตอร์",
        "SE": "สาขาวิชาวิศวกรรมซอฟต์แวร์",
        "CG": "สาขาวิชาคอมพิวเตอร์กราฟิกและมัลติมีเดีย",
        "OFFICE": "สำนักงานคณะ"
    }

    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=5, choices=ROLE)
    branch = models.CharField(max_length=40, choices=BRANCH)
    totalHour = models.IntegerField(null=True)

    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName', 'role']

    def __str__(self):
        return self.email
