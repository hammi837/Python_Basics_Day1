from django.contrib.auth.base_user import BaseUserManager

class usermanager(BaseUserManager):
    use_in_migrations =True
    def create_user(self, email, password=None, **extra_field):
        if not email:
            raise ValueError('email is required')
        user=self.models(email=email, **extra_field)
        user=self.normalize_email(email)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password=None, **extra_field):
        extra_field.setdefault('is_staff' ,True)
        extra_field.setdefault('is_superuser' ,True)
        extra_field.setdefault('is_active' ,True)
        return self.create_user(email, password , **extra_field)
    

    
