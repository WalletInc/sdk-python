"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.523
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



class ReachPerformanceStats(ModelNormal):
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
        ('sent_count',): {
            'inclusive_minimum': 0,
        },
        ('delivered_count',): {
            'inclusive_minimum': 0,
        },
        ('failed_count',): {
            'inclusive_minimum': 0,
        },
        ('undelivered_count',): {
            'inclusive_minimum': 0,
        },
        ('viewed_count',): {
            'inclusive_minimum': 0,
        },
        ('redemptions_count',): {
            'inclusive_minimum': 0,
        },
        ('value_claimed',): {
            'inclusive_minimum': 0,
        },
        ('revenue_generated',): {
            'inclusive_minimum': 0,
        },
        ('refunds_count',): {
            'inclusive_minimum': 0,
        },
        ('value_refunded',): {
            'inclusive_minimum': 0,
        },
        ('revenue_lost',): {
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
        return {
            'sent_count': (int,),  # noqa: E501
            'delivered_count': (int,),  # noqa: E501
            'failed_count': (int,),  # noqa: E501
            'undelivered_count': (int,),  # noqa: E501
            'viewed_count': (int,),  # noqa: E501
            'redemptions_count': (int,),  # noqa: E501
            'value_claimed': (int,),  # noqa: E501
            'revenue_generated': (int,),  # noqa: E501
            'refunds_count': (int,),  # noqa: E501
            'value_refunded': (int,),  # noqa: E501
            'revenue_lost': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'sent_count': 'sentCount',  # noqa: E501
        'delivered_count': 'deliveredCount',  # noqa: E501
        'failed_count': 'failedCount',  # noqa: E501
        'undelivered_count': 'undeliveredCount',  # noqa: E501
        'viewed_count': 'viewedCount',  # noqa: E501
        'redemptions_count': 'redemptionsCount',  # noqa: E501
        'value_claimed': 'valueClaimed',  # noqa: E501
        'revenue_generated': 'revenueGenerated',  # noqa: E501
        'refunds_count': 'refundsCount',  # noqa: E501
        'value_refunded': 'valueRefunded',  # noqa: E501
        'revenue_lost': 'revenueLost',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, sent_count, delivered_count, failed_count, undelivered_count, viewed_count, redemptions_count, value_claimed, revenue_generated, refunds_count, value_refunded, revenue_lost, *args, **kwargs):  # noqa: E501
        """ReachPerformanceStats - a model defined in OpenAPI

        Args:
            sent_count (int): Denotes the number of SMSes sent
            delivered_count (int): Denotes the number of SMSes delivered
            failed_count (int): Denotes the number of SMSes that have failed to deliver
            undelivered_count (int): Denotes the number of SMSes that were undelivered
            viewed_count (int): Denotes the count of SMSes viewed (by clicking on the link sent as part of the SMS)
            redemptions_count (int): Denotes the count of redemptions
            value_claimed (int): Denotes the total value claimed as discounts (in cents)
            revenue_generated (int): Denotes the total revenue generated for the business by using various payment objects (in cents)
            refunds_count (int): Denotes the count of refunds
            value_refunded (int): Denotes the total value refunded (in the form of discounts, in cents)
            revenue_lost (int): Denotes the total revenue lost for the business on account of refunds (in cents)

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

        self.sent_count = sent_count
        self.delivered_count = delivered_count
        self.failed_count = failed_count
        self.undelivered_count = undelivered_count
        self.viewed_count = viewed_count
        self.redemptions_count = redemptions_count
        self.value_claimed = value_claimed
        self.revenue_generated = revenue_generated
        self.refunds_count = refunds_count
        self.value_refunded = value_refunded
        self.revenue_lost = revenue_lost
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
    def __init__(self, sent_count, delivered_count, failed_count, undelivered_count, viewed_count, redemptions_count, value_claimed, revenue_generated, refunds_count, value_refunded, revenue_lost, *args, **kwargs):  # noqa: E501
        """ReachPerformanceStats - a model defined in OpenAPI

        Args:
            sent_count (int): Denotes the number of SMSes sent
            delivered_count (int): Denotes the number of SMSes delivered
            failed_count (int): Denotes the number of SMSes that have failed to deliver
            undelivered_count (int): Denotes the number of SMSes that were undelivered
            viewed_count (int): Denotes the count of SMSes viewed (by clicking on the link sent as part of the SMS)
            redemptions_count (int): Denotes the count of redemptions
            value_claimed (int): Denotes the total value claimed as discounts (in cents)
            revenue_generated (int): Denotes the total revenue generated for the business by using various payment objects (in cents)
            refunds_count (int): Denotes the count of refunds
            value_refunded (int): Denotes the total value refunded (in the form of discounts, in cents)
            revenue_lost (int): Denotes the total revenue lost for the business on account of refunds (in cents)

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

        self.sent_count = sent_count
        self.delivered_count = delivered_count
        self.failed_count = failed_count
        self.undelivered_count = undelivered_count
        self.viewed_count = viewed_count
        self.redemptions_count = redemptions_count
        self.value_claimed = value_claimed
        self.revenue_generated = revenue_generated
        self.refunds_count = refunds_count
        self.value_refunded = value_refunded
        self.revenue_lost = revenue_lost
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
