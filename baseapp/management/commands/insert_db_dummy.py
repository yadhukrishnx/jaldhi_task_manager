from django.core.management.base import BaseCommand
from datetime import date
from baseapp.models import Task  
class Command(BaseCommand):
    help = 'Insert dummy tasks into the database'

    def handle(self, *args, **kwargs):
       tasks =   [
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
    {'title': 'Create User Stories', 'description': 'Develop user stories for the next sprint.', 'date': date(2024, 6, 11), 'is_completed': False},
    {'title': 'Design Database Schema', 'description': 'Design the schema for the new project database.', 'date': date(2024, 6, 12), 'is_completed': False},
    {'title': 'Set Up CI/CD Pipeline', 'description': 'Configure continuous integration and deployment pipeline.', 'date': date(2024, 6, 13), 'is_completed': False},
    {'title': 'Conduct Training Session', 'description': 'Train new team members on the project workflow.', 'date': date(2024, 6, 14), 'is_completed': False},
    {'title': 'Performance Testing', 'description': 'Perform load and stress testing on the application.', 'date': date(2024, 6, 15), 'is_completed': False},
    {'title': 'Code Refactoring', 'description': 'Refactor the existing codebase for better maintainability.', 'date': date(2024, 6, 16), 'is_completed': False},
    {'title': 'Security Audit', 'description': 'Conduct a security audit of the application.', 'date': date(2024, 6, 17), 'is_completed': False},
    {'title': 'Create API Documentation', 'description': 'Document the APIs developed for the project.', 'date': date(2024, 6, 18), 'is_completed': False},
    {'title': 'Plan Sprint Retrospective', 'description': 'Organize and plan the sprint retrospective meeting.', 'date': date(2024, 6, 19), 'is_completed': False},
    {'title': 'Prepare Presentation', 'description': 'Prepare a presentation for the upcoming project demo.', 'date': date(2024, 6, 20), 'is_completed': False},
    {'title': 'Update CI/CD Scripts', 'description': 'Update the CI/CD scripts to include new tests.', 'date': date(2024, 6, 21), 'is_completed': False},
    {'title': 'Analyze User Feedback', 'description': 'Analyze the feedback received from users.', 'date': date(2024, 6, 22), 'is_completed': False},
]


       for task_data in tasks:
            task = Task(**task_data)
            task.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created task "{task.title}"'))
