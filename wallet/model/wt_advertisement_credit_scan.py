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
    from wallet.model.merchant_id import MerchantID
    from wallet.model.nano_id import NanoID
    from wallet.model.status import Status
    globals()['MerchantID'] = MerchantID
    globals()['NanoID'] = NanoID
    globals()['Status'] = Status


class WTAdvertisementCreditScan(ModelNormal):
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
        ('id',): {
            'max_length': 12,
            'min_length': 10,
        },
        ('redeemed_amount',): {
            'inclusive_minimum': 0,
        },
        ('refunded_amount',): {
            'inclusive_minimum': 0,
        },
        ('authorized_amount',): {
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
            'id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'transaction_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'register_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'redeemed_source': (str,),  # noqa: E501
            'redeemed_transaction_id': (str,),  # noqa: E501
            'redeemed_amount': (int,),  # noqa: E501
            'is_redeemed': (bool,),  # noqa: E501
            'refunded_transaction_id': (str,),  # noqa: E501
            'refunded_amount': (int,),  # noqa: E501
            'status': (Status,),  # noqa: E501
            'authorized_against_check_number': (str,),  # noqa: E501
            'authorized_amount': (int,),  # noqa: E501
            'merchant_id': (MerchantID,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'is_active': (bool,),  # noqa: E501
            'advertisement_credit_id': (NanoID,),  # noqa: E501
            'redeemed_amount_decimal': (str,),  # noqa: E501
            'redeemed_amount_string': (str,),  # noqa: E501
            'authorized_amount_decimal': (str,),  # noqa: E501
            'authorized_amount_string': (str,),  # noqa: E501
            'date_time_redeemed': (datetime, none_type,),  # noqa: E501
            'date_time_refunded': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'transaction_type': 'transactionType',  # noqa: E501
        'register_id': 'registerID',  # noqa: E501
        'redeemed_source': 'redeemedSource',  # noqa: E501
        'redeemed_transaction_id': 'redeemedTransactionID',  # noqa: E501
        'redeemed_amount': 'redeemedAmount',  # noqa: E501
        'is_redeemed': 'isRedeemed',  # noqa: E501
        'refunded_transaction_id': 'refundedTransactionID',  # noqa: E501
        'refunded_amount': 'refundedAmount',  # noqa: E501
        'status': 'status',  # noqa: E501
        'authorized_against_check_number': 'authorizedAgainstCheckNumber',  # noqa: E501
        'authorized_amount': 'authorizedAmount',  # noqa: E501
        'merchant_id': 'merchantID',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'is_active': 'isActive',  # noqa: E501
        'advertisement_credit_id': 'advertisementCreditID',  # noqa: E501
        'redeemed_amount_decimal': 'redeemedAmount_decimal',  # noqa: E501
        'redeemed_amount_string': 'redeemedAmount_string',  # noqa: E501
        'authorized_amount_decimal': 'authorizedAmount_decimal',  # noqa: E501
        'authorized_amount_string': 'authorizedAmount_string',  # noqa: E501
        'date_time_redeemed': 'dateTimeRedeemed',  # noqa: E501
        'date_time_refunded': 'dateTimeRefunded',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, transaction_type, register_id, redeemed_source, redeemed_transaction_id, redeemed_amount, is_redeemed, refunded_transaction_id, refunded_amount, status, authorized_against_check_number, authorized_amount, merchant_id, created_at, updated_at, is_active, advertisement_credit_id, redeemed_amount_decimal, redeemed_amount_string, authorized_amount_decimal, authorized_amount_string, date_time_redeemed, date_time_refunded, *args, **kwargs):  # noqa: E501
        """WTAdvertisementCreditScan - a model defined in OpenAPI

        Args:
            id (bool, date, datetime, dict, float, int, list, str, none_type):
            transaction_type (bool, date, datetime, dict, float, int, list, str, none_type): The type of the transaction - only redemption at the moment
            register_id (bool, date, datetime, dict, float, int, list, str, none_type): The ID of the register where the transaction occurred
            redeemed_source (str):
            redeemed_transaction_id (str):
            redeemed_amount (int):
            is_redeemed (bool):
            refunded_transaction_id (str):
            refunded_amount (int):
            status (Status):
            authorized_against_check_number (str):
            authorized_amount (int):
            merchant_id (MerchantID):
            created_at (datetime):
            updated_at (datetime):
            is_active (bool):
            advertisement_credit_id (NanoID):
            redeemed_amount_decimal (str):
            redeemed_amount_string (str):
            authorized_amount_decimal (str):
            authorized_amount_string (str):
            date_time_redeemed (datetime, none_type):
            date_time_refunded (datetime, none_type):

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

        self.id = id
        self.transaction_type = transaction_type
        self.register_id = register_id
        self.redeemed_source = redeemed_source
        self.redeemed_transaction_id = redeemed_transaction_id
        self.redeemed_amount = redeemed_amount
        self.is_redeemed = is_redeemed
        self.refunded_transaction_id = refunded_transaction_id
        self.refunded_amount = refunded_amount
        self.status = status
        self.authorized_against_check_number = authorized_against_check_number
        self.authorized_amount = authorized_amount
        self.merchant_id = merchant_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active
        self.advertisement_credit_id = advertisement_credit_id
        self.redeemed_amount_decimal = redeemed_amount_decimal
        self.redeemed_amount_string = redeemed_amount_string
        self.authorized_amount_decimal = authorized_amount_decimal
        self.authorized_amount_string = authorized_amount_string
        self.date_time_redeemed = date_time_redeemed
        self.date_time_refunded = date_time_refunded
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
    def __init__(self, id, transaction_type, register_id, redeemed_source, redeemed_transaction_id, redeemed_amount, is_redeemed, refunded_transaction_id, refunded_amount, status, authorized_against_check_number, authorized_amount, merchant_id, created_at, updated_at, is_active, advertisement_credit_id, redeemed_amount_decimal, redeemed_amount_string, authorized_amount_decimal, authorized_amount_string, date_time_redeemed, date_time_refunded, *args, **kwargs):  # noqa: E501
        """WTAdvertisementCreditScan - a model defined in OpenAPI

        Args:
            id (bool, date, datetime, dict, float, int, list, str, none_type):
            transaction_type (bool, date, datetime, dict, float, int, list, str, none_type): The type of the transaction - only redemption at the moment
            register_id (bool, date, datetime, dict, float, int, list, str, none_type): The ID of the register where the transaction occurred
            redeemed_source (str):
            redeemed_transaction_id (str):
            redeemed_amount (int):
            is_redeemed (bool):
            refunded_transaction_id (str):
            refunded_amount (int):
            status (Status):
            authorized_against_check_number (str):
            authorized_amount (int):
            merchant_id (MerchantID):
            created_at (datetime):
            updated_at (datetime):
            is_active (bool):
            advertisement_credit_id (NanoID):
            redeemed_amount_decimal (str):
            redeemed_amount_string (str):
            authorized_amount_decimal (str):
            authorized_amount_string (str):
            date_time_redeemed (datetime, none_type):
            date_time_refunded (datetime, none_type):

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

        self.id = id
        self.transaction_type = transaction_type
        self.register_id = register_id
        self.redeemed_source = redeemed_source
        self.redeemed_transaction_id = redeemed_transaction_id
        self.redeemed_amount = redeemed_amount
        self.is_redeemed = is_redeemed
        self.refunded_transaction_id = refunded_transaction_id
        self.refunded_amount = refunded_amount
        self.status = status
        self.authorized_against_check_number = authorized_against_check_number
        self.authorized_amount = authorized_amount
        self.merchant_id = merchant_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active
        self.advertisement_credit_id = advertisement_credit_id
        self.redeemed_amount_decimal = redeemed_amount_decimal
        self.redeemed_amount_string = redeemed_amount_string
        self.authorized_amount_decimal = authorized_amount_decimal
        self.authorized_amount_string = authorized_amount_string
        self.date_time_redeemed = date_time_redeemed
        self.date_time_refunded = date_time_refunded
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
