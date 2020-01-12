import os
from django.contrib.auth.models import User
from dotenv import load_dotenv


load_dotenv()

username = os.getenv("SU_NAME")
email = os.getenv("SU_EMAIL")
password = os.getenv("SU_PASSWORD")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
