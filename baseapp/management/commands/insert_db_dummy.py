from django.core.management.base import BaseCommand
from datetime import date
from baseapp.models import Task  
class Command(BaseCommand):
    help = 'Insert dummy tasks into the database'

    def handle(self, *args, **kwargs):
        tasks = [
    {'title': 'Complete Project Report', 'description': 'Finalize and submit the project report to the client.', 'date': date(2024, 6, 1), 'is_completed': False},
    {'title': 'Code Review', 'description': 'Review the code submitted by the junior developers.', 'date': date(2024, 6, 2), 'is_completed': False},
    {'title': 'Client Meeting', 'description': 'Discuss the new requirements and project scope with the client.', 'date': date(2024, 6, 3), 'is_completed': True},
    {'title': 'Team Standup', 'description': 'Daily standup meeting with the development team.', 'date': date(2024, 6, 4), 'is_completed': True},
    {'title': 'Implement Authentication', 'description': 'Develop and integrate authentication module for the application.', 'date': date(2024, 6, 5), 'is_completed': False},
    {'title': 'Fix Bugs', 'description': 'Fix the bugs reported by the QA team in the latest release.', 'date': date(2024, 6, 6), 'is_completed': False},
    {'title': 'Optimize Database', 'description': 'Optimize database queries and indexes for better performance.', 'date': date(2024, 6, 7), 'is_completed': True},
    {'title': 'Deploy to Production', 'description': 'Deploy the latest version of the application to the production server.', 'date': date(2024, 6, 8), 'is_completed': True},
    {'title': 'Write Unit Tests', 'description': 'Write unit tests for the new features added in the project.', 'date': date(2024, 6, 9), 'is_completed': False},
    {'title': 'Update Documentation', 'description': 'Update the project documentation with the latest changes.', 'date': date(2024, 6, 10), 'is_completed': False},
]

        for task_data in tasks:
            task = Task(**task_data)
            task.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created task "{task.title}"'))
