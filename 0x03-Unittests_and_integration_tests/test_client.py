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
