"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.521
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
    from wallet.model.click_funnel_contact import ClickFunnelContact
    from wallet.model.click_funnel_original_amount import ClickFunnelOriginalAmount
    from wallet.model.click_funnel_product import ClickFunnelProduct
    globals()['ClickFunnelContact'] = ClickFunnelContact
    globals()['ClickFunnelOriginalAmount'] = ClickFunnelOriginalAmount
    globals()['ClickFunnelProduct'] = ClickFunnelProduct


class ClickFunnelPurchase(ModelNormal):
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
            'id': (float,),  # noqa: E501
            'products': ([ClickFunnelProduct],),  # noqa: E501
            'contact': (ClickFunnelContact,),  # noqa: E501
            'funnel_id': (float,),  # noqa: E501
            'stripe_customer_token': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'subscription_id': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'fulfillments': (dict,),  # noqa: E501
            'original_amount_cents': (float,),  # noqa: E501
            'original_amount': (ClickFunnelOriginalAmount,),  # noqa: E501
            'original_amount_currency': (str,),  # noqa: E501
            'manual': (bool,),  # noqa: E501
            'member_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'charge_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ctransreceipt': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'fulfillment_status': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'fulfillment_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'payments_count': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'infusionsoft_ccid': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'oap_customer_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'payment_instrument_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'error_message': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'nmi_customer_vault_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'products': 'products',  # noqa: E501
        'contact': 'contact',  # noqa: E501
        'funnel_id': 'funnel_id',  # noqa: E501
        'stripe_customer_token': 'stripe_customer_token',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'subscription_id': 'subscription_id',  # noqa: E501
        'status': 'status',  # noqa: E501
        'fulfillments': 'fulfillments',  # noqa: E501
        'original_amount_cents': 'original_amount_cents',  # noqa: E501
        'original_amount': 'original_amount',  # noqa: E501
        'original_amount_currency': 'original_amount_currency',  # noqa: E501
        'manual': 'manual',  # noqa: E501
        'member_id': 'member_id',  # noqa: E501
        'charge_id': 'charge_id',  # noqa: E501
        'ctransreceipt': 'ctransreceipt',  # noqa: E501
        'fulfillment_status': 'fulfillment_status',  # noqa: E501
        'fulfillment_id': 'fulfillment_id',  # noqa: E501
        'payments_count': 'payments_count',  # noqa: E501
        'infusionsoft_ccid': 'infusionsoft_ccid',  # noqa: E501
        'oap_customer_id': 'oap_customer_id',  # noqa: E501
        'payment_instrument_type': 'payment_instrument_type',  # noqa: E501
        'error_message': 'error_message',  # noqa: E501
        'nmi_customer_vault_id': 'nmi_customer_vault_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, products, contact, funnel_id, stripe_customer_token, created_at, updated_at, subscription_id, status, fulfillments, original_amount_cents, original_amount, original_amount_currency, manual, *args, **kwargs):  # noqa: E501
        """ClickFunnelPurchase - a model defined in OpenAPI

        Args:
            id (float):
            products ([ClickFunnelProduct]):
            contact (ClickFunnelContact):
            funnel_id (float):
            stripe_customer_token (str):
            created_at (datetime):
            updated_at (datetime):
            subscription_id (str):
            status (str):
            fulfillments (dict):
            original_amount_cents (float):
            original_amount (ClickFunnelOriginalAmount):
            original_amount_currency (str):
            manual (bool):

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
            member_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            charge_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ctransreceipt (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            fulfillment_status (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            fulfillment_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            payments_count (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            infusionsoft_ccid (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            oap_customer_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            payment_instrument_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            error_message (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            nmi_customer_vault_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
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
        self.products = products
        self.contact = contact
        self.funnel_id = funnel_id
        self.stripe_customer_token = stripe_customer_token
        self.created_at = created_at
        self.updated_at = updated_at
        self.subscription_id = subscription_id
        self.status = status
        self.fulfillments = fulfillments
        self.original_amount_cents = original_amount_cents
        self.original_amount = original_amount
        self.original_amount_currency = original_amount_currency
        self.manual = manual
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
    def __init__(self, id, products, contact, funnel_id, stripe_customer_token, created_at, updated_at, subscription_id, status, fulfillments, original_amount_cents, original_amount, original_amount_currency, manual, *args, **kwargs):  # noqa: E501
        """ClickFunnelPurchase - a model defined in OpenAPI

        Args:
            id (float):
            products ([ClickFunnelProduct]):
            contact (ClickFunnelContact):
            funnel_id (float):
            stripe_customer_token (str):
            created_at (datetime):
            updated_at (datetime):
            subscription_id (str):
            status (str):
            fulfillments (dict):
            original_amount_cents (float):
            original_amount (ClickFunnelOriginalAmount):
            original_amount_currency (str):
            manual (bool):

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
            member_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            charge_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ctransreceipt (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            fulfillment_status (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            fulfillment_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            payments_count (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            infusionsoft_ccid (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            oap_customer_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            payment_instrument_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            error_message (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            nmi_customer_vault_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
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
        self.products = products
        self.contact = contact
        self.funnel_id = funnel_id
        self.stripe_customer_token = stripe_customer_token
        self.created_at = created_at
        self.updated_at = updated_at
        self.subscription_id = subscription_id
        self.status = status
        self.fulfillments = fulfillments
        self.original_amount_cents = original_amount_cents
        self.original_amount = original_amount
        self.original_amount_currency = original_amount_currency
        self.manual = manual
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
