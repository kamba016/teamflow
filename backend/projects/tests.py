# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Project


class HealthCheckTests(TestCase):

    def test_health_check_returns_success(self):
        response = self.client.get(
            reverse("health-check")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["status"],
            "success"
        )
class ProjectModelTests(TestCase):

    def test_create_project(self):
        project = Project.objects.create(
            name="TeamFlow Development",
            description="Our first project",
        )

        self.assertEqual(
            project.name,
            "TeamFlow Development"
        )

        self.assertEqual(
            project.status,
            Project.Status.PLANNED
        )

        self.assertIsNotNone(project.id)

    def test_project_string_representation(self):
        project = Project.objects.create(
            name="Cloud Project"
        )

        self.assertEqual(str(project), "Cloud Project")