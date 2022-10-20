"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.515
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
    from wallet.model.merchant_id import MerchantID
    from wallet.model.nano_id import NanoID
    from wallet.model.vs_dynamic_voucher_status import VSDynamicVoucherStatus
    globals()['MerchantID'] = MerchantID
    globals()['NanoID'] = NanoID
    globals()['VSDynamicVoucherStatus'] = VSDynamicVoucherStatus


class WTDynamicVoucherRedemption(ModelNormal):
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
        ('session_key',): {
        },
        ('redeemed_amount',): {
            'inclusive_minimum': 0,
        },
        ('id',): {
            'max_length': 12,
            'min_length': 10,
        },
        ('refunded_amount',): {
            'inclusive_minimum': 0,
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
            'session_key': (str,),  # noqa: E501
            'redeemed_amount': (int,),  # noqa: E501
            'dynamic_voucher_id': (NanoID,),  # noqa: E501
            'redeemed_source': (str,),  # noqa: E501
            'redeemed_transaction_id': (str,),  # noqa: E501
            'transaction_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'register_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'merchant_id': (MerchantID,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'is_active': (bool,),  # noqa: E501
            'refunded_transaction_id': (str,),  # noqa: E501
            'refunded_amount': (int,),  # noqa: E501
            'status': (VSDynamicVoucherStatus,),  # noqa: E501
            'redeemed_amount_decimal': (str,),  # noqa: E501
            'redeemed_amount_string': (str,),  # noqa: E501
            'discount_received': (str,),  # noqa: E501
            'meta_value': (str,),  # noqa: E501
            'parent_object_id': (NanoID,),  # noqa: E501
            'redeemed_at': (datetime, none_type,),  # noqa: E501
            'refunded_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'session_key': 'sessionKey',  # noqa: E501
        'redeemed_amount': 'redeemedAmount',  # noqa: E501
        'dynamic_voucher_id': 'dynamicVoucherID',  # noqa: E501
        'redeemed_source': 'redeemedSource',  # noqa: E501
        'redeemed_transaction_id': 'redeemedTransactionID',  # noqa: E501
        'transaction_type': 'transactionType',  # noqa: E501
        'register_id': 'registerID',  # noqa: E501
        'id': 'id',  # noqa: E501
        'merchant_id': 'merchantID',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'is_active': 'isActive',  # noqa: E501
        'refunded_transaction_id': 'refundedTransactionID',  # noqa: E501
        'refunded_amount': 'refundedAmount',  # noqa: E501
        'status': 'status',  # noqa: E501
        'redeemed_amount_decimal': 'redeemedAmount_decimal',  # noqa: E501
        'redeemed_amount_string': 'redeemedAmount_string',  # noqa: E501
        'discount_received': 'discountReceived',  # noqa: E501
        'meta_value': 'metaValue',  # noqa: E501
        'parent_object_id': 'parentObjectID',  # noqa: E501
        'redeemed_at': 'redeemedAt',  # noqa: E501
        'refunded_at': 'refundedAt',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, session_key, redeemed_amount, dynamic_voucher_id, redeemed_source, redeemed_transaction_id, transaction_type, register_id, id, merchant_id, created_at, updated_at, is_active, refunded_transaction_id, refunded_amount, status, redeemed_amount_decimal, redeemed_amount_string, discount_received, meta_value, parent_object_id, *args, **kwargs):  # noqa: E501
        """WTDynamicVoucherRedemption - a model defined in OpenAPI

        Args:
            session_key (str):
            redeemed_amount (int):
            dynamic_voucher_id (NanoID):
            redeemed_source (str):
            redeemed_transaction_id (str):
            transaction_type (bool, date, datetime, dict, float, int, list, str, none_type): The type of the transaction - only redemption at the moment
            register_id (bool, date, datetime, dict, float, int, list, str, none_type): The ID of the register where the transaction occurred
            id (bool, date, datetime, dict, float, int, list, str, none_type):
            merchant_id (MerchantID):
            created_at (datetime):
            updated_at (datetime):
            is_active (bool):
            refunded_transaction_id (str):
            refunded_amount (int):
            status (VSDynamicVoucherStatus):
            redeemed_amount_decimal (str):
            redeemed_amount_string (str):
            discount_received (str):
            meta_value (str):
            parent_object_id (NanoID):

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
            redeemed_at (datetime, none_type): [optional]  # noqa: E501
            refunded_at (datetime, none_type): [optional]  # noqa: E501
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

        self.session_key = session_key
        self.redeemed_amount = redeemed_amount
        self.dynamic_voucher_id = dynamic_voucher_id
        self.redeemed_source = redeemed_source
        self.redeemed_transaction_id = redeemed_transaction_id
        self.transaction_type = transaction_type
        self.register_id = register_id
        self.id = id
        self.merchant_id = merchant_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active
        self.refunded_transaction_id = refunded_transaction_id
        self.refunded_amount = refunded_amount
        self.status = status
        self.redeemed_amount_decimal = redeemed_amount_decimal
        self.redeemed_amount_string = redeemed_amount_string
        self.discount_received = discount_received
        self.meta_value = meta_value
        self.parent_object_id = parent_object_id
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
    def __init__(self, session_key, redeemed_amount, dynamic_voucher_id, redeemed_source, redeemed_transaction_id, transaction_type, register_id, id, merchant_id, created_at, updated_at, is_active, refunded_transaction_id, refunded_amount, status, redeemed_amount_decimal, redeemed_amount_string, discount_received, meta_value, parent_object_id, *args, **kwargs):  # noqa: E501
        """WTDynamicVoucherRedemption - a model defined in OpenAPI

        Args:
            session_key (str):
            redeemed_amount (int):
            dynamic_voucher_id (NanoID):
            redeemed_source (str):
            redeemed_transaction_id (str):
            transaction_type (bool, date, datetime, dict, float, int, list, str, none_type): The type of the transaction - only redemption at the moment
            register_id (bool, date, datetime, dict, float, int, list, str, none_type): The ID of the register where the transaction occurred
            id (bool, date, datetime, dict, float, int, list, str, none_type):
            merchant_id (MerchantID):
            created_at (datetime):
            updated_at (datetime):
            is_active (bool):
            refunded_transaction_id (str):
            refunded_amount (int):
            status (VSDynamicVoucherStatus):
            redeemed_amount_decimal (str):
            redeemed_amount_string (str):
            discount_received (str):
            meta_value (str):
            parent_object_id (NanoID):

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
            redeemed_at (datetime, none_type): [optional]  # noqa: E501
            refunded_at (datetime, none_type): [optional]  # noqa: E501
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

        self.session_key = session_key
        self.redeemed_amount = redeemed_amount
        self.dynamic_voucher_id = dynamic_voucher_id
        self.redeemed_source = redeemed_source
        self.redeemed_transaction_id = redeemed_transaction_id
        self.transaction_type = transaction_type
        self.register_id = register_id
        self.id = id
        self.merchant_id = merchant_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active
        self.refunded_transaction_id = refunded_transaction_id
        self.refunded_amount = refunded_amount
        self.status = status
        self.redeemed_amount_decimal = redeemed_amount_decimal
        self.redeemed_amount_string = redeemed_amount_string
        self.discount_received = discount_received
        self.meta_value = meta_value
        self.parent_object_id = parent_object_id
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
