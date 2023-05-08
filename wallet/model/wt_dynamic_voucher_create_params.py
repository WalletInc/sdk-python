"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.533
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
    from wallet.model.nano_id import NanoID
    globals()['NanoID'] = NanoID


class WTDynamicVoucherCreateParams(ModelNormal):
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
        ('title',): {
            'min_length': 1,
        },
        ('starting_value',): {
            'inclusive_minimum': 0,
        },
        ('max_budget',): {
            'inclusive_minimum': 0,
        },
        ('decrease_amount',): {
            'inclusive_minimum': 0,
        },
        ('frequency',): {
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
            'title': (str,),  # noqa: E501
            'notes': (str,),  # noqa: E501
            'payment_design_id': (NanoID,),  # noqa: E501
            'date_time_start': (datetime,),  # noqa: E501
            'date_time_expiration': (datetime,),  # noqa: E501
            'starting_value': (int,),  # noqa: E501
            'max_budget': (int,),  # noqa: E501
            'decrease_amount': (int,),  # noqa: E501
            'frequency': (int,),  # noqa: E501
            'frequency_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'decrease_by': (float,),  # noqa: E501
            'decrease_every': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'title': 'title',  # noqa: E501
        'notes': 'notes',  # noqa: E501
        'payment_design_id': 'paymentDesignID',  # noqa: E501
        'date_time_start': 'dateTimeStart',  # noqa: E501
        'date_time_expiration': 'dateTimeExpiration',  # noqa: E501
        'starting_value': 'startingValue',  # noqa: E501
        'max_budget': 'maxBudget',  # noqa: E501
        'decrease_amount': 'decreaseAmount',  # noqa: E501
        'frequency': 'frequency',  # noqa: E501
        'frequency_type': 'frequencyType',  # noqa: E501
        'decrease_by': 'decreaseBy',  # noqa: E501
        'decrease_every': 'decreaseEvery',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, title, notes, payment_design_id, date_time_start, date_time_expiration, starting_value, max_budget, decrease_amount, frequency, frequency_type, *args, **kwargs):  # noqa: E501
        """WTDynamicVoucherCreateParams - a model defined in OpenAPI

        Args:
            title (str):
            notes (str):
            payment_design_id (NanoID):
            date_time_start (datetime):
            date_time_expiration (datetime):
            starting_value (int):
            max_budget (int):
            decrease_amount (int):
            frequency (int):
            frequency_type (bool, date, datetime, dict, float, int, list, str, none_type):

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
            decrease_by (float): [optional]  # noqa: E501
            decrease_every (float): [optional]  # noqa: E501
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

        self.title = title
        self.notes = notes
        self.payment_design_id = payment_design_id
        self.date_time_start = date_time_start
        self.date_time_expiration = date_time_expiration
        self.starting_value = starting_value
        self.max_budget = max_budget
        self.decrease_amount = decrease_amount
        self.frequency = frequency
        self.frequency_type = frequency_type
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
    def __init__(self, title, notes, payment_design_id, date_time_start, date_time_expiration, starting_value, max_budget, decrease_amount, frequency, frequency_type, *args, **kwargs):  # noqa: E501
        """WTDynamicVoucherCreateParams - a model defined in OpenAPI

        Args:
            title (str):
            notes (str):
            payment_design_id (NanoID):
            date_time_start (datetime):
            date_time_expiration (datetime):
            starting_value (int):
            max_budget (int):
            decrease_amount (int):
            frequency (int):
            frequency_type (bool, date, datetime, dict, float, int, list, str, none_type):

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
            decrease_by (float): [optional]  # noqa: E501
            decrease_every (float): [optional]  # noqa: E501
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

        self.title = title
        self.notes = notes
        self.payment_design_id = payment_design_id
        self.date_time_start = date_time_start
        self.date_time_expiration = date_time_expiration
        self.starting_value = starting_value
        self.max_budget = max_budget
        self.decrease_amount = decrease_amount
        self.frequency = frequency
        self.frequency_type = frequency_type
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
