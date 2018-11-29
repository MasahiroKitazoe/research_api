from django.db import models

class User(models.Model):
  user_id = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=50)

  @classmethod
  def insert_user_data(cls, user_id, password):
    User.objects.create(
        user_id=user_id,
        password=password
      )

  @classmethod
  def is_registered(cls, user_id, password):
    try:
      user = User.objects.filter(user_id=user_id).first()
    except User.DoesNotExist:
      return False

    if user.password == password:
      return True
    else:
      return False
