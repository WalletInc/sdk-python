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
    from wallet.model.wt_wallet_page_view_geo_point import WTWalletPageViewGeoPoint
    globals()['MerchantID'] = MerchantID
    globals()['WTWalletPageViewGeoPoint'] = WTWalletPageViewGeoPoint


class WalletPageView(ModelNormal):
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
            'ip': (str,),  # noqa: E501
            'wallet_object_id': (str,),  # noqa: E501
            'wallet_object_prefix': (str,),  # noqa: E501
            'parent_object_id': (str,),  # noqa: E501
            'parent_object_prefix': (str,),  # noqa: E501
            'session_id': (str,),  # noqa: E501
            'navigator_agent': (str,),  # noqa: E501
            'browser_name': (str,),  # noqa: E501
            'browser_version': (str,),  # noqa: E501
            'engine_name': (str,),  # noqa: E501
            'engine_version': (str,),  # noqa: E501
            'o_s_name': (str,),  # noqa: E501
            'o_s_version': (str,),  # noqa: E501
            'is_mobile': (bool,),  # noqa: E501
            'device_vendor': (str,),  # noqa: E501
            'device_model': (str,),  # noqa: E501
            'device_type': (str,),  # noqa: E501
            'phone_verification_token': (str,),  # noqa: E501
            'id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'country_code': (str,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'region_name': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'zip': (str,),  # noqa: E501
            'latitude': (float,),  # noqa: E501
            'longitude': (float,),  # noqa: E501
            'timezone': (str,),  # noqa: E501
            'isp': (str,),  # noqa: E501
            'org': (str,),  # noqa: E501
            'asn': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'merchant_id': (MerchantID,),  # noqa: E501
            'is_active': (bool,),  # noqa: E501
            'geo_point': (WTWalletPageViewGeoPoint,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ip': 'ip',  # noqa: E501
        'wallet_object_id': 'walletObjectID',  # noqa: E501
        'wallet_object_prefix': 'walletObjectPrefix',  # noqa: E501
        'parent_object_id': 'parentObjectID',  # noqa: E501
        'parent_object_prefix': 'parentObjectPrefix',  # noqa: E501
        'session_id': 'sessionID',  # noqa: E501
        'navigator_agent': 'navigatorAgent',  # noqa: E501
        'browser_name': 'browserName',  # noqa: E501
        'browser_version': 'browserVersion',  # noqa: E501
        'engine_name': 'engineName',  # noqa: E501
        'engine_version': 'engineVersion',  # noqa: E501
        'o_s_name': 'oSName',  # noqa: E501
        'o_s_version': 'oSVersion',  # noqa: E501
        'is_mobile': 'isMobile',  # noqa: E501
        'device_vendor': 'deviceVendor',  # noqa: E501
        'device_model': 'deviceModel',  # noqa: E501
        'device_type': 'deviceType',  # noqa: E501
        'phone_verification_token': 'phoneVerificationToken',  # noqa: E501
        'id': 'id',  # noqa: E501
        'status': 'status',  # noqa: E501
        'country': 'country',  # noqa: E501
        'country_code': 'countryCode',  # noqa: E501
        'region': 'region',  # noqa: E501
        'region_name': 'regionName',  # noqa: E501
        'city': 'city',  # noqa: E501
        'zip': 'zip',  # noqa: E501
        'latitude': 'latitude',  # noqa: E501
        'longitude': 'longitude',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'isp': 'isp',  # noqa: E501
        'org': 'org',  # noqa: E501
        'asn': 'asn',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'merchant_id': 'merchantID',  # noqa: E501
        'is_active': 'isActive',  # noqa: E501
        'geo_point': 'geoPoint',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, ip, wallet_object_id, wallet_object_prefix, parent_object_id, parent_object_prefix, session_id, navigator_agent, browser_name, browser_version, engine_name, engine_version, o_s_name, o_s_version, is_mobile, device_vendor, device_model, device_type, phone_verification_token, id, status, country, country_code, region, region_name, city, zip, latitude, longitude, timezone, isp, org, asn, created_at, updated_at, merchant_id, is_active, geo_point, *args, **kwargs):  # noqa: E501
        """WalletPageView - a model defined in OpenAPI

        Args:
            ip (str):
            wallet_object_id (str):
            wallet_object_prefix (str):
            parent_object_id (str):
            parent_object_prefix (str):
            session_id (str):
            navigator_agent (str):
            browser_name (str):
            browser_version (str):
            engine_name (str):
            engine_version (str):
            o_s_name (str):
            o_s_version (str):
            is_mobile (bool):
            device_vendor (str):
            device_model (str):
            device_type (str):
            phone_verification_token (str):
            id (bool, date, datetime, dict, float, int, list, str, none_type):
            status (str):
            country (str):
            country_code (str):
            region (str):
            region_name (str):
            city (str):
            zip (str):
            latitude (float):
            longitude (float):
            timezone (str):
            isp (str):
            org (str):
            asn (str):
            created_at (datetime):
            updated_at (datetime):
            merchant_id (MerchantID):
            is_active (bool): Denotes if this resource is active
            geo_point (WTWalletPageViewGeoPoint):

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

        self.ip = ip
        self.wallet_object_id = wallet_object_id
        self.wallet_object_prefix = wallet_object_prefix
        self.parent_object_id = parent_object_id
        self.parent_object_prefix = parent_object_prefix
        self.session_id = session_id
        self.navigator_agent = navigator_agent
        self.browser_name = browser_name
        self.browser_version = browser_version
        self.engine_name = engine_name
        self.engine_version = engine_version
        self.o_s_name = o_s_name
        self.o_s_version = o_s_version
        self.is_mobile = is_mobile
        self.device_vendor = device_vendor
        self.device_model = device_model
        self.device_type = device_type
        self.phone_verification_token = phone_verification_token
        self.id = id
        self.status = status
        self.country = country
        self.country_code = country_code
        self.region = region
        self.region_name = region_name
        self.city = city
        self.zip = zip
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.isp = isp
        self.org = org
        self.asn = asn
        self.created_at = created_at
        self.updated_at = updated_at
        self.merchant_id = merchant_id
        self.is_active = is_active
        self.geo_point = geo_point
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
    def __init__(self, ip, wallet_object_id, wallet_object_prefix, parent_object_id, parent_object_prefix, session_id, navigator_agent, browser_name, browser_version, engine_name, engine_version, o_s_name, o_s_version, is_mobile, device_vendor, device_model, device_type, phone_verification_token, id, status, country, country_code, region, region_name, city, zip, latitude, longitude, timezone, isp, org, asn, created_at, updated_at, merchant_id, is_active, geo_point, *args, **kwargs):  # noqa: E501
        """WalletPageView - a model defined in OpenAPI

        Args:
            ip (str):
            wallet_object_id (str):
            wallet_object_prefix (str):
            parent_object_id (str):
            parent_object_prefix (str):
            session_id (str):
            navigator_agent (str):
            browser_name (str):
            browser_version (str):
            engine_name (str):
            engine_version (str):
            o_s_name (str):
            o_s_version (str):
            is_mobile (bool):
            device_vendor (str):
            device_model (str):
            device_type (str):
            phone_verification_token (str):
            id (bool, date, datetime, dict, float, int, list, str, none_type):
            status (str):
            country (str):
            country_code (str):
            region (str):
            region_name (str):
            city (str):
            zip (str):
            latitude (float):
            longitude (float):
            timezone (str):
            isp (str):
            org (str):
            asn (str):
            created_at (datetime):
            updated_at (datetime):
            merchant_id (MerchantID):
            is_active (bool): Denotes if this resource is active
            geo_point (WTWalletPageViewGeoPoint):

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

        self.ip = ip
        self.wallet_object_id = wallet_object_id
        self.wallet_object_prefix = wallet_object_prefix
        self.parent_object_id = parent_object_id
        self.parent_object_prefix = parent_object_prefix
        self.session_id = session_id
        self.navigator_agent = navigator_agent
        self.browser_name = browser_name
        self.browser_version = browser_version
        self.engine_name = engine_name
        self.engine_version = engine_version
        self.o_s_name = o_s_name
        self.o_s_version = o_s_version
        self.is_mobile = is_mobile
        self.device_vendor = device_vendor
        self.device_model = device_model
        self.device_type = device_type
        self.phone_verification_token = phone_verification_token
        self.id = id
        self.status = status
        self.country = country
        self.country_code = country_code
        self.region = region
        self.region_name = region_name
        self.city = city
        self.zip = zip
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.isp = isp
        self.org = org
        self.asn = asn
        self.created_at = created_at
        self.updated_at = updated_at
        self.merchant_id = merchant_id
        self.is_active = is_active
        self.geo_point = geo_point
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
