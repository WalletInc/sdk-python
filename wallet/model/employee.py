"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.527
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
    globals()['MerchantID'] = MerchantID
    globals()['NanoID'] = NanoID


class Employee(ModelNormal):
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
        ('first_name',): {
            'min_length': 1,
        },
        ('last_name',): {
            'min_length': 1,
        },
        ('email',): {
            'min_length': 1,
        },
        ('employee_id',): {
            'min_length': 0,
        },
        ('job_title',): {
            'min_length': 0,
        },
        ('department',): {
            'min_length': 0,
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
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'phone_number': (str,),  # noqa: E501
            'is_public_representative': (bool,),  # noqa: E501
            'wallet_sequence_number': (int,),  # noqa: E501
            'employee_id': (str,),  # noqa: E501
            'job_title': (str,),  # noqa: E501
            'department': (str,),  # noqa: E501
            'id': (NanoID,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'username': (str,),  # noqa: E501
            'email_verified': (str,),  # noqa: E501
            'profile_picture_url': (str,),  # noqa: E501
            'merchant_id': (MerchantID,),  # noqa: E501
            'session_token': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'first_name': 'firstName',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'email': 'email',  # noqa: E501
        'phone_number': 'phoneNumber',  # noqa: E501
        'is_public_representative': 'isPublicRepresentative',  # noqa: E501
        'wallet_sequence_number': 'walletSequenceNumber',  # noqa: E501
        'employee_id': 'employeeID',  # noqa: E501
        'job_title': 'jobTitle',  # noqa: E501
        'department': 'department',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'username': 'username',  # noqa: E501
        'email_verified': 'emailVerified',  # noqa: E501
        'profile_picture_url': 'profilePictureURL',  # noqa: E501
        'merchant_id': 'merchantID',  # noqa: E501
        'session_token': 'sessionToken',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, first_name, last_name, email, phone_number, is_public_representative, wallet_sequence_number, employee_id, job_title, department, id, created_at, updated_at, username, email_verified, profile_picture_url, merchant_id, session_token, *args, **kwargs):  # noqa: E501
        """Employee - a model defined in OpenAPI

        Args:
            first_name (str):
            last_name (str):
            email (str):
            phone_number (str):
            is_public_representative (bool):
            wallet_sequence_number (int):
            employee_id (str):
            job_title (str):
            department (str):
            id (NanoID):
            created_at (datetime):
            updated_at (datetime):
            username (str):
            email_verified (str):
            profile_picture_url (str):
            merchant_id (MerchantID):
            session_token (str):

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

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.is_public_representative = is_public_representative
        self.wallet_sequence_number = wallet_sequence_number
        self.employee_id = employee_id
        self.job_title = job_title
        self.department = department
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.username = username
        self.email_verified = email_verified
        self.profile_picture_url = profile_picture_url
        self.merchant_id = merchant_id
        self.session_token = session_token
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
    def __init__(self, first_name, last_name, email, phone_number, is_public_representative, wallet_sequence_number, employee_id, job_title, department, id, created_at, updated_at, username, email_verified, profile_picture_url, merchant_id, session_token, *args, **kwargs):  # noqa: E501
        """Employee - a model defined in OpenAPI

        Args:
            first_name (str):
            last_name (str):
            email (str):
            phone_number (str):
            is_public_representative (bool):
            wallet_sequence_number (int):
            employee_id (str):
            job_title (str):
            department (str):
            id (NanoID):
            created_at (datetime):
            updated_at (datetime):
            username (str):
            email_verified (str):
            profile_picture_url (str):
            merchant_id (MerchantID):
            session_token (str):

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

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.is_public_representative = is_public_representative
        self.wallet_sequence_number = wallet_sequence_number
        self.employee_id = employee_id
        self.job_title = job_title
        self.department = department
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.username = username
        self.email_verified = email_verified
        self.profile_picture_url = profile_picture_url
        self.merchant_id = merchant_id
        self.session_token = session_token
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
