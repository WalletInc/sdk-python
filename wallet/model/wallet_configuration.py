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


def lazy_import():
    from wallet.model.merchant_id import MerchantID
    from wallet.model.nano_id import NanoID
    globals()['MerchantID'] = MerchantID
    globals()['NanoID'] = NanoID


class WalletConfiguration(ModelNormal):
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
            'header_background_color': (str,),  # noqa: E501
            'header_button_color': (str,),  # noqa: E501
            'left_menu_section_color': (str,),  # noqa: E501
            'left_menu_arrow_color': (str,),  # noqa: E501
            'company_logo_url': (str,),  # noqa: E501
            'welcome_message': (str,),  # noqa: E501
            'is_apple_enabled': (bool,),  # noqa: E501
            'is_google_enabled': (bool,),  # noqa: E501
            'is_samsung_enabled': (bool,),  # noqa: E501
            'is_ad_credits': (bool,),  # noqa: E501
            'is_static_vouchers': (bool,),  # noqa: E501
            'is_dynamic_vouchers': (bool,),  # noqa: E501
            'is_membership_tier': (bool,),  # noqa: E501
            'is_membership_points': (bool,),  # noqa: E501
            'is_membership_level': (bool,),  # noqa: E501
            'is_gift_cards': (bool,),  # noqa: E501
            'is_gift_certificates': (bool,),  # noqa: E501
            'is_promotions': (bool,),  # noqa: E501
            'is_merchant_credit': (bool,),  # noqa: E501
            'is_news_articles': (bool,),  # noqa: E501
            'is_performances': (bool,),  # noqa: E501
            'is_messages': (bool,),  # noqa: E501
            'is_call': (bool,),  # noqa: E501
            'is_representatives': (bool,),  # noqa: E501
            'is_map_directions': (bool,),  # noqa: E501
            'is_link_book': (bool,),  # noqa: E501
            'is_image_grid': (bool,),  # noqa: E501
            'is_transaction_history': (bool,),  # noqa: E501
            'is_profile': (bool,),  # noqa: E501
            'is_settings': (bool,),  # noqa: E501
            'is_chat_room': (bool,),  # noqa: E501
            'id': (NanoID,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'merchant_id': (MerchantID,),  # noqa: E501
            'header_image_url': (str,),  # noqa: E501
            'header_custom_icon': (str,),  # noqa: E501
            'is_tickets': (bool,),  # noqa: E501
            'google_analytics_id': (str,),  # noqa: E501
            'facebook_pixel_id': (str,),  # noqa: E501
            'public_chat_room_channel_id': (float,),  # noqa: E501
            'vanity_handle': (str,),  # noqa: E501
            'vanity_page_wallet_prefix': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'header_background_color': 'headerBackgroundColor',  # noqa: E501
        'header_button_color': 'headerButtonColor',  # noqa: E501
        'left_menu_section_color': 'leftMenuSectionColor',  # noqa: E501
        'left_menu_arrow_color': 'leftMenuArrowColor',  # noqa: E501
        'company_logo_url': 'companyLogoURL',  # noqa: E501
        'welcome_message': 'welcomeMessage',  # noqa: E501
        'is_apple_enabled': 'isAppleEnabled',  # noqa: E501
        'is_google_enabled': 'isGoogleEnabled',  # noqa: E501
        'is_samsung_enabled': 'isSamsungEnabled',  # noqa: E501
        'is_ad_credits': 'isAdCredits',  # noqa: E501
        'is_static_vouchers': 'isStaticVouchers',  # noqa: E501
        'is_dynamic_vouchers': 'isDynamicVouchers',  # noqa: E501
        'is_membership_tier': 'isMembershipTier',  # noqa: E501
        'is_membership_points': 'isMembershipPoints',  # noqa: E501
        'is_membership_level': 'isMembershipLevel',  # noqa: E501
        'is_gift_cards': 'isGiftCards',  # noqa: E501
        'is_gift_certificates': 'isGiftCertificates',  # noqa: E501
        'is_promotions': 'isPromotions',  # noqa: E501
        'is_merchant_credit': 'isMerchantCredit',  # noqa: E501
        'is_news_articles': 'isNewsArticles',  # noqa: E501
        'is_performances': 'isPerformances',  # noqa: E501
        'is_messages': 'isMessages',  # noqa: E501
        'is_call': 'isCall',  # noqa: E501
        'is_representatives': 'isRepresentatives',  # noqa: E501
        'is_map_directions': 'isMapDirections',  # noqa: E501
        'is_link_book': 'isLinkBook',  # noqa: E501
        'is_image_grid': 'isImageGrid',  # noqa: E501
        'is_transaction_history': 'isTransactionHistory',  # noqa: E501
        'is_profile': 'isProfile',  # noqa: E501
        'is_settings': 'isSettings',  # noqa: E501
        'is_chat_room': 'isChatRoom',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'merchant_id': 'merchantID',  # noqa: E501
        'header_image_url': 'headerImageURL',  # noqa: E501
        'header_custom_icon': 'headerCustomIcon',  # noqa: E501
        'is_tickets': 'isTickets',  # noqa: E501
        'google_analytics_id': 'googleAnalyticsID',  # noqa: E501
        'facebook_pixel_id': 'facebookPixelID',  # noqa: E501
        'public_chat_room_channel_id': 'publicChatRoomChannelID',  # noqa: E501
        'vanity_handle': 'vanityHandle',  # noqa: E501
        'vanity_page_wallet_prefix': 'vanityPageWalletPrefix',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, header_background_color, header_button_color, left_menu_section_color, left_menu_arrow_color, company_logo_url, welcome_message, is_apple_enabled, is_google_enabled, is_samsung_enabled, is_ad_credits, is_static_vouchers, is_dynamic_vouchers, is_membership_tier, is_membership_points, is_membership_level, is_gift_cards, is_gift_certificates, is_promotions, is_merchant_credit, is_news_articles, is_performances, is_messages, is_call, is_representatives, is_map_directions, is_link_book, is_image_grid, is_transaction_history, is_profile, is_settings, is_chat_room, id, created_at, updated_at, merchant_id, *args, **kwargs):  # noqa: E501
        """WalletConfiguration - a model defined in OpenAPI

        Args:
            header_background_color (str):
            header_button_color (str):
            left_menu_section_color (str):
            left_menu_arrow_color (str):
            company_logo_url (str):
            welcome_message (str):
            is_apple_enabled (bool):
            is_google_enabled (bool):
            is_samsung_enabled (bool):
            is_ad_credits (bool):
            is_static_vouchers (bool):
            is_dynamic_vouchers (bool):
            is_membership_tier (bool):
            is_membership_points (bool):
            is_membership_level (bool):
            is_gift_cards (bool):
            is_gift_certificates (bool):
            is_promotions (bool):
            is_merchant_credit (bool):
            is_news_articles (bool):
            is_performances (bool):
            is_messages (bool):
            is_call (bool):
            is_representatives (bool):
            is_map_directions (bool):
            is_link_book (bool):
            is_image_grid (bool):
            is_transaction_history (bool):
            is_profile (bool):
            is_settings (bool):
            is_chat_room (bool):
            id (NanoID):
            created_at (datetime):
            updated_at (datetime):
            merchant_id (MerchantID):

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
            header_image_url (str): [optional]  # noqa: E501
            header_custom_icon (str): [optional]  # noqa: E501
            is_tickets (bool): [optional]  # noqa: E501
            google_analytics_id (str): [optional]  # noqa: E501
            facebook_pixel_id (str): [optional]  # noqa: E501
            public_chat_room_channel_id (float): [optional]  # noqa: E501
            vanity_handle (str): [optional]  # noqa: E501
            vanity_page_wallet_prefix (str): [optional]  # noqa: E501
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

        self.header_background_color = header_background_color
        self.header_button_color = header_button_color
        self.left_menu_section_color = left_menu_section_color
        self.left_menu_arrow_color = left_menu_arrow_color
        self.company_logo_url = company_logo_url
        self.welcome_message = welcome_message
        self.is_apple_enabled = is_apple_enabled
        self.is_google_enabled = is_google_enabled
        self.is_samsung_enabled = is_samsung_enabled
        self.is_ad_credits = is_ad_credits
        self.is_static_vouchers = is_static_vouchers
        self.is_dynamic_vouchers = is_dynamic_vouchers
        self.is_membership_tier = is_membership_tier
        self.is_membership_points = is_membership_points
        self.is_membership_level = is_membership_level
        self.is_gift_cards = is_gift_cards
        self.is_gift_certificates = is_gift_certificates
        self.is_promotions = is_promotions
        self.is_merchant_credit = is_merchant_credit
        self.is_news_articles = is_news_articles
        self.is_performances = is_performances
        self.is_messages = is_messages
        self.is_call = is_call
        self.is_representatives = is_representatives
        self.is_map_directions = is_map_directions
        self.is_link_book = is_link_book
        self.is_image_grid = is_image_grid
        self.is_transaction_history = is_transaction_history
        self.is_profile = is_profile
        self.is_settings = is_settings
        self.is_chat_room = is_chat_room
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.merchant_id = merchant_id
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
    def __init__(self, header_background_color, header_button_color, left_menu_section_color, left_menu_arrow_color, company_logo_url, welcome_message, is_apple_enabled, is_google_enabled, is_samsung_enabled, is_ad_credits, is_static_vouchers, is_dynamic_vouchers, is_membership_tier, is_membership_points, is_membership_level, is_gift_cards, is_gift_certificates, is_promotions, is_merchant_credit, is_news_articles, is_performances, is_messages, is_call, is_representatives, is_map_directions, is_link_book, is_image_grid, is_transaction_history, is_profile, is_settings, is_chat_room, id, created_at, updated_at, merchant_id, *args, **kwargs):  # noqa: E501
        """WalletConfiguration - a model defined in OpenAPI

        Args:
            header_background_color (str):
            header_button_color (str):
            left_menu_section_color (str):
            left_menu_arrow_color (str):
            company_logo_url (str):
            welcome_message (str):
            is_apple_enabled (bool):
            is_google_enabled (bool):
            is_samsung_enabled (bool):
            is_ad_credits (bool):
            is_static_vouchers (bool):
            is_dynamic_vouchers (bool):
            is_membership_tier (bool):
            is_membership_points (bool):
            is_membership_level (bool):
            is_gift_cards (bool):
            is_gift_certificates (bool):
            is_promotions (bool):
            is_merchant_credit (bool):
            is_news_articles (bool):
            is_performances (bool):
            is_messages (bool):
            is_call (bool):
            is_representatives (bool):
            is_map_directions (bool):
            is_link_book (bool):
            is_image_grid (bool):
            is_transaction_history (bool):
            is_profile (bool):
            is_settings (bool):
            is_chat_room (bool):
            id (NanoID):
            created_at (datetime):
            updated_at (datetime):
            merchant_id (MerchantID):

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
            header_image_url (str): [optional]  # noqa: E501
            header_custom_icon (str): [optional]  # noqa: E501
            is_tickets (bool): [optional]  # noqa: E501
            google_analytics_id (str): [optional]  # noqa: E501
            facebook_pixel_id (str): [optional]  # noqa: E501
            public_chat_room_channel_id (float): [optional]  # noqa: E501
            vanity_handle (str): [optional]  # noqa: E501
            vanity_page_wallet_prefix (str): [optional]  # noqa: E501
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

        self.header_background_color = header_background_color
        self.header_button_color = header_button_color
        self.left_menu_section_color = left_menu_section_color
        self.left_menu_arrow_color = left_menu_arrow_color
        self.company_logo_url = company_logo_url
        self.welcome_message = welcome_message
        self.is_apple_enabled = is_apple_enabled
        self.is_google_enabled = is_google_enabled
        self.is_samsung_enabled = is_samsung_enabled
        self.is_ad_credits = is_ad_credits
        self.is_static_vouchers = is_static_vouchers
        self.is_dynamic_vouchers = is_dynamic_vouchers
        self.is_membership_tier = is_membership_tier
        self.is_membership_points = is_membership_points
        self.is_membership_level = is_membership_level
        self.is_gift_cards = is_gift_cards
        self.is_gift_certificates = is_gift_certificates
        self.is_promotions = is_promotions
        self.is_merchant_credit = is_merchant_credit
        self.is_news_articles = is_news_articles
        self.is_performances = is_performances
        self.is_messages = is_messages
        self.is_call = is_call
        self.is_representatives = is_representatives
        self.is_map_directions = is_map_directions
        self.is_link_book = is_link_book
        self.is_image_grid = is_image_grid
        self.is_transaction_history = is_transaction_history
        self.is_profile = is_profile
        self.is_settings = is_settings
        self.is_chat_room = is_chat_room
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.merchant_id = merchant_id
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
