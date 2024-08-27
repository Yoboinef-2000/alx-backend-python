#!/usr/bin/env python3
"""Testing GithubOrgClient.org"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient.org"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Testing GithubOrgClient.org"""
        mock_response = {"login": org_name}
        mock_get_json.return_value = mock_response

        client = GithubOrgClient(org_name)
        result = client.org()

        mock_get_json.\
            assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, mock_response)

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the expected URL"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Testing if has_license returns the correct result."""

        client = GithubOrgClient("test_org")
        with patch.object(client, 'repo', repo):
            result = client.has_license(license_key)
            self.assertEqual(result, expected_result)
