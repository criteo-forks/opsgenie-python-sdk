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


class PrtgCallback(object):
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
        'passhash': 'str',
        'prtg_url': 'str'
    }

    attribute_map = {
        'username': 'username',
        'passhash': 'passhash',
        'prtg_url': 'prtgUrl'
    }

    def __init__(self, username=None, passhash=None, prtg_url=None):  # noqa: E501
        """PrtgCallback - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._passhash = None
        self._prtg_url = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if passhash is not None:
            self.passhash = passhash
        if prtg_url is not None:
            self.prtg_url = prtg_url

    @property
    def username(self):
        """Gets the username of this PrtgCallback.  # noqa: E501


        :return: The username of this PrtgCallback.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PrtgCallback.


        :param username: The username of this PrtgCallback.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def passhash(self):
        """Gets the passhash of this PrtgCallback.  # noqa: E501


        :return: The passhash of this PrtgCallback.  # noqa: E501
        :rtype: str
        """
        return self._passhash

    @passhash.setter
    def passhash(self, passhash):
        """Sets the passhash of this PrtgCallback.


        :param passhash: The passhash of this PrtgCallback.  # noqa: E501
        :type: str
        """

        self._passhash = passhash

    @property
    def prtg_url(self):
        """Gets the prtg_url of this PrtgCallback.  # noqa: E501


        :return: The prtg_url of this PrtgCallback.  # noqa: E501
        :rtype: str
        """
        return self._prtg_url

    @prtg_url.setter
    def prtg_url(self, prtg_url):
        """Sets the prtg_url of this PrtgCallback.


        :param prtg_url: The prtg_url of this PrtgCallback.  # noqa: E501
        :type: str
        """

        self._prtg_url = prtg_url

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
        if not isinstance(other, PrtgCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
