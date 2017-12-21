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

from opsgenie_swagger.models.base_incoming_feature import BaseIncomingFeature  # noqa: F401,E501
from opsgenie_swagger.models.recipient import Recipient  # noqa: F401,E501


class TokenBasedIncomingFeature(object):
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
        'allow_configuration_access': 'bool',
        'allow_write_access': 'bool'
    }

    attribute_map = {
        'allow_configuration_access': 'allowConfigurationAccess',
        'allow_write_access': 'allowWriteAccess'
    }

    def __init__(self, allow_configuration_access=None, allow_write_access=None):  # noqa: E501
        """TokenBasedIncomingFeature - a model defined in Swagger"""  # noqa: E501

        self._allow_configuration_access = None
        self._allow_write_access = None
        self.discriminator = None

        if allow_configuration_access is not None:
            self.allow_configuration_access = allow_configuration_access
        if allow_write_access is not None:
            self.allow_write_access = allow_write_access

    @property
    def allow_configuration_access(self):
        """Gets the allow_configuration_access of this TokenBasedIncomingFeature.  # noqa: E501

        This parameter is for allowing or restricting the configuration access. If configuration access is restricted, the integration will be limited to Alert API requests and sending heartbeats. Defaults to false  # noqa: E501

        :return: The allow_configuration_access of this TokenBasedIncomingFeature.  # noqa: E501
        :rtype: bool
        """
        return self._allow_configuration_access

    @allow_configuration_access.setter
    def allow_configuration_access(self, allow_configuration_access):
        """Sets the allow_configuration_access of this TokenBasedIncomingFeature.

        This parameter is for allowing or restricting the configuration access. If configuration access is restricted, the integration will be limited to Alert API requests and sending heartbeats. Defaults to false  # noqa: E501

        :param allow_configuration_access: The allow_configuration_access of this TokenBasedIncomingFeature.  # noqa: E501
        :type: bool
        """

        self._allow_configuration_access = allow_configuration_access

    @property
    def allow_write_access(self):
        """Gets the allow_write_access of this TokenBasedIncomingFeature.  # noqa: E501

        This parameter is for configuring the read-only access of integration. If the integration is limited to read-only access, the integration will not be authorized to perform any create, update or delete action within any domain. Defaults to true  # noqa: E501

        :return: The allow_write_access of this TokenBasedIncomingFeature.  # noqa: E501
        :rtype: bool
        """
        return self._allow_write_access

    @allow_write_access.setter
    def allow_write_access(self, allow_write_access):
        """Sets the allow_write_access of this TokenBasedIncomingFeature.

        This parameter is for configuring the read-only access of integration. If the integration is limited to read-only access, the integration will not be authorized to perform any create, update or delete action within any domain. Defaults to true  # noqa: E501

        :param allow_write_access: The allow_write_access of this TokenBasedIncomingFeature.  # noqa: E501
        :type: bool
        """

        self._allow_write_access = allow_write_access

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
        if not isinstance(other, TokenBasedIncomingFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other