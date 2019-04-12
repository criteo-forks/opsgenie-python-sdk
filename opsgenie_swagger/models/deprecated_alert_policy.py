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

from opsgenie_swagger.models.filter import Filter  # noqa: F401,E501
from opsgenie_swagger.models.time_restriction_interval import TimeRestrictionInterval  # noqa: F401,E501


class DeprecatedAlertPolicy(object):
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
        'id': 'str',
        'name': 'str',
        'policy_description': 'str',
        'filter': 'Filter',
        'time_restrictions': 'TimeRestrictionInterval',
        'enabled': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policy_description': 'policyDescription',
        'filter': 'filter',
        'time_restrictions': 'timeRestrictions',
        'enabled': 'enabled',
        'type': 'type'
    }

    discriminator_value_class_map = {
        'auto-restart-notifications': 'DeprecatedAutoRestartNotificationsAlertPolicy',
        'notification-deduplication': 'DeprecatedNotificationDeduplicationAlertPolicy',
        'notification-suppress': 'DeprecatedNotificationSuppressAlertPolicy',
        'notification-renotify': 'DeprecatedNotificationRenotifyAlertPolicy',
        'modify': 'DeprecatedModifyAlertPolicy',
        'auto-close': 'DeprecatedAutoCloseAlertPolicy',
        'notification-delay': 'DeprecatedNotificationDelayAlertPolicy'
    }

    def __init__(self, id=None, name=None, policy_description=None, filter=None, time_restrictions=None, enabled=None, type=None):  # noqa: E501
        """DeprecatedAlertPolicy - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._policy_description = None
        self._filter = None
        self._time_restrictions = None
        self._enabled = None
        self._type = None
        self.discriminator = 'type'

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policy_description is not None:
            self.policy_description = policy_description
        if filter is not None:
            self.filter = filter
        if time_restrictions is not None:
            self.time_restrictions = time_restrictions
        if enabled is not None:
            self.enabled = enabled
        self.type = type

    @property
    def id(self):
        """Gets the id of this DeprecatedAlertPolicy.  # noqa: E501


        :return: The id of this DeprecatedAlertPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeprecatedAlertPolicy.


        :param id: The id of this DeprecatedAlertPolicy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeprecatedAlertPolicy.  # noqa: E501

        Name of the policy  # noqa: E501

        :return: The name of this DeprecatedAlertPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeprecatedAlertPolicy.

        Name of the policy  # noqa: E501

        :param name: The name of this DeprecatedAlertPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def policy_description(self):
        """Gets the policy_description of this DeprecatedAlertPolicy.  # noqa: E501

        Description of the policy  # noqa: E501

        :return: The policy_description of this DeprecatedAlertPolicy.  # noqa: E501
        :rtype: str
        """
        return self._policy_description

    @policy_description.setter
    def policy_description(self, policy_description):
        """Sets the policy_description of this DeprecatedAlertPolicy.

        Description of the policy  # noqa: E501

        :param policy_description: The policy_description of this DeprecatedAlertPolicy.  # noqa: E501
        :type: str
        """

        self._policy_description = policy_description

    @property
    def filter(self):
        """Gets the filter of this DeprecatedAlertPolicy.  # noqa: E501

        Conditions specified in this field must be met for this policy to work  # noqa: E501

        :return: The filter of this DeprecatedAlertPolicy.  # noqa: E501
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this DeprecatedAlertPolicy.

        Conditions specified in this field must be met for this policy to work  # noqa: E501

        :param filter: The filter of this DeprecatedAlertPolicy.  # noqa: E501
        :type: Filter
        """

        self._filter = filter

    @property
    def time_restrictions(self):
        """Gets the time_restrictions of this DeprecatedAlertPolicy.  # noqa: E501

        Time restrictions specified in this field must be met for this policy to work  # noqa: E501

        :return: The time_restrictions of this DeprecatedAlertPolicy.  # noqa: E501
        :rtype: TimeRestrictionInterval
        """
        return self._time_restrictions

    @time_restrictions.setter
    def time_restrictions(self, time_restrictions):
        """Sets the time_restrictions of this DeprecatedAlertPolicy.

        Time restrictions specified in this field must be met for this policy to work  # noqa: E501

        :param time_restrictions: The time_restrictions of this DeprecatedAlertPolicy.  # noqa: E501
        :type: TimeRestrictionInterval
        """

        self._time_restrictions = time_restrictions

    @property
    def enabled(self):
        """Gets the enabled of this DeprecatedAlertPolicy.  # noqa: E501

        Activity status of the alert policy  # noqa: E501

        :return: The enabled of this DeprecatedAlertPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DeprecatedAlertPolicy.

        Activity status of the alert policy  # noqa: E501

        :param enabled: The enabled of this DeprecatedAlertPolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def type(self):
        """Gets the type of this DeprecatedAlertPolicy.  # noqa: E501

        Type of the policy  # noqa: E501

        :return: The type of this DeprecatedAlertPolicy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeprecatedAlertPolicy.

        Type of the policy  # noqa: E501

        :param type: The type of this DeprecatedAlertPolicy.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["modify", "auto-close", "notification-delay", "notification-deduplication", "notification-suppress", "notification-renotify", "auto-restart-notifications"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, DeprecatedAlertPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other