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
    from wallet.model.advertisement_credit import AdvertisementCredit
    from wallet.model.ss_nano_id import SSNanoID
    from wallet.model.wt_imported_list import WTImportedList
    from wallet.model.wt_opt_in_list import WTOptInList
    globals()['AdvertisementCredit'] = AdvertisementCredit
    globals()['SSNanoID'] = SSNanoID
    globals()['WTImportedList'] = WTImportedList
    globals()['WTOptInList'] = WTOptInList


class AdvertisementCreditBroadcast(ModelNormal):
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
        ('payment_object_prefix',): {
            'max_length': 2,
            'min_length': 2,
        },
        ('id',): {
            'max_length': 12,
            'min_length': 10,
        },
    }

    additional_properties_type = None

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
            'phone_number_id': (SSNanoID,),  # noqa: E501
            'payment_object_prefix': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'payment_object_id': (SSNanoID,),  # noqa: E501
            'message_template': (str,),  # noqa: E501
            'media_urls': ([str],),  # noqa: E501
            'employee_id': (SSNanoID,),  # noqa: E501
            'broadcast_scheduled_at': (datetime,),  # noqa: E501
            'id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'merchant_id': (SSNanoID,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'is_active': (bool,),  # noqa: E501
            'broadcast_status': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'broadcast_queued_at': (datetime, none_type,),  # noqa: E501
            'broadcast_started_at': (datetime, none_type,),  # noqa: E501
            'broadcast_completed_at': (datetime, none_type,),  # noqa: E501
            'list_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'list_id': (SSNanoID,),  # noqa: E501
            'advertisement_credit': (AdvertisementCredit,),  # noqa: E501
            'opt_in_list': (WTOptInList,),  # noqa: E501
            'imported_list': (WTImportedList,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'phone_number_id': 'phoneNumberID',  # noqa: E501
        'payment_object_prefix': 'paymentObjectPrefix',  # noqa: E501
        'payment_object_id': 'paymentObjectID',  # noqa: E501
        'message_template': 'messageTemplate',  # noqa: E501
        'media_urls': 'mediaURLs',  # noqa: E501
        'employee_id': 'employeeID',  # noqa: E501
        'broadcast_scheduled_at': 'broadcastScheduledAt',  # noqa: E501
        'id': 'id',  # noqa: E501
        'merchant_id': 'merchantID',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'is_active': 'isActive',  # noqa: E501
        'broadcast_status': 'broadcastStatus',  # noqa: E501
        'broadcast_queued_at': 'broadcastQueuedAt',  # noqa: E501
        'broadcast_started_at': 'broadcastStartedAt',  # noqa: E501
        'broadcast_completed_at': 'broadcastCompletedAt',  # noqa: E501
        'list_type': 'listType',  # noqa: E501
        'list_id': 'listID',  # noqa: E501
        'advertisement_credit': 'AdvertisementCredit',  # noqa: E501
        'opt_in_list': 'OptInList',  # noqa: E501
        'imported_list': 'ImportedList',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, phone_number_id, payment_object_prefix, payment_object_id, message_template, media_urls, employee_id, broadcast_scheduled_at, id, merchant_id, created_at, updated_at, is_active, broadcast_status, broadcast_queued_at, broadcast_started_at, broadcast_completed_at, list_type, list_id, advertisement_credit, *args, **kwargs):  # noqa: E501
        """AdvertisementCreditBroadcast - a model defined in OpenAPI

        Args:
            phone_number_id (SSNanoID):
            payment_object_prefix (bool, date, datetime, dict, float, int, list, str, none_type):
            payment_object_id (SSNanoID):
            message_template (str):
            media_urls ([str]):
            employee_id (SSNanoID):
            broadcast_scheduled_at (datetime):
            id (bool, date, datetime, dict, float, int, list, str, none_type):
            merchant_id (SSNanoID):
            created_at (datetime):
            updated_at (datetime):
            is_active (bool):
            broadcast_status (bool, date, datetime, dict, float, int, list, str, none_type):
            broadcast_queued_at (datetime, none_type):
            broadcast_started_at (datetime, none_type):
            broadcast_completed_at (datetime, none_type):
            list_type (bool, date, datetime, dict, float, int, list, str, none_type):
            list_id (SSNanoID):
            advertisement_credit (AdvertisementCredit):

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
            opt_in_list (WTOptInList): [optional]  # noqa: E501
            imported_list (WTImportedList): [optional]  # noqa: E501
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

        self.phone_number_id = phone_number_id
        self.payment_object_prefix = payment_object_prefix
        self.payment_object_id = payment_object_id
        self.message_template = message_template
        self.media_urls = media_urls
        self.employee_id = employee_id
        self.broadcast_scheduled_at = broadcast_scheduled_at
        self.id = id
        self.merchant_id = merchant_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active
        self.broadcast_status = broadcast_status
        self.broadcast_queued_at = broadcast_queued_at
        self.broadcast_started_at = broadcast_started_at
        self.broadcast_completed_at = broadcast_completed_at
        self.list_type = list_type
        self.list_id = list_id
        self.advertisement_credit = advertisement_credit
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
    def __init__(self, phone_number_id, payment_object_prefix, payment_object_id, message_template, media_urls, employee_id, broadcast_scheduled_at, id, merchant_id, created_at, updated_at, is_active, broadcast_status, broadcast_queued_at, broadcast_started_at, broadcast_completed_at, list_type, list_id, advertisement_credit, *args, **kwargs):  # noqa: E501
        """AdvertisementCreditBroadcast - a model defined in OpenAPI

        Args:
            phone_number_id (SSNanoID):
            payment_object_prefix (bool, date, datetime, dict, float, int, list, str, none_type):
            payment_object_id (SSNanoID):
            message_template (str):
            media_urls ([str]):
            employee_id (SSNanoID):
            broadcast_scheduled_at (datetime):
            id (bool, date, datetime, dict, float, int, list, str, none_type):
            merchant_id (SSNanoID):
            created_at (datetime):
            updated_at (datetime):
            is_active (bool):
            broadcast_status (bool, date, datetime, dict, float, int, list, str, none_type):
            broadcast_queued_at (datetime, none_type):
            broadcast_started_at (datetime, none_type):
            broadcast_completed_at (datetime, none_type):
            list_type (bool, date, datetime, dict, float, int, list, str, none_type):
            list_id (SSNanoID):
            advertisement_credit (AdvertisementCredit):

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
            opt_in_list (WTOptInList): [optional]  # noqa: E501
            imported_list (WTImportedList): [optional]  # noqa: E501
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

        self.phone_number_id = phone_number_id
        self.payment_object_prefix = payment_object_prefix
        self.payment_object_id = payment_object_id
        self.message_template = message_template
        self.media_urls = media_urls
        self.employee_id = employee_id
        self.broadcast_scheduled_at = broadcast_scheduled_at
        self.id = id
        self.merchant_id = merchant_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active
        self.broadcast_status = broadcast_status
        self.broadcast_queued_at = broadcast_queued_at
        self.broadcast_started_at = broadcast_started_at
        self.broadcast_completed_at = broadcast_completed_at
        self.list_type = list_type
        self.list_id = list_id
        self.advertisement_credit = advertisement_credit
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
