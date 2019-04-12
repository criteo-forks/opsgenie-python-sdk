# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from opsgenie_swagger.models.action_mapping import ActionMapping  # noqa: F401,E501
from opsgenie_swagger.models.alert_filter import AlertFilter  # noqa: F401,E501
from opsgenie_swagger.models.integration import Integration  # noqa: F401,E501
from opsgenie_swagger.models.team_meta import TeamMeta  # noqa: F401,E501
from opsgenie_swagger.models.webhook_callback import WebhookCallback  # noqa: F401,E501


class WebhookIntegration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alert_filter': 'AlertFilter',
        'forwarding_enabled': 'bool',
        'forwarding_action_mappings': 'list[ActionMapping]',
        'callback_type': 'str',
        'url': 'str',
        'headers': 'dict(str, str)',
        'add_alert_details': 'bool',
        'add_alert_description': 'bool',
        'base_webhook_callback_type': 'str'
    }

    attribute_map = {
        'alert_filter': 'alertFilter',
        'forwarding_enabled': 'forwardingEnabled',
        'forwarding_action_mappings': 'forwardingActionMappings',
        'callback_type': 'callback-type',
        'url': 'url',
        'headers': 'headers',
        'add_alert_details': 'addAlertDetails',
        'add_alert_description': 'addAlertDescription',
        'base_webhook_callback_type': 'base-webhook-callback-type'
    }

    def __init__(self, alert_filter=None, forwarding_enabled=None, forwarding_action_mappings=None, callback_type=None, url=None, headers=None, add_alert_details=None, add_alert_description=None, base_webhook_callback_type=None):  # noqa: E501
        """WebhookIntegration - a model defined in Swagger"""  # noqa: E501

        self._alert_filter = None
        self._forwarding_enabled = None
        self._forwarding_action_mappings = None
        self._callback_type = None
        self._url = None
        self._headers = None
        self._add_alert_details = None
        self._add_alert_description = None
        self._base_webhook_callback_type = None
        self.discriminator = None

        if alert_filter is not None:
            self.alert_filter = alert_filter
        if forwarding_enabled is not None:
            self.forwarding_enabled = forwarding_enabled
        if forwarding_action_mappings is not None:
            self.forwarding_action_mappings = forwarding_action_mappings
        if callback_type is not None:
            self.callback_type = callback_type
        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers
        if add_alert_details is not None:
            self.add_alert_details = add_alert_details
        if add_alert_description is not None:
            self.add_alert_description = add_alert_description
        if base_webhook_callback_type is not None:
            self.base_webhook_callback_type = base_webhook_callback_type

    @property
    def alert_filter(self):
        """Gets the alert_filter of this WebhookIntegration.  # noqa: E501


        :return: The alert_filter of this WebhookIntegration.  # noqa: E501
        :rtype: AlertFilter
        """
        return self._alert_filter

    @alert_filter.setter
    def alert_filter(self, alert_filter):
        """Sets the alert_filter of this WebhookIntegration.


        :param alert_filter: The alert_filter of this WebhookIntegration.  # noqa: E501
        :type: AlertFilter
        """

        self._alert_filter = alert_filter

    @property
    def forwarding_enabled(self):
        """Gets the forwarding_enabled of this WebhookIntegration.  # noqa: E501


        :return: The forwarding_enabled of this WebhookIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._forwarding_enabled

    @forwarding_enabled.setter
    def forwarding_enabled(self, forwarding_enabled):
        """Sets the forwarding_enabled of this WebhookIntegration.


        :param forwarding_enabled: The forwarding_enabled of this WebhookIntegration.  # noqa: E501
        :type: bool
        """

        self._forwarding_enabled = forwarding_enabled

    @property
    def forwarding_action_mappings(self):
        """Gets the forwarding_action_mappings of this WebhookIntegration.  # noqa: E501


        :return: The forwarding_action_mappings of this WebhookIntegration.  # noqa: E501
        :rtype: list[ActionMapping]
        """
        return self._forwarding_action_mappings

    @forwarding_action_mappings.setter
    def forwarding_action_mappings(self, forwarding_action_mappings):
        """Sets the forwarding_action_mappings of this WebhookIntegration.


        :param forwarding_action_mappings: The forwarding_action_mappings of this WebhookIntegration.  # noqa: E501
        :type: list[ActionMapping]
        """

        self._forwarding_action_mappings = forwarding_action_mappings

    @property
    def callback_type(self):
        """Gets the callback_type of this WebhookIntegration.  # noqa: E501


        :return: The callback_type of this WebhookIntegration.  # noqa: E501
        :rtype: str
        """
        return self._callback_type

    @callback_type.setter
    def callback_type(self, callback_type):
        """Sets the callback_type of this WebhookIntegration.


        :param callback_type: The callback_type of this WebhookIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["amazon-sns-callback", "base-webhook-callback", "bidirectional-callback-new", "bmc-remedy-on-demand-callback"]  # noqa: E501
        if callback_type not in allowed_values:
            raise ValueError(
                "Invalid value for `callback_type` ({0}), must be one of {1}"  # noqa: E501
                .format(callback_type, allowed_values)
            )

        self._callback_type = callback_type

    @property
    def url(self):
        """Gets the url of this WebhookIntegration.  # noqa: E501


        :return: The url of this WebhookIntegration.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookIntegration.


        :param url: The url of this WebhookIntegration.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this WebhookIntegration.  # noqa: E501


        :return: The headers of this WebhookIntegration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this WebhookIntegration.


        :param headers: The headers of this WebhookIntegration.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def add_alert_details(self):
        """Gets the add_alert_details of this WebhookIntegration.  # noqa: E501


        :return: The add_alert_details of this WebhookIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._add_alert_details

    @add_alert_details.setter
    def add_alert_details(self, add_alert_details):
        """Sets the add_alert_details of this WebhookIntegration.


        :param add_alert_details: The add_alert_details of this WebhookIntegration.  # noqa: E501
        :type: bool
        """

        self._add_alert_details = add_alert_details

    @property
    def add_alert_description(self):
        """Gets the add_alert_description of this WebhookIntegration.  # noqa: E501


        :return: The add_alert_description of this WebhookIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._add_alert_description

    @add_alert_description.setter
    def add_alert_description(self, add_alert_description):
        """Sets the add_alert_description of this WebhookIntegration.


        :param add_alert_description: The add_alert_description of this WebhookIntegration.  # noqa: E501
        :type: bool
        """

        self._add_alert_description = add_alert_description

    @property
    def base_webhook_callback_type(self):
        """Gets the base_webhook_callback_type of this WebhookIntegration.  # noqa: E501


        :return: The base_webhook_callback_type of this WebhookIntegration.  # noqa: E501
        :rtype: str
        """
        return self._base_webhook_callback_type

    @base_webhook_callback_type.setter
    def base_webhook_callback_type(self, base_webhook_callback_type):
        """Sets the base_webhook_callback_type of this WebhookIntegration.


        :param base_webhook_callback_type: The base_webhook_callback_type of this WebhookIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["flock-callback", "kore-callback", "moxtra-callback", "ring-central-glip-callback", "statusy-callback", "webhook-callback"]  # noqa: E501
        if base_webhook_callback_type not in allowed_values:
            raise ValueError(
                "Invalid value for `base_webhook_callback_type` ({0}), must be one of {1}"  # noqa: E501
                .format(base_webhook_callback_type, allowed_values)
            )

        self._base_webhook_callback_type = base_webhook_callback_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebhookIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
