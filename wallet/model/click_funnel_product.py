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
    from wallet.model.click_funnel_amount import ClickFunnelAmount
    globals()['ClickFunnelAmount'] = ClickFunnelAmount


class ClickFunnelProduct(ModelNormal):
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
            'name': (str,),  # noqa: E501
            'stripe_plan': (str,),  # noqa: E501
            'amount': (ClickFunnelAmount,),  # noqa: E501
            'amount_currency': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'subject': (str,),  # noqa: E501
            'html_body': (str,),  # noqa: E501
            'thank_you_page_id': (float,),  # noqa: E501
            'bump': (bool,),  # noqa: E501
            'billing_integration': (str,),  # noqa: E501
            'commissionable': (bool,),  # noqa: E501
            'statement_descriptor': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'stripe_cancel_after_payments': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'cart_product_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'infusionsoft_product_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'infusionsoft_subscription_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ontraport_product_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ontraport_payment_count': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ontraport_payment_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ontraport_unit': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ontraport_gateway_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ontraport_invoice_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'netsuite_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'netsuite_tag': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'netsuite_class': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'stripe_plan': 'stripe_plan',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'amount_currency': 'amount_currency',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'subject': 'subject',  # noqa: E501
        'html_body': 'html_body',  # noqa: E501
        'thank_you_page_id': 'thank_you_page_id',  # noqa: E501
        'bump': 'bump',  # noqa: E501
        'billing_integration': 'billing_integration',  # noqa: E501
        'commissionable': 'commissionable',  # noqa: E501
        'statement_descriptor': 'statement_descriptor',  # noqa: E501
        'description': 'description',  # noqa: E501
        'stripe_cancel_after_payments': 'stripe_cancel_after_payments',  # noqa: E501
        'cart_product_id': 'cart_product_id',  # noqa: E501
        'infusionsoft_product_id': 'infusionsoft_product_id',  # noqa: E501
        'infusionsoft_subscription_id': 'infusionsoft_subscription_id',  # noqa: E501
        'ontraport_product_id': 'ontraport_product_id',  # noqa: E501
        'ontraport_payment_count': 'ontraport_payment_count',  # noqa: E501
        'ontraport_payment_type': 'ontraport_payment_type',  # noqa: E501
        'ontraport_unit': 'ontraport_unit',  # noqa: E501
        'ontraport_gateway_id': 'ontraport_gateway_id',  # noqa: E501
        'ontraport_invoice_id': 'ontraport_invoice_id',  # noqa: E501
        'netsuite_id': 'netsuite_id',  # noqa: E501
        'netsuite_tag': 'netsuite_tag',  # noqa: E501
        'netsuite_class': 'netsuite_class',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, name, stripe_plan, amount, amount_currency, created_at, updated_at, subject, html_body, thank_you_page_id, bump, billing_integration, commissionable, statement_descriptor, description, *args, **kwargs):  # noqa: E501
        """ClickFunnelProduct - a model defined in OpenAPI

        Args:
            id (float):
            name (str):
            stripe_plan (str):
            amount (ClickFunnelAmount):
            amount_currency (str):
            created_at (datetime):
            updated_at (datetime):
            subject (str):
            html_body (str):
            thank_you_page_id (float):
            bump (bool):
            billing_integration (str):
            commissionable (bool):
            statement_descriptor (str):
            description (str):

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
            stripe_cancel_after_payments (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            cart_product_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            infusionsoft_product_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            infusionsoft_subscription_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_product_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_payment_count (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_payment_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_unit (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_gateway_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_invoice_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            netsuite_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            netsuite_tag (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            netsuite_class (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
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
        self.name = name
        self.stripe_plan = stripe_plan
        self.amount = amount
        self.amount_currency = amount_currency
        self.created_at = created_at
        self.updated_at = updated_at
        self.subject = subject
        self.html_body = html_body
        self.thank_you_page_id = thank_you_page_id
        self.bump = bump
        self.billing_integration = billing_integration
        self.commissionable = commissionable
        self.statement_descriptor = statement_descriptor
        self.description = description
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
    def __init__(self, id, name, stripe_plan, amount, amount_currency, created_at, updated_at, subject, html_body, thank_you_page_id, bump, billing_integration, commissionable, statement_descriptor, description, *args, **kwargs):  # noqa: E501
        """ClickFunnelProduct - a model defined in OpenAPI

        Args:
            id (float):
            name (str):
            stripe_plan (str):
            amount (ClickFunnelAmount):
            amount_currency (str):
            created_at (datetime):
            updated_at (datetime):
            subject (str):
            html_body (str):
            thank_you_page_id (float):
            bump (bool):
            billing_integration (str):
            commissionable (bool):
            statement_descriptor (str):
            description (str):

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
            stripe_cancel_after_payments (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            cart_product_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            infusionsoft_product_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            infusionsoft_subscription_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_product_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_payment_count (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_payment_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_unit (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_gateway_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            ontraport_invoice_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            netsuite_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            netsuite_tag (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            netsuite_class (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
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
        self.name = name
        self.stripe_plan = stripe_plan
        self.amount = amount
        self.amount_currency = amount_currency
        self.created_at = created_at
        self.updated_at = updated_at
        self.subject = subject
        self.html_body = html_body
        self.thank_you_page_id = thank_you_page_id
        self.bump = bump
        self.billing_integration = billing_integration
        self.commissionable = commissionable
        self.statement_descriptor = statement_descriptor
        self.description = description
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
