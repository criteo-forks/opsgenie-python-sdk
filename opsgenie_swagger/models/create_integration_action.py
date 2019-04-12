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

from opsgenie_swagger.models.common_integration_action import CommonIntegrationAction  # noqa: F401,E501
from opsgenie_swagger.models.integration_action_filter import IntegrationActionFilter  # noqa: F401,E501
from opsgenie_swagger.models.recipient import Recipient  # noqa: F401,E501


class CreateIntegrationAction(object):
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
        'source': 'str',
        'message': 'str',
        'description': 'str',
        'entity': 'str',
        'priority': 'str',
        'custom_priority': 'str',
        'append_attachments': 'bool',
        'alert_actions': 'list[str]',
        'ignore_alert_actions_from_payload': 'bool',
        'recipients': 'list[Recipient]',
        'ignore_recipients_from_payload': 'bool',
        'ignore_teams_from_payload': 'bool',
        'tags': 'list[str]',
        'ignore_tags_from_payload': 'bool',
        'extra_properties': 'dict(str, str)',
        'ignore_extra_properties_from_payload': 'bool'
    }

    attribute_map = {
        'source': 'source',
        'message': 'message',
        'description': 'description',
        'entity': 'entity',
        'priority': 'priority',
        'custom_priority': 'customPriority',
        'append_attachments': 'appendAttachments',
        'alert_actions': 'alertActions',
        'ignore_alert_actions_from_payload': 'ignoreAlertActionsFromPayload',
        'recipients': 'recipients',
        'ignore_recipients_from_payload': 'ignoreRecipientsFromPayload',
        'ignore_teams_from_payload': 'ignoreTeamsFromPayload',
        'tags': 'tags',
        'ignore_tags_from_payload': 'ignoreTagsFromPayload',
        'extra_properties': 'extraProperties',
        'ignore_extra_properties_from_payload': 'ignoreExtraPropertiesFromPayload'
    }

    def __init__(self, source=None, message=None, description=None, entity=None, priority=None, custom_priority=None, append_attachments=None, alert_actions=None, ignore_alert_actions_from_payload=None, recipients=None, ignore_recipients_from_payload=None, ignore_teams_from_payload=None, tags=None, ignore_tags_from_payload=None, extra_properties=None, ignore_extra_properties_from_payload=None):  # noqa: E501
        """CreateIntegrationAction - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._message = None
        self._description = None
        self._entity = None
        self._priority = None
        self._custom_priority = None
        self._append_attachments = None
        self._alert_actions = None
        self._ignore_alert_actions_from_payload = None
        self._recipients = None
        self._ignore_recipients_from_payload = None
        self._ignore_teams_from_payload = None
        self._tags = None
        self._ignore_tags_from_payload = None
        self._extra_properties = None
        self._ignore_extra_properties_from_payload = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if message is not None:
            self.message = message
        if description is not None:
            self.description = description
        if entity is not None:
            self.entity = entity
        if priority is not None:
            self.priority = priority
        if custom_priority is not None:
            self.custom_priority = custom_priority
        if append_attachments is not None:
            self.append_attachments = append_attachments
        if alert_actions is not None:
            self.alert_actions = alert_actions
        if ignore_alert_actions_from_payload is not None:
            self.ignore_alert_actions_from_payload = ignore_alert_actions_from_payload
        if recipients is not None:
            self.recipients = recipients
        if ignore_recipients_from_payload is not None:
            self.ignore_recipients_from_payload = ignore_recipients_from_payload
        if ignore_teams_from_payload is not None:
            self.ignore_teams_from_payload = ignore_teams_from_payload
        if tags is not None:
            self.tags = tags
        if ignore_tags_from_payload is not None:
            self.ignore_tags_from_payload = ignore_tags_from_payload
        if extra_properties is not None:
            self.extra_properties = extra_properties
        if ignore_extra_properties_from_payload is not None:
            self.ignore_extra_properties_from_payload = ignore_extra_properties_from_payload

    @property
    def source(self):
        """Gets the source of this CreateIntegrationAction.  # noqa: E501


        :return: The source of this CreateIntegrationAction.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateIntegrationAction.


        :param source: The source of this CreateIntegrationAction.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def message(self):
        """Gets the message of this CreateIntegrationAction.  # noqa: E501


        :return: The message of this CreateIntegrationAction.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateIntegrationAction.


        :param message: The message of this CreateIntegrationAction.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def description(self):
        """Gets the description of this CreateIntegrationAction.  # noqa: E501


        :return: The description of this CreateIntegrationAction.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIntegrationAction.


        :param description: The description of this CreateIntegrationAction.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entity(self):
        """Gets the entity of this CreateIntegrationAction.  # noqa: E501


        :return: The entity of this CreateIntegrationAction.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this CreateIntegrationAction.


        :param entity: The entity of this CreateIntegrationAction.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def priority(self):
        """Gets the priority of this CreateIntegrationAction.  # noqa: E501


        :return: The priority of this CreateIntegrationAction.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateIntegrationAction.


        :param priority: The priority of this CreateIntegrationAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["P1", "P2", "P3", "P4", "P5"]  # noqa: E501
        if priority not in allowed_values:
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def custom_priority(self):
        """Gets the custom_priority of this CreateIntegrationAction.  # noqa: E501


        :return: The custom_priority of this CreateIntegrationAction.  # noqa: E501
        :rtype: str
        """
        return self._custom_priority

    @custom_priority.setter
    def custom_priority(self, custom_priority):
        """Sets the custom_priority of this CreateIntegrationAction.


        :param custom_priority: The custom_priority of this CreateIntegrationAction.  # noqa: E501
        :type: str
        """

        self._custom_priority = custom_priority

    @property
    def append_attachments(self):
        """Gets the append_attachments of this CreateIntegrationAction.  # noqa: E501


        :return: The append_attachments of this CreateIntegrationAction.  # noqa: E501
        :rtype: bool
        """
        return self._append_attachments

    @append_attachments.setter
    def append_attachments(self, append_attachments):
        """Sets the append_attachments of this CreateIntegrationAction.


        :param append_attachments: The append_attachments of this CreateIntegrationAction.  # noqa: E501
        :type: bool
        """

        self._append_attachments = append_attachments

    @property
    def alert_actions(self):
        """Gets the alert_actions of this CreateIntegrationAction.  # noqa: E501


        :return: The alert_actions of this CreateIntegrationAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_actions

    @alert_actions.setter
    def alert_actions(self, alert_actions):
        """Sets the alert_actions of this CreateIntegrationAction.


        :param alert_actions: The alert_actions of this CreateIntegrationAction.  # noqa: E501
        :type: list[str]
        """

        self._alert_actions = alert_actions

    @property
    def ignore_alert_actions_from_payload(self):
        """Gets the ignore_alert_actions_from_payload of this CreateIntegrationAction.  # noqa: E501


        :return: The ignore_alert_actions_from_payload of this CreateIntegrationAction.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_alert_actions_from_payload

    @ignore_alert_actions_from_payload.setter
    def ignore_alert_actions_from_payload(self, ignore_alert_actions_from_payload):
        """Sets the ignore_alert_actions_from_payload of this CreateIntegrationAction.


        :param ignore_alert_actions_from_payload: The ignore_alert_actions_from_payload of this CreateIntegrationAction.  # noqa: E501
        :type: bool
        """

        self._ignore_alert_actions_from_payload = ignore_alert_actions_from_payload

    @property
    def recipients(self):
        """Gets the recipients of this CreateIntegrationAction.  # noqa: E501


        :return: The recipients of this CreateIntegrationAction.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this CreateIntegrationAction.


        :param recipients: The recipients of this CreateIntegrationAction.  # noqa: E501
        :type: list[Recipient]
        """

        self._recipients = recipients

    @property
    def ignore_recipients_from_payload(self):
        """Gets the ignore_recipients_from_payload of this CreateIntegrationAction.  # noqa: E501


        :return: The ignore_recipients_from_payload of this CreateIntegrationAction.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_recipients_from_payload

    @ignore_recipients_from_payload.setter
    def ignore_recipients_from_payload(self, ignore_recipients_from_payload):
        """Sets the ignore_recipients_from_payload of this CreateIntegrationAction.


        :param ignore_recipients_from_payload: The ignore_recipients_from_payload of this CreateIntegrationAction.  # noqa: E501
        :type: bool
        """

        self._ignore_recipients_from_payload = ignore_recipients_from_payload

    @property
    def ignore_teams_from_payload(self):
        """Gets the ignore_teams_from_payload of this CreateIntegrationAction.  # noqa: E501


        :return: The ignore_teams_from_payload of this CreateIntegrationAction.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_teams_from_payload

    @ignore_teams_from_payload.setter
    def ignore_teams_from_payload(self, ignore_teams_from_payload):
        """Sets the ignore_teams_from_payload of this CreateIntegrationAction.


        :param ignore_teams_from_payload: The ignore_teams_from_payload of this CreateIntegrationAction.  # noqa: E501
        :type: bool
        """

        self._ignore_teams_from_payload = ignore_teams_from_payload

    @property
    def tags(self):
        """Gets the tags of this CreateIntegrationAction.  # noqa: E501


        :return: The tags of this CreateIntegrationAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateIntegrationAction.


        :param tags: The tags of this CreateIntegrationAction.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def ignore_tags_from_payload(self):
        """Gets the ignore_tags_from_payload of this CreateIntegrationAction.  # noqa: E501


        :return: The ignore_tags_from_payload of this CreateIntegrationAction.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_tags_from_payload

    @ignore_tags_from_payload.setter
    def ignore_tags_from_payload(self, ignore_tags_from_payload):
        """Sets the ignore_tags_from_payload of this CreateIntegrationAction.


        :param ignore_tags_from_payload: The ignore_tags_from_payload of this CreateIntegrationAction.  # noqa: E501
        :type: bool
        """

        self._ignore_tags_from_payload = ignore_tags_from_payload

    @property
    def extra_properties(self):
        """Gets the extra_properties of this CreateIntegrationAction.  # noqa: E501


        :return: The extra_properties of this CreateIntegrationAction.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this CreateIntegrationAction.


        :param extra_properties: The extra_properties of this CreateIntegrationAction.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra_properties = extra_properties

    @property
    def ignore_extra_properties_from_payload(self):
        """Gets the ignore_extra_properties_from_payload of this CreateIntegrationAction.  # noqa: E501


        :return: The ignore_extra_properties_from_payload of this CreateIntegrationAction.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_extra_properties_from_payload

    @ignore_extra_properties_from_payload.setter
    def ignore_extra_properties_from_payload(self, ignore_extra_properties_from_payload):
        """Sets the ignore_extra_properties_from_payload of this CreateIntegrationAction.


        :param ignore_extra_properties_from_payload: The ignore_extra_properties_from_payload of this CreateIntegrationAction.  # noqa: E501
        :type: bool
        """

        self._ignore_extra_properties_from_payload = ignore_extra_properties_from_payload

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
        if not isinstance(other, CreateIntegrationAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
