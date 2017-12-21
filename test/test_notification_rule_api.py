# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opsgenie_swagger
from opsgenie_swagger.api.notification_rule_api import NotificationRuleApi  # noqa: E501
from opsgenie_swagger.rest import ApiException


class TestNotificationRuleApi(unittest.TestCase):
    """NotificationRuleApi unit test stubs"""

    def setUp(self):
        self.api = opsgenie_swagger.api.notification_rule_api.NotificationRuleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_notification_rule_order(self):
        """Test case for change_notification_rule_order

        Change order of Notification Rule  # noqa: E501
        """
        pass

    def test_create_notification_rule(self):
        """Test case for create_notification_rule

        Create Notification Rule  # noqa: E501
        """
        pass

    def test_delete_notification_rule(self):
        """Test case for delete_notification_rule

        Delete Notification Rule  # noqa: E501
        """
        pass

    def test_disable_notification_rule(self):
        """Test case for disable_notification_rule

        Disable Notification Rule  # noqa: E501
        """
        pass

    def test_enable_notification_rule(self):
        """Test case for enable_notification_rule

        Enable Notification Rule  # noqa: E501
        """
        pass

    def test_get_notification_rule(self):
        """Test case for get_notification_rule

        Get Notification Rule  # noqa: E501
        """
        pass

    def test_list_notification_rules(self):
        """Test case for list_notification_rules

        List Notification Rules  # noqa: E501
        """
        pass

    def test_update_notification_rule(self):
        """Test case for update_notification_rule

        Update Notification Rule (Partial)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()