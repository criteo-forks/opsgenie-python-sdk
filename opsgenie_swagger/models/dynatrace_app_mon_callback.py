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
from opsgenie_swagger.models.bidirectional_callback_new import BidirectionalCallbackNew  # noqa: F401,E501


class DynatraceAppMonCallback(object):
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
        'username': 'str',
        'password': 'str',
        'url': 'str',
        'profile_name': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'url': 'url',
        'profile_name': 'profileName'
    }

    def __init__(self, username=None, password=None, url=None, profile_name=None):  # noqa: E501
        """DynatraceAppMonCallback - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._password = None
        self._url = None
        self._profile_name = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if url is not None:
            self.url = url
        if profile_name is not None:
            self.profile_name = profile_name

    @property
    def username(self):
        """Gets the username of this DynatraceAppMonCallback.  # noqa: E501


        :return: The username of this DynatraceAppMonCallback.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DynatraceAppMonCallback.


        :param username: The username of this DynatraceAppMonCallback.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this DynatraceAppMonCallback.  # noqa: E501


        :return: The password of this DynatraceAppMonCallback.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DynatraceAppMonCallback.


        :param password: The password of this DynatraceAppMonCallback.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def url(self):
        """Gets the url of this DynatraceAppMonCallback.  # noqa: E501


        :return: The url of this DynatraceAppMonCallback.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DynatraceAppMonCallback.


        :param url: The url of this DynatraceAppMonCallback.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def profile_name(self):
        """Gets the profile_name of this DynatraceAppMonCallback.  # noqa: E501


        :return: The profile_name of this DynatraceAppMonCallback.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this DynatraceAppMonCallback.


        :param profile_name: The profile_name of this DynatraceAppMonCallback.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

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
        if not isinstance(other, DynatraceAppMonCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
