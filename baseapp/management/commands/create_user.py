from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from baseapp.models import UserProfile  # Adjust 'myapp' to the name of your app

class Command(BaseCommand):
    help = 'Creates dummy users with profile images'

    def handle(self, *args, **options):
        # Create dummy users with profile images
        dummy_users = [
            {'username': 'user1', 'password': 'password1', 'image_path': 'path/to/image1.jpg'},
            {'username': 'user2', 'password': 'password2', 'image_path': 'path/to/image2.jpg'},
            # Add more dummy user data as needed
        ]

        for data in dummy_users:
            username = data['username']
            password = data['password']
            image_path = data['image_path']

            # Create user
            user = User.objects.create_user(username=username, password=password)

            # Create user profile with image
            user_profile = UserProfile(user=user, image=image_path)
            user_profile.save()

            self.stdout.write(self.style.SUCCESS(f"Dummy user '{username}' created successfully."))
