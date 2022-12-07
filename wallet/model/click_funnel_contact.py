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
    from wallet.model.click_funnel_contact_profile import ClickFunnelContactProfile
    globals()['ClickFunnelContactProfile'] = ClickFunnelContactProfile


class ClickFunnelContact(ModelNormal):
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
            'page_id': (float,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'address': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'zip': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'phone': (str,),  # noqa: E501
            'webinar_ext': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'ip': (str,),  # noqa: E501
            'funnel_id': (float,),  # noqa: E501
            'funnel_step_id': (float,),  # noqa: E501
            'cf_uvid': (str,),  # noqa: E501
            'cart_affiliate_id': (str,),  # noqa: E501
            'shipping_address': (str,),  # noqa: E501
            'shipping_city': (str,),  # noqa: E501
            'shipping_country': (str,),  # noqa: E501
            'shipping_state': (str,),  # noqa: E501
            'shipping_zip': (str,),  # noqa: E501
            'vat_number': (str,),  # noqa: E501
            'aff_sub': (str,),  # noqa: E501
            'aff_sub2': (str,),  # noqa: E501
            'company_name': (str,),  # noqa: E501
            'company_industry': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'webinar_at': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'webinar_last_time': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'unsubscribed_at': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'affiliate_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'cf_affiliate_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'contact_profile': (ClickFunnelContactProfile,),  # noqa: E501
            'time_zone': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'page_id': 'page_id',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'name': 'name',  # noqa: E501
        'address': 'address',  # noqa: E501
        'city': 'city',  # noqa: E501
        'country': 'country',  # noqa: E501
        'zip': 'zip',  # noqa: E501
        'email': 'email',  # noqa: E501
        'phone': 'phone',  # noqa: E501
        'webinar_ext': 'webinar_ext',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'ip': 'ip',  # noqa: E501
        'funnel_id': 'funnel_id',  # noqa: E501
        'funnel_step_id': 'funnel_step_id',  # noqa: E501
        'cf_uvid': 'cf_uvid',  # noqa: E501
        'cart_affiliate_id': 'cart_affiliate_id',  # noqa: E501
        'shipping_address': 'shipping_address',  # noqa: E501
        'shipping_city': 'shipping_city',  # noqa: E501
        'shipping_country': 'shipping_country',  # noqa: E501
        'shipping_state': 'shipping_state',  # noqa: E501
        'shipping_zip': 'shipping_zip',  # noqa: E501
        'vat_number': 'vat_number',  # noqa: E501
        'aff_sub': 'aff_sub',  # noqa: E501
        'aff_sub2': 'aff_sub2',  # noqa: E501
        'company_name': 'company_name',  # noqa: E501
        'company_industry': 'company_industry',  # noqa: E501
        'state': 'state',  # noqa: E501
        'webinar_at': 'webinar_at',  # noqa: E501
        'webinar_last_time': 'webinar_last_time',  # noqa: E501
        'unsubscribed_at': 'unsubscribed_at',  # noqa: E501
        'affiliate_id': 'affiliate_id',  # noqa: E501
        'cf_affiliate_id': 'cf_affiliate_id',  # noqa: E501
        'contact_profile': 'contact_profile',  # noqa: E501
        'time_zone': 'time_zone',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, page_id, first_name, last_name, name, address, city, country, zip, email, phone, webinar_ext, created_at, updated_at, ip, funnel_id, funnel_step_id, cf_uvid, cart_affiliate_id, shipping_address, shipping_city, shipping_country, shipping_state, shipping_zip, vat_number, aff_sub, aff_sub2, company_name, company_industry, *args, **kwargs):  # noqa: E501
        """ClickFunnelContact - a model defined in OpenAPI

        Args:
            id (float):
            page_id (float):
            first_name (str):
            last_name (str):
            name (str):
            address (str):
            city (str):
            country (str):
            zip (str):
            email (str):
            phone (str):
            webinar_ext (str):
            created_at (datetime):
            updated_at (datetime):
            ip (str):
            funnel_id (float):
            funnel_step_id (float):
            cf_uvid (str):
            cart_affiliate_id (str):
            shipping_address (str):
            shipping_city (str):
            shipping_country (str):
            shipping_state (str):
            shipping_zip (str):
            vat_number (str):
            aff_sub (str):
            aff_sub2 (str):
            company_name (str):
            company_industry (str):

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
            state (str): [optional]  # noqa: E501
            webinar_at (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            webinar_last_time (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            unsubscribed_at (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            affiliate_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            cf_affiliate_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            contact_profile (ClickFunnelContactProfile): [optional]  # noqa: E501
            time_zone (str, none_type): [optional]  # noqa: E501
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
        self.page_id = page_id
        self.first_name = first_name
        self.last_name = last_name
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.zip = zip
        self.email = email
        self.phone = phone
        self.webinar_ext = webinar_ext
        self.created_at = created_at
        self.updated_at = updated_at
        self.ip = ip
        self.funnel_id = funnel_id
        self.funnel_step_id = funnel_step_id
        self.cf_uvid = cf_uvid
        self.cart_affiliate_id = cart_affiliate_id
        self.shipping_address = shipping_address
        self.shipping_city = shipping_city
        self.shipping_country = shipping_country
        self.shipping_state = shipping_state
        self.shipping_zip = shipping_zip
        self.vat_number = vat_number
        self.aff_sub = aff_sub
        self.aff_sub2 = aff_sub2
        self.company_name = company_name
        self.company_industry = company_industry
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
    def __init__(self, id, page_id, first_name, last_name, name, address, city, country, zip, email, phone, webinar_ext, created_at, updated_at, ip, funnel_id, funnel_step_id, cf_uvid, cart_affiliate_id, shipping_address, shipping_city, shipping_country, shipping_state, shipping_zip, vat_number, aff_sub, aff_sub2, company_name, company_industry, *args, **kwargs):  # noqa: E501
        """ClickFunnelContact - a model defined in OpenAPI

        Args:
            id (float):
            page_id (float):
            first_name (str):
            last_name (str):
            name (str):
            address (str):
            city (str):
            country (str):
            zip (str):
            email (str):
            phone (str):
            webinar_ext (str):
            created_at (datetime):
            updated_at (datetime):
            ip (str):
            funnel_id (float):
            funnel_step_id (float):
            cf_uvid (str):
            cart_affiliate_id (str):
            shipping_address (str):
            shipping_city (str):
            shipping_country (str):
            shipping_state (str):
            shipping_zip (str):
            vat_number (str):
            aff_sub (str):
            aff_sub2 (str):
            company_name (str):
            company_industry (str):

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
            state (str): [optional]  # noqa: E501
            webinar_at (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            webinar_last_time (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            unsubscribed_at (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            affiliate_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            cf_affiliate_id (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            contact_profile (ClickFunnelContactProfile): [optional]  # noqa: E501
            time_zone (str, none_type): [optional]  # noqa: E501
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
        self.page_id = page_id
        self.first_name = first_name
        self.last_name = last_name
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.zip = zip
        self.email = email
        self.phone = phone
        self.webinar_ext = webinar_ext
        self.created_at = created_at
        self.updated_at = updated_at
        self.ip = ip
        self.funnel_id = funnel_id
        self.funnel_step_id = funnel_step_id
        self.cf_uvid = cf_uvid
        self.cart_affiliate_id = cart_affiliate_id
        self.shipping_address = shipping_address
        self.shipping_city = shipping_city
        self.shipping_country = shipping_country
        self.shipping_state = shipping_state
        self.shipping_zip = shipping_zip
        self.vat_number = vat_number
        self.aff_sub = aff_sub
        self.aff_sub2 = aff_sub2
        self.company_name = company_name
        self.company_industry = company_industry
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
