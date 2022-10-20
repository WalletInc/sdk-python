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



class WTDynamicVoucherSummary(ModelNormal):
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
        return {
            'calc_error': (bool,),  # noqa: E501
            'calc_error_details': (str,),  # noqa: E501
            'current_value': (float,),  # noqa: E501
            'current_value_decimal': (str,),  # noqa: E501
            'current_value_string': (str,),  # noqa: E501
            'time_value_zero': (bool,),  # noqa: E501
            'time_value_zero_subtracted_amount': (float,),  # noqa: E501
            'total_number_redeemed': (float,),  # noqa: E501
            'total_value_redeemed': (float,),  # noqa: E501
            'total_budget_remaining': (float,),  # noqa: E501
            'maximum_budget_exhausted': (bool,),  # noqa: E501
            'maximum_budget_exhausted_by': (float,),  # noqa: E501
            'maximum_budget_exhausted_by_decimal': (str,),  # noqa: E501
            'maximum_budget_exhausted_by_string': (str,),  # noqa: E501
            'maximum_budget_exhausted_total_value_redeemed': (float,),  # noqa: E501
            'maximum_budget_exhausted_total_value_redeemed_decimal': (str,),  # noqa: E501
            'maximum_budget_exhausted_total_value_redeemed_string': (str,),  # noqa: E501
            'total_amount_subtracted': (float,),  # noqa: E501
            'total_amount_subtracted_decimal': (str,),  # noqa: E501
            'total_amount_subtracted_string': (str,),  # noqa: E501
            'total_decremented_multiple': (float,),  # noqa: E501
            'redeemed_keys': ([str],),  # noqa: E501
            'status': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'expired': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'calc_error': 'calcError',  # noqa: E501
        'calc_error_details': 'calcErrorDetails',  # noqa: E501
        'current_value': 'currentValue',  # noqa: E501
        'current_value_decimal': 'currentValue_decimal',  # noqa: E501
        'current_value_string': 'currentValue_string',  # noqa: E501
        'time_value_zero': 'timeValueZero',  # noqa: E501
        'time_value_zero_subtracted_amount': 'timeValueZeroSubtractedAmount',  # noqa: E501
        'total_number_redeemed': 'totalNumberRedeemed',  # noqa: E501
        'total_value_redeemed': 'totalValueRedeemed',  # noqa: E501
        'total_budget_remaining': 'totalBudgetRemaining',  # noqa: E501
        'maximum_budget_exhausted': 'maximumBudgetExhausted',  # noqa: E501
        'maximum_budget_exhausted_by': 'maximumBudgetExhaustedBy',  # noqa: E501
        'maximum_budget_exhausted_by_decimal': 'maximumBudgetExhaustedBy_decimal',  # noqa: E501
        'maximum_budget_exhausted_by_string': 'maximumBudgetExhaustedBy_string',  # noqa: E501
        'maximum_budget_exhausted_total_value_redeemed': 'maximumBudgetExhaustedTotalValueRedeemed',  # noqa: E501
        'maximum_budget_exhausted_total_value_redeemed_decimal': 'maximumBudgetExhaustedTotalValueRedeemed_decimal',  # noqa: E501
        'maximum_budget_exhausted_total_value_redeemed_string': 'maximumBudgetExhaustedTotalValueRedeemed_string',  # noqa: E501
        'total_amount_subtracted': 'totalAmountSubtracted',  # noqa: E501
        'total_amount_subtracted_decimal': 'totalAmountSubtracted_decimal',  # noqa: E501
        'total_amount_subtracted_string': 'totalAmountSubtracted_string',  # noqa: E501
        'total_decremented_multiple': 'totalDecrementedMultiple',  # noqa: E501
        'redeemed_keys': 'redeemedKeys',  # noqa: E501
        'status': 'status',  # noqa: E501
        'expired': 'expired',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, calc_error, calc_error_details, current_value, current_value_decimal, current_value_string, time_value_zero, time_value_zero_subtracted_amount, total_number_redeemed, total_value_redeemed, total_budget_remaining, maximum_budget_exhausted, maximum_budget_exhausted_by, maximum_budget_exhausted_by_decimal, maximum_budget_exhausted_by_string, maximum_budget_exhausted_total_value_redeemed, maximum_budget_exhausted_total_value_redeemed_decimal, maximum_budget_exhausted_total_value_redeemed_string, total_amount_subtracted, total_amount_subtracted_decimal, total_amount_subtracted_string, total_decremented_multiple, redeemed_keys, status, expired, *args, **kwargs):  # noqa: E501
        """WTDynamicVoucherSummary - a model defined in OpenAPI

        Args:
            calc_error (bool):
            calc_error_details (str):
            current_value (float):
            current_value_decimal (str):
            current_value_string (str):
            time_value_zero (bool):
            time_value_zero_subtracted_amount (float):
            total_number_redeemed (float):
            total_value_redeemed (float):
            total_budget_remaining (float):
            maximum_budget_exhausted (bool):
            maximum_budget_exhausted_by (float):
            maximum_budget_exhausted_by_decimal (str):
            maximum_budget_exhausted_by_string (str):
            maximum_budget_exhausted_total_value_redeemed (float):
            maximum_budget_exhausted_total_value_redeemed_decimal (str):
            maximum_budget_exhausted_total_value_redeemed_string (str):
            total_amount_subtracted (float):
            total_amount_subtracted_decimal (str):
            total_amount_subtracted_string (str):
            total_decremented_multiple (float):
            redeemed_keys ([str]):
            status (bool, date, datetime, dict, float, int, list, str, none_type):
            expired (bool):

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

        self.calc_error = calc_error
        self.calc_error_details = calc_error_details
        self.current_value = current_value
        self.current_value_decimal = current_value_decimal
        self.current_value_string = current_value_string
        self.time_value_zero = time_value_zero
        self.time_value_zero_subtracted_amount = time_value_zero_subtracted_amount
        self.total_number_redeemed = total_number_redeemed
        self.total_value_redeemed = total_value_redeemed
        self.total_budget_remaining = total_budget_remaining
        self.maximum_budget_exhausted = maximum_budget_exhausted
        self.maximum_budget_exhausted_by = maximum_budget_exhausted_by
        self.maximum_budget_exhausted_by_decimal = maximum_budget_exhausted_by_decimal
        self.maximum_budget_exhausted_by_string = maximum_budget_exhausted_by_string
        self.maximum_budget_exhausted_total_value_redeemed = maximum_budget_exhausted_total_value_redeemed
        self.maximum_budget_exhausted_total_value_redeemed_decimal = maximum_budget_exhausted_total_value_redeemed_decimal
        self.maximum_budget_exhausted_total_value_redeemed_string = maximum_budget_exhausted_total_value_redeemed_string
        self.total_amount_subtracted = total_amount_subtracted
        self.total_amount_subtracted_decimal = total_amount_subtracted_decimal
        self.total_amount_subtracted_string = total_amount_subtracted_string
        self.total_decremented_multiple = total_decremented_multiple
        self.redeemed_keys = redeemed_keys
        self.status = status
        self.expired = expired
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
    def __init__(self, calc_error, calc_error_details, current_value, current_value_decimal, current_value_string, time_value_zero, time_value_zero_subtracted_amount, total_number_redeemed, total_value_redeemed, total_budget_remaining, maximum_budget_exhausted, maximum_budget_exhausted_by, maximum_budget_exhausted_by_decimal, maximum_budget_exhausted_by_string, maximum_budget_exhausted_total_value_redeemed, maximum_budget_exhausted_total_value_redeemed_decimal, maximum_budget_exhausted_total_value_redeemed_string, total_amount_subtracted, total_amount_subtracted_decimal, total_amount_subtracted_string, total_decremented_multiple, redeemed_keys, status, expired, *args, **kwargs):  # noqa: E501
        """WTDynamicVoucherSummary - a model defined in OpenAPI

        Args:
            calc_error (bool):
            calc_error_details (str):
            current_value (float):
            current_value_decimal (str):
            current_value_string (str):
            time_value_zero (bool):
            time_value_zero_subtracted_amount (float):
            total_number_redeemed (float):
            total_value_redeemed (float):
            total_budget_remaining (float):
            maximum_budget_exhausted (bool):
            maximum_budget_exhausted_by (float):
            maximum_budget_exhausted_by_decimal (str):
            maximum_budget_exhausted_by_string (str):
            maximum_budget_exhausted_total_value_redeemed (float):
            maximum_budget_exhausted_total_value_redeemed_decimal (str):
            maximum_budget_exhausted_total_value_redeemed_string (str):
            total_amount_subtracted (float):
            total_amount_subtracted_decimal (str):
            total_amount_subtracted_string (str):
            total_decremented_multiple (float):
            redeemed_keys ([str]):
            status (bool, date, datetime, dict, float, int, list, str, none_type):
            expired (bool):

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

        self.calc_error = calc_error
        self.calc_error_details = calc_error_details
        self.current_value = current_value
        self.current_value_decimal = current_value_decimal
        self.current_value_string = current_value_string
        self.time_value_zero = time_value_zero
        self.time_value_zero_subtracted_amount = time_value_zero_subtracted_amount
        self.total_number_redeemed = total_number_redeemed
        self.total_value_redeemed = total_value_redeemed
        self.total_budget_remaining = total_budget_remaining
        self.maximum_budget_exhausted = maximum_budget_exhausted
        self.maximum_budget_exhausted_by = maximum_budget_exhausted_by
        self.maximum_budget_exhausted_by_decimal = maximum_budget_exhausted_by_decimal
        self.maximum_budget_exhausted_by_string = maximum_budget_exhausted_by_string
        self.maximum_budget_exhausted_total_value_redeemed = maximum_budget_exhausted_total_value_redeemed
        self.maximum_budget_exhausted_total_value_redeemed_decimal = maximum_budget_exhausted_total_value_redeemed_decimal
        self.maximum_budget_exhausted_total_value_redeemed_string = maximum_budget_exhausted_total_value_redeemed_string
        self.total_amount_subtracted = total_amount_subtracted
        self.total_amount_subtracted_decimal = total_amount_subtracted_decimal
        self.total_amount_subtracted_string = total_amount_subtracted_string
        self.total_decremented_multiple = total_decremented_multiple
        self.redeemed_keys = redeemed_keys
        self.status = status
        self.expired = expired
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
