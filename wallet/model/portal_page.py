"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.524
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



class PortalPage(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'ANALYTICS-AD-CREDITS': "analytics-ad-credits",
            'ANALYTICS-CLUB-MEMBERS': "analytics-club-members",
            'DIGITAL-WALLET-CUSTOMER-SESSIONS': "digital-wallet-customer-sessions",
            'ANALYTICS-DYNAMIC-VOUCHERS': "analytics-dynamic-vouchers",
            'ANALYTICS-MEMBERSHIP-TIERS': "analytics-membership-tiers",
            'ANALYTICS-MERCHANT-CREDITS': "analytics-merchant-credits",
            'ANALYTICS-STATIC-VOUCHERS': "analytics-static-vouchers",
            'ANALYTICS-BROADCASTS': "analytics-broadcasts",
            'ANALYTICS-OUTBOUND-SMS': "analytics-outbound-sms",
            'ANALYTICS-HELP-DESK': "analytics-help-desk",
            'ANALYTICS-TCPA': "analytics-tcpa",
            'CALENDAR-TEAM': "calendar-team",
            'COMMUNICATIONS-APPLE-WALLET': "communications-apple-wallet",
            'COMMUNICATIONS-GOOGLE-WALLET': "communications-google-wallet",
            'COMMUNICATIONS-SMS-MEDIA': "communications-sms-media",
            'COMMUNICATIONS-SMS-AGREEMENT': "communications-sms-agreement",
            'COMMUNICATIONS-SMS-CREATE': "communications-sms-create",
            'COMMUNICATIONS-SMS-CUSTOMER-SERVICE': "communications-sms-customer-service",
            'COMMUNICATIONS-SMS-KEYWORDS': "communications-sms-keywords",
            'COMMUNICATIONS-SMS-NUMBERS': "communications-sms-numbers",
            'COMMUNICATIONS-SMS-SOURCES': "communications-sms-sources",
            'COMMUNICATIONS-SMS-SUBSCRIBERS': "communications-sms-subscribers",
            'COMMUNICATIONS-SMS-VOUCHER-CAMPAIGNS': "communications-sms-voucher-campaigns",
            'MEMBERSHIPS-CLUB-MEMBERS': "memberships-club-members",
            'MEMBERSHIPS-TIERS': "memberships-tiers",
            'MERCHANT-PROFILE': "merchant-profile",
            'MERCHANT-URLS': "merchant-urls",
            'POS-CONFIGURATION': "pos-configuration",
            'POS-LEDGER': "pos-ledger",
            'POS-REGISTER-INFOGENESIS': "pos-register-infogenesis",
            'POS-REGISTER-WEB': "pos-register-web",
            'SEARCH': "search",
            'SETTINGS-AUTH-CHANGES': "settings-auth-changes",
            'SETTINGS-MANAGE-ROLES': "settings-manage-roles",
            'SETTINGS-MANAGE-USERS': "settings-manage-users",
            'SETTINGS-PLATFORM-USAGE': "settings-platform-usage",
            'SETTINGS-PROFILE': "settings-profile",
            'SETTINGS-PROFILE-DATA-EXPORTS': "settings-profile-data-exports",
            'SETTINGS-USER-ACTIVITY': "settings-user-activity",
            'ADVERTISEMENT-CREDIT': "advertisement-credit",
            'PAYMENT-CONFIGURATION-DESIGN': "payment-configuration-design",
            'MERCHANT-CREDIT': "merchant-credit",
            'VOUCHERS-DYNAMIC': "vouchers-dynamic",
            'VOUCHERS-STATIC-SINGLE': "vouchers-static-single",
            'VOUCHERS-STATIC-SINGLE-CAMPAIGN': "vouchers-static-single-campaign",
            'DIGITAL-WALLET-CONFIGURATION': "digital-wallet-configuration",
            'PERFORMANCES': "performances",
            'LINK-BOOK': "link-book",
            'IMAGE-GRID': "image-grid",
            'LIVE-CHAT': "live-chat",
            'PROMO-CODES': "promo-codes",
            'NEWS': "news",
        },
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
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """PortalPage - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str):, must be one of ["analytics-ad-credits", "analytics-club-members", "digital-wallet-customer-sessions", "analytics-dynamic-vouchers", "analytics-membership-tiers", "analytics-merchant-credits", "analytics-static-vouchers", "analytics-broadcasts", "analytics-outbound-sms", "analytics-help-desk", "analytics-tcpa", "calendar-team", "communications-apple-wallet", "communications-google-wallet", "communications-sms-media", "communications-sms-agreement", "communications-sms-create", "communications-sms-customer-service", "communications-sms-keywords", "communications-sms-numbers", "communications-sms-sources", "communications-sms-subscribers", "communications-sms-voucher-campaigns", "memberships-club-members", "memberships-tiers", "merchant-profile", "merchant-urls", "pos-configuration", "pos-ledger", "pos-register-infogenesis", "pos-register-web", "search", "settings-auth-changes", "settings-manage-roles", "settings-manage-users", "settings-platform-usage", "settings-profile", "settings-profile-data-exports", "settings-user-activity", "advertisement-credit", "payment-configuration-design", "merchant-credit", "vouchers-dynamic", "vouchers-static-single", "vouchers-static-single-campaign", "digital-wallet-configuration", "performances", "link-book", "image-grid", "live-chat", "promo-codes", "news", ]  # noqa: E501

        Keyword Args:
            value (str):, must be one of ["analytics-ad-credits", "analytics-club-members", "digital-wallet-customer-sessions", "analytics-dynamic-vouchers", "analytics-membership-tiers", "analytics-merchant-credits", "analytics-static-vouchers", "analytics-broadcasts", "analytics-outbound-sms", "analytics-help-desk", "analytics-tcpa", "calendar-team", "communications-apple-wallet", "communications-google-wallet", "communications-sms-media", "communications-sms-agreement", "communications-sms-create", "communications-sms-customer-service", "communications-sms-keywords", "communications-sms-numbers", "communications-sms-sources", "communications-sms-subscribers", "communications-sms-voucher-campaigns", "memberships-club-members", "memberships-tiers", "merchant-profile", "merchant-urls", "pos-configuration", "pos-ledger", "pos-register-infogenesis", "pos-register-web", "search", "settings-auth-changes", "settings-manage-roles", "settings-manage-users", "settings-platform-usage", "settings-profile", "settings-profile-data-exports", "settings-user-activity", "advertisement-credit", "payment-configuration-design", "merchant-credit", "vouchers-dynamic", "vouchers-static-single", "vouchers-static-single-campaign", "digital-wallet-configuration", "performances", "link-book", "image-grid", "live-chat", "promo-codes", "news", ]  # noqa: E501
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
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """PortalPage - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str):, must be one of ["analytics-ad-credits", "analytics-club-members", "digital-wallet-customer-sessions", "analytics-dynamic-vouchers", "analytics-membership-tiers", "analytics-merchant-credits", "analytics-static-vouchers", "analytics-broadcasts", "analytics-outbound-sms", "analytics-help-desk", "analytics-tcpa", "calendar-team", "communications-apple-wallet", "communications-google-wallet", "communications-sms-media", "communications-sms-agreement", "communications-sms-create", "communications-sms-customer-service", "communications-sms-keywords", "communications-sms-numbers", "communications-sms-sources", "communications-sms-subscribers", "communications-sms-voucher-campaigns", "memberships-club-members", "memberships-tiers", "merchant-profile", "merchant-urls", "pos-configuration", "pos-ledger", "pos-register-infogenesis", "pos-register-web", "search", "settings-auth-changes", "settings-manage-roles", "settings-manage-users", "settings-platform-usage", "settings-profile", "settings-profile-data-exports", "settings-user-activity", "advertisement-credit", "payment-configuration-design", "merchant-credit", "vouchers-dynamic", "vouchers-static-single", "vouchers-static-single-campaign", "digital-wallet-configuration", "performances", "link-book", "image-grid", "live-chat", "promo-codes", "news", ]  # noqa: E501

        Keyword Args:
            value (str):, must be one of ["analytics-ad-credits", "analytics-club-members", "digital-wallet-customer-sessions", "analytics-dynamic-vouchers", "analytics-membership-tiers", "analytics-merchant-credits", "analytics-static-vouchers", "analytics-broadcasts", "analytics-outbound-sms", "analytics-help-desk", "analytics-tcpa", "calendar-team", "communications-apple-wallet", "communications-google-wallet", "communications-sms-media", "communications-sms-agreement", "communications-sms-create", "communications-sms-customer-service", "communications-sms-keywords", "communications-sms-numbers", "communications-sms-sources", "communications-sms-subscribers", "communications-sms-voucher-campaigns", "memberships-club-members", "memberships-tiers", "merchant-profile", "merchant-urls", "pos-configuration", "pos-ledger", "pos-register-infogenesis", "pos-register-web", "search", "settings-auth-changes", "settings-manage-roles", "settings-manage-users", "settings-platform-usage", "settings-profile", "settings-profile-data-exports", "settings-user-activity", "advertisement-credit", "payment-configuration-design", "merchant-credit", "vouchers-dynamic", "vouchers-static-single", "vouchers-static-single-campaign", "digital-wallet-configuration", "performances", "link-book", "image-grid", "live-chat", "promo-codes", "news", ]  # noqa: E501
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
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
