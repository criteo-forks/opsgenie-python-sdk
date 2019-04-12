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

from opsgenie_swagger.models.integration import Integration  # noqa: F401,E501
from opsgenie_swagger.models.recipient import Recipient  # noqa: F401,E501
from opsgenie_swagger.models.team_meta import TeamMeta  # noqa: F401,E501
from opsgenie_swagger.models.token_based_incoming_feature import TokenBasedIncomingFeature  # noqa: F401,E501


class AmazonSnsIntegration(object):
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
        'suppress_notifications': 'bool',
        'ignore_teams_from_payload': 'bool',
        'ignore_recipients_from_payload': 'bool',
        'recipients': 'list[Recipient]',
        'is_advanced': 'bool',
        'ignore_tags_from_payload': 'bool',
        'ignore_extra_properties_from_payload': 'bool',
        'priority': 'str',
        'custom_priority': 'str',
        'tags': 'list[str]',
        'extra_properties': 'dict(str, str)',
        'assigned_team': 'TeamMeta',
        'feature_type': 'str',
        'allow_configuration_access': 'bool',
        'allow_read_access': 'bool',
        'allow_write_access': 'bool',
        'allow_delete_access': 'bool'
    }

    attribute_map = {
        'suppress_notifications': 'suppressNotifications',
        'ignore_teams_from_payload': 'ignoreTeamsFromPayload',
        'ignore_recipients_from_payload': 'ignoreRecipientsFromPayload',
        'recipients': 'recipients',
        'is_advanced': 'isAdvanced',
        'ignore_tags_from_payload': 'ignoreTagsFromPayload',
        'ignore_extra_properties_from_payload': 'ignoreExtraPropertiesFromPayload',
        'priority': 'priority',
        'custom_priority': 'customPriority',
        'tags': 'tags',
        'extra_properties': 'extraProperties',
        'assigned_team': 'assignedTeam',
        'feature_type': 'feature-type',
        'allow_configuration_access': 'allowConfigurationAccess',
        'allow_read_access': 'allowReadAccess',
        'allow_write_access': 'allowWriteAccess',
        'allow_delete_access': 'allowDeleteAccess'
    }

    def __init__(self, suppress_notifications=None, ignore_teams_from_payload=None, ignore_recipients_from_payload=None, recipients=None, is_advanced=None, ignore_tags_from_payload=None, ignore_extra_properties_from_payload=None, priority=None, custom_priority=None, tags=None, extra_properties=None, assigned_team=None, feature_type=None, allow_configuration_access=None, allow_read_access=None, allow_write_access=None, allow_delete_access=None):  # noqa: E501
        """AmazonSnsIntegration - a model defined in Swagger"""  # noqa: E501

        self._suppress_notifications = None
        self._ignore_teams_from_payload = None
        self._ignore_recipients_from_payload = None
        self._recipients = None
        self._is_advanced = None
        self._ignore_tags_from_payload = None
        self._ignore_extra_properties_from_payload = None
        self._priority = None
        self._custom_priority = None
        self._tags = None
        self._extra_properties = None
        self._assigned_team = None
        self._feature_type = None
        self._allow_configuration_access = None
        self._allow_read_access = None
        self._allow_write_access = None
        self._allow_delete_access = None
        self.discriminator = None

        if suppress_notifications is not None:
            self.suppress_notifications = suppress_notifications
        if ignore_teams_from_payload is not None:
            self.ignore_teams_from_payload = ignore_teams_from_payload
        if ignore_recipients_from_payload is not None:
            self.ignore_recipients_from_payload = ignore_recipients_from_payload
        if recipients is not None:
            self.recipients = recipients
        if is_advanced is not None:
            self.is_advanced = is_advanced
        if ignore_tags_from_payload is not None:
            self.ignore_tags_from_payload = ignore_tags_from_payload
        if ignore_extra_properties_from_payload is not None:
            self.ignore_extra_properties_from_payload = ignore_extra_properties_from_payload
        if priority is not None:
            self.priority = priority
        if custom_priority is not None:
            self.custom_priority = custom_priority
        if tags is not None:
            self.tags = tags
        if extra_properties is not None:
            self.extra_properties = extra_properties
        if assigned_team is not None:
            self.assigned_team = assigned_team
        if feature_type is not None:
            self.feature_type = feature_type
        if allow_configuration_access is not None:
            self.allow_configuration_access = allow_configuration_access
        if allow_read_access is not None:
            self.allow_read_access = allow_read_access
        if allow_write_access is not None:
            self.allow_write_access = allow_write_access
        if allow_delete_access is not None:
            self.allow_delete_access = allow_delete_access

    @property
    def suppress_notifications(self):
        """Gets the suppress_notifications of this AmazonSnsIntegration.  # noqa: E501

        If enabled, notifications that come from alerts will be suppressed. Defaults to false  # noqa: E501

        :return: The suppress_notifications of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_notifications

    @suppress_notifications.setter
    def suppress_notifications(self, suppress_notifications):
        """Sets the suppress_notifications of this AmazonSnsIntegration.

        If enabled, notifications that come from alerts will be suppressed. Defaults to false  # noqa: E501

        :param suppress_notifications: The suppress_notifications of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._suppress_notifications = suppress_notifications

    @property
    def ignore_teams_from_payload(self):
        """Gets the ignore_teams_from_payload of this AmazonSnsIntegration.  # noqa: E501

        If enabled, the integration will ignore teams sent in request payloads. Defaults to false  # noqa: E501

        :return: The ignore_teams_from_payload of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_teams_from_payload

    @ignore_teams_from_payload.setter
    def ignore_teams_from_payload(self, ignore_teams_from_payload):
        """Sets the ignore_teams_from_payload of this AmazonSnsIntegration.

        If enabled, the integration will ignore teams sent in request payloads. Defaults to false  # noqa: E501

        :param ignore_teams_from_payload: The ignore_teams_from_payload of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._ignore_teams_from_payload = ignore_teams_from_payload

    @property
    def ignore_recipients_from_payload(self):
        """Gets the ignore_recipients_from_payload of this AmazonSnsIntegration.  # noqa: E501

        If enabled, the integration will ignore recipients sent in request payloads. Defaults to false  # noqa: E501

        :return: The ignore_recipients_from_payload of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_recipients_from_payload

    @ignore_recipients_from_payload.setter
    def ignore_recipients_from_payload(self, ignore_recipients_from_payload):
        """Sets the ignore_recipients_from_payload of this AmazonSnsIntegration.

        If enabled, the integration will ignore recipients sent in request payloads. Defaults to false  # noqa: E501

        :param ignore_recipients_from_payload: The ignore_recipients_from_payload of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._ignore_recipients_from_payload = ignore_recipients_from_payload

    @property
    def recipients(self):
        """Gets the recipients of this AmazonSnsIntegration.  # noqa: E501

        Optional user, schedule, teams or escalation names to calculate which users will receive the notifications of the alert. Recipients which are exceeding the limit are ignored  # noqa: E501

        :return: The recipients of this AmazonSnsIntegration.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this AmazonSnsIntegration.

        Optional user, schedule, teams or escalation names to calculate which users will receive the notifications of the alert. Recipients which are exceeding the limit are ignored  # noqa: E501

        :param recipients: The recipients of this AmazonSnsIntegration.  # noqa: E501
        :type: list[Recipient]
        """

        self._recipients = recipients

    @property
    def is_advanced(self):
        """Gets the is_advanced of this AmazonSnsIntegration.  # noqa: E501


        :return: The is_advanced of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._is_advanced

    @is_advanced.setter
    def is_advanced(self, is_advanced):
        """Sets the is_advanced of this AmazonSnsIntegration.


        :param is_advanced: The is_advanced of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._is_advanced = is_advanced

    @property
    def ignore_tags_from_payload(self):
        """Gets the ignore_tags_from_payload of this AmazonSnsIntegration.  # noqa: E501


        :return: The ignore_tags_from_payload of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_tags_from_payload

    @ignore_tags_from_payload.setter
    def ignore_tags_from_payload(self, ignore_tags_from_payload):
        """Sets the ignore_tags_from_payload of this AmazonSnsIntegration.


        :param ignore_tags_from_payload: The ignore_tags_from_payload of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._ignore_tags_from_payload = ignore_tags_from_payload

    @property
    def ignore_extra_properties_from_payload(self):
        """Gets the ignore_extra_properties_from_payload of this AmazonSnsIntegration.  # noqa: E501


        :return: The ignore_extra_properties_from_payload of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_extra_properties_from_payload

    @ignore_extra_properties_from_payload.setter
    def ignore_extra_properties_from_payload(self, ignore_extra_properties_from_payload):
        """Sets the ignore_extra_properties_from_payload of this AmazonSnsIntegration.


        :param ignore_extra_properties_from_payload: The ignore_extra_properties_from_payload of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._ignore_extra_properties_from_payload = ignore_extra_properties_from_payload

    @property
    def priority(self):
        """Gets the priority of this AmazonSnsIntegration.  # noqa: E501


        :return: The priority of this AmazonSnsIntegration.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this AmazonSnsIntegration.


        :param priority: The priority of this AmazonSnsIntegration.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def custom_priority(self):
        """Gets the custom_priority of this AmazonSnsIntegration.  # noqa: E501


        :return: The custom_priority of this AmazonSnsIntegration.  # noqa: E501
        :rtype: str
        """
        return self._custom_priority

    @custom_priority.setter
    def custom_priority(self, custom_priority):
        """Sets the custom_priority of this AmazonSnsIntegration.


        :param custom_priority: The custom_priority of this AmazonSnsIntegration.  # noqa: E501
        :type: str
        """

        self._custom_priority = custom_priority

    @property
    def tags(self):
        """Gets the tags of this AmazonSnsIntegration.  # noqa: E501


        :return: The tags of this AmazonSnsIntegration.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AmazonSnsIntegration.


        :param tags: The tags of this AmazonSnsIntegration.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def extra_properties(self):
        """Gets the extra_properties of this AmazonSnsIntegration.  # noqa: E501


        :return: The extra_properties of this AmazonSnsIntegration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this AmazonSnsIntegration.


        :param extra_properties: The extra_properties of this AmazonSnsIntegration.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra_properties = extra_properties

    @property
    def assigned_team(self):
        """Gets the assigned_team of this AmazonSnsIntegration.  # noqa: E501


        :return: The assigned_team of this AmazonSnsIntegration.  # noqa: E501
        :rtype: TeamMeta
        """
        return self._assigned_team

    @assigned_team.setter
    def assigned_team(self, assigned_team):
        """Sets the assigned_team of this AmazonSnsIntegration.


        :param assigned_team: The assigned_team of this AmazonSnsIntegration.  # noqa: E501
        :type: TeamMeta
        """

        self._assigned_team = assigned_team

    @property
    def feature_type(self):
        """Gets the feature_type of this AmazonSnsIntegration.  # noqa: E501


        :return: The feature_type of this AmazonSnsIntegration.  # noqa: E501
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this AmazonSnsIntegration.


        :param feature_type: The feature_type of this AmazonSnsIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["email-based", "token-based"]  # noqa: E501
        if feature_type not in allowed_values:
            raise ValueError(
                "Invalid value for `feature_type` ({0}), must be one of {1}"  # noqa: E501
                .format(feature_type, allowed_values)
            )

        self._feature_type = feature_type

    @property
    def allow_configuration_access(self):
        """Gets the allow_configuration_access of this AmazonSnsIntegration.  # noqa: E501

        This parameter is for allowing or restricting the configuration access. If configuration access is restricted, the integration will be limited to Alert API requests and sending heartbeats. Defaults to false  # noqa: E501

        :return: The allow_configuration_access of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_configuration_access

    @allow_configuration_access.setter
    def allow_configuration_access(self, allow_configuration_access):
        """Sets the allow_configuration_access of this AmazonSnsIntegration.

        This parameter is for allowing or restricting the configuration access. If configuration access is restricted, the integration will be limited to Alert API requests and sending heartbeats. Defaults to false  # noqa: E501

        :param allow_configuration_access: The allow_configuration_access of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._allow_configuration_access = allow_configuration_access

    @property
    def allow_read_access(self):
        """Gets the allow_read_access of this AmazonSnsIntegration.  # noqa: E501


        :return: The allow_read_access of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_read_access

    @allow_read_access.setter
    def allow_read_access(self, allow_read_access):
        """Sets the allow_read_access of this AmazonSnsIntegration.


        :param allow_read_access: The allow_read_access of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._allow_read_access = allow_read_access

    @property
    def allow_write_access(self):
        """Gets the allow_write_access of this AmazonSnsIntegration.  # noqa: E501

        This parameter is for configuring the read-only access of integration. If the integration is limited to read-only access, the integration will not be authorized to perform any create, update or delete action within any domain. Defaults to true  # noqa: E501

        :return: The allow_write_access of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_write_access

    @allow_write_access.setter
    def allow_write_access(self, allow_write_access):
        """Sets the allow_write_access of this AmazonSnsIntegration.

        This parameter is for configuring the read-only access of integration. If the integration is limited to read-only access, the integration will not be authorized to perform any create, update or delete action within any domain. Defaults to true  # noqa: E501

        :param allow_write_access: The allow_write_access of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._allow_write_access = allow_write_access

    @property
    def allow_delete_access(self):
        """Gets the allow_delete_access of this AmazonSnsIntegration.  # noqa: E501


        :return: The allow_delete_access of this AmazonSnsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_delete_access

    @allow_delete_access.setter
    def allow_delete_access(self, allow_delete_access):
        """Sets the allow_delete_access of this AmazonSnsIntegration.


        :param allow_delete_access: The allow_delete_access of this AmazonSnsIntegration.  # noqa: E501
        :type: bool
        """

        self._allow_delete_access = allow_delete_access

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
        if not isinstance(other, AmazonSnsIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
