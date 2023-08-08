"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.535
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from wallet.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from wallet.exceptions import ApiAttributeError


def lazy_import():
    from wallet.model.message_direction import MessageDirection
    from wallet.model.message_status import MessageStatus
    globals()['MessageDirection'] = MessageDirection
    globals()['MessageStatus'] = MessageStatus


class WTMessageInstance(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'subresource_uris': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'api_version': (str,),  # noqa: E501
            'price_unit': (str,),  # noqa: E501
            'error_code': (float,),  # noqa: E501
            'date_created': (datetime,),  # noqa: E501
            'date_sent': (datetime,),  # noqa: E501
            'sid': (str,),  # noqa: E501
            'messaging_service_sid': (str,),  # noqa: E501
            'status': (MessageStatus,),  # noqa: E501
            'num_media': (str,),  # noqa: E501
            'account_sid': (str,),  # noqa: E501
            'uri': (str,),  # noqa: E501
            'error_message': (str,),  # noqa: E501
            'price': (str,),  # noqa: E501
            'date_updated': (datetime,),  # noqa: E501
            'to': (str,),  # noqa: E501
            '_from': (str,),  # noqa: E501
            'direction': (MessageDirection,),  # noqa: E501
            'num_segments': (str,),  # noqa: E501
            'body': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'subresource_uris': 'subresourceUris',  # noqa: E501
        'api_version': 'apiVersion',  # noqa: E501
        'price_unit': 'priceUnit',  # noqa: E501
        'error_code': 'errorCode',  # noqa: E501
        'date_created': 'dateCreated',  # noqa: E501
        'date_sent': 'dateSent',  # noqa: E501
        'sid': 'sid',  # noqa: E501
        'messaging_service_sid': 'messagingServiceSid',  # noqa: E501
        'status': 'status',  # noqa: E501
        'num_media': 'numMedia',  # noqa: E501
        'account_sid': 'accountSid',  # noqa: E501
        'uri': 'uri',  # noqa: E501
        'error_message': 'errorMessage',  # noqa: E501
        'price': 'price',  # noqa: E501
        'date_updated': 'dateUpdated',  # noqa: E501
        'to': 'to',  # noqa: E501
        '_from': 'from',  # noqa: E501
        'direction': 'direction',  # noqa: E501
        'num_segments': 'numSegments',  # noqa: E501
        'body': 'body',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, subresource_uris, api_version, price_unit, error_code, date_created, date_sent, sid, messaging_service_sid, status, num_media, account_sid, uri, error_message, price, date_updated, to, _from, direction, num_segments, body, *args, **kwargs):  # noqa: E501
        """WTMessageInstance - a model defined in OpenAPI

        Args:
            subresource_uris ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Construct a type with a set of properties K of type T
            api_version (str):
            price_unit (str):
            error_code (float):
            date_created (datetime):
            date_sent (datetime):
            sid (str):
            messaging_service_sid (str):
            status (MessageStatus):
            num_media (str):
            account_sid (str):
            uri (str):
            error_message (str):
            price (str):
            date_updated (datetime):
            to (str):
            _from (str):
            direction (MessageDirection):
            num_segments (str):
            body (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.subresource_uris = subresource_uris
        self.api_version = api_version
        self.price_unit = price_unit
        self.error_code = error_code
        self.date_created = date_created
        self.date_sent = date_sent
        self.sid = sid
        self.messaging_service_sid = messaging_service_sid
        self.status = status
        self.num_media = num_media
        self.account_sid = account_sid
        self.uri = uri
        self.error_message = error_message
        self.price = price
        self.date_updated = date_updated
        self.to = to
        self._from = _from
        self.direction = direction
        self.num_segments = num_segments
        self.body = body
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, subresource_uris, api_version, price_unit, error_code, date_created, date_sent, sid, messaging_service_sid, status, num_media, account_sid, uri, error_message, price, date_updated, to, _from, direction, num_segments, body, *args, **kwargs):  # noqa: E501
        """WTMessageInstance - a model defined in OpenAPI

        Args:
            subresource_uris ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Construct a type with a set of properties K of type T
            api_version (str):
            price_unit (str):
            error_code (float):
            date_created (datetime):
            date_sent (datetime):
            sid (str):
            messaging_service_sid (str):
            status (MessageStatus):
            num_media (str):
            account_sid (str):
            uri (str):
            error_message (str):
            price (str):
            date_updated (datetime):
            to (str):
            _from (str):
            direction (MessageDirection):
            num_segments (str):
            body (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.subresource_uris = subresource_uris
        self.api_version = api_version
        self.price_unit = price_unit
        self.error_code = error_code
        self.date_created = date_created
        self.date_sent = date_sent
        self.sid = sid
        self.messaging_service_sid = messaging_service_sid
        self.status = status
        self.num_media = num_media
        self.account_sid = account_sid
        self.uri = uri
        self.error_message = error_message
        self.price = price
        self.date_updated = date_updated
        self.to = to
        self._from = _from
        self.direction = direction
        self.num_segments = num_segments
        self.body = body
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")