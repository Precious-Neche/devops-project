from unittest.mock import patch, MagicMock
from django.test import SimpleTestCase


class HealthCheckTests(SimpleTestCase):
    @patch("health.views.redis.Redis.from_url")
    def test_health_check_returns_ok(self, mock_from_url):
        fake_redis = MagicMock()
        fake_redis.get.return_value = b"ok"
        mock_from_url.return_value = fake_redis

        response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")