"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.519
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


class Request(ModelNormal):
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
            'id': (NanoID,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'auth_amount': (float,),  # noqa: E501
            'server_emp_id': (str,),  # noqa: E501
            'module_invoked': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'cashier_emp_id': (str,),  # noqa: E501
            'routing_id': (str,),  # noqa: E501
            'auth_account_num': (float,),  # noqa: E501
            'more_records_count': (float,),  # noqa: E501
            'payment_method_id': (str,),  # noqa: E501
            'tag_data': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'total_auth_amount': (float,),  # noqa: E501
            'refund_flag': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'close_time': (datetime,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'change_amount': (float,),  # noqa: E501
            'employee_id': (NanoID,),  # noqa: E501
            'training_mode_flag': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'source_property_id': (str,),  # noqa: E501
            'associated_check_number': (str,),  # noqa: E501
            'post_to_property_id': (str,),  # noqa: E501
            'unique_posting_id': (str,),  # noqa: E501
            'expire_date': (datetime,),  # noqa: E501
            'by_name_flag': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'payment_slip_id': (str,),  # noqa: E501
            'financial_bin_detail': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'cvv2': (str,),  # noqa: E501
            'employee_grat_tip': (float,),  # noqa: E501
            'card_swipe_track1': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'card_swipe_track2': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'check_number': (str,),  # noqa: E501
            'more_records_key': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'tip_amount': (float,),  # noqa: E501
            'input_data': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'profit_center_id': (str,),  # noqa: E501
            'invoice_number': (str,),  # noqa: E501
            'receipt_text_image': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'brokerage_amount': (float,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'cover_count': (float,),  # noqa: E501
            'more_records_flag': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'account_num': (str,),  # noqa: E501
            'max_record_count': (float,),  # noqa: E501
            'incremental_auth_amount': (float,),  # noqa: E501
            'extra_data': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'check_type_id': (str,),  # noqa: E501
            'posting_id': (str,),  # noqa: E501
            'destination_property_id': (str,),  # noqa: E501
            'account_detail': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'payment_amount': (float,),  # noqa: E501
            'register_id': (str,),  # noqa: E501
            'tndr_account_object': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'meal_period_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'auth_amount': 'authAmount',  # noqa: E501
        'server_emp_id': 'serverEmpID',  # noqa: E501
        'module_invoked': 'moduleInvoked',  # noqa: E501
        'cashier_emp_id': 'cashierEmpID',  # noqa: E501
        'routing_id': 'routingID',  # noqa: E501
        'auth_account_num': 'authAccountNum',  # noqa: E501
        'more_records_count': 'moreRecordsCount',  # noqa: E501
        'payment_method_id': 'paymentMethodID',  # noqa: E501
        'tag_data': 'tagData',  # noqa: E501
        'total_auth_amount': 'totalAuthAmount',  # noqa: E501
        'refund_flag': 'refundFlag',  # noqa: E501
        'close_time': 'closeTime',  # noqa: E501
        'client_id': 'clientID',  # noqa: E501
        'change_amount': 'changeAmount',  # noqa: E501
        'employee_id': 'employeeID',  # noqa: E501
        'training_mode_flag': 'trainingModeFlag',  # noqa: E501
        'source_property_id': 'sourcePropertyID',  # noqa: E501
        'associated_check_number': 'associatedCheckNumber',  # noqa: E501
        'post_to_property_id': 'postToPropertyID',  # noqa: E501
        'unique_posting_id': 'uniquePostingID',  # noqa: E501
        'expire_date': 'expireDate',  # noqa: E501
        'by_name_flag': 'byNameFlag',  # noqa: E501
        'payment_slip_id': 'paymentSlipID',  # noqa: E501
        'financial_bin_detail': 'financialBinDetail',  # noqa: E501
        'cvv2': 'cvv2',  # noqa: E501
        'employee_grat_tip': 'employeeGratTip',  # noqa: E501
        'card_swipe_track1': 'cardSwipeTrack1',  # noqa: E501
        'card_swipe_track2': 'cardSwipeTrack2',  # noqa: E501
        'check_number': 'checkNumber',  # noqa: E501
        'more_records_key': 'moreRecordsKey',  # noqa: E501
        'tip_amount': 'tipAmount',  # noqa: E501
        'input_data': 'inputData',  # noqa: E501
        'profit_center_id': 'profitCenterID',  # noqa: E501
        'invoice_number': 'invoiceNumber',  # noqa: E501
        'receipt_text_image': 'receiptTextImage',  # noqa: E501
        'brokerage_amount': 'brokerageAmount',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'cover_count': 'coverCount',  # noqa: E501
        'more_records_flag': 'moreRecordsFlag',  # noqa: E501
        'account_num': 'accountNum',  # noqa: E501
        'max_record_count': 'maxRecordCount',  # noqa: E501
        'incremental_auth_amount': 'incrementalAuthAmount',  # noqa: E501
        'extra_data': 'extraData',  # noqa: E501
        'check_type_id': 'checkTypeID',  # noqa: E501
        'posting_id': 'postingID',  # noqa: E501
        'destination_property_id': 'destinationPropertyID',  # noqa: E501
        'account_detail': 'accountDetail',  # noqa: E501
        'payment_amount': 'paymentAmount',  # noqa: E501
        'register_id': 'registerID',  # noqa: E501
        'tndr_account_object': 'tndrAccountObject',  # noqa: E501
        'meal_period_id': 'mealPeriodID',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, created_at, updated_at, auth_amount, server_emp_id, module_invoked, cashier_emp_id, routing_id, auth_account_num, more_records_count, payment_method_id, tag_data, total_auth_amount, refund_flag, close_time, client_id, change_amount, employee_id, training_mode_flag, source_property_id, associated_check_number, post_to_property_id, unique_posting_id, expire_date, by_name_flag, payment_slip_id, financial_bin_detail, cvv2, employee_grat_tip, card_swipe_track1, card_swipe_track2, check_number, more_records_key, tip_amount, input_data, profit_center_id, invoice_number, receipt_text_image, brokerage_amount, amount, cover_count, more_records_flag, account_num, max_record_count, incremental_auth_amount, extra_data, check_type_id, posting_id, destination_property_id, account_detail, payment_amount, register_id, tndr_account_object, meal_period_id, *args, **kwargs):  # noqa: E501
        """Request - a model defined in OpenAPI

        Args:
            id (NanoID):
            created_at (datetime):
            updated_at (datetime):
            auth_amount (float):
            server_emp_id (str):
            module_invoked (bool, date, datetime, dict, float, int, list, str, none_type):
            cashier_emp_id (str):
            routing_id (str):
            auth_account_num (float):
            more_records_count (float):
            payment_method_id (str):
            tag_data (bool, date, datetime, dict, float, int, list, str, none_type):
            total_auth_amount (float):
            refund_flag (bool, date, datetime, dict, float, int, list, str, none_type):
            close_time (datetime):
            client_id (str):
            change_amount (float):
            employee_id (NanoID):
            training_mode_flag (bool, date, datetime, dict, float, int, list, str, none_type):
            source_property_id (str):
            associated_check_number (str):
            post_to_property_id (str):
            unique_posting_id (str):
            expire_date (datetime):
            by_name_flag (bool, date, datetime, dict, float, int, list, str, none_type):
            payment_slip_id (str):
            financial_bin_detail (bool, date, datetime, dict, float, int, list, str, none_type):
            cvv2 (str):
            employee_grat_tip (float):
            card_swipe_track1 (bool, date, datetime, dict, float, int, list, str, none_type):
            card_swipe_track2 (bool, date, datetime, dict, float, int, list, str, none_type):
            check_number (str):
            more_records_key (bool, date, datetime, dict, float, int, list, str, none_type):
            tip_amount (float):
            input_data (bool, date, datetime, dict, float, int, list, str, none_type):
            profit_center_id (str):
            invoice_number (str):
            receipt_text_image (bool, date, datetime, dict, float, int, list, str, none_type):
            brokerage_amount (float):
            amount (float):
            cover_count (float):
            more_records_flag (bool, date, datetime, dict, float, int, list, str, none_type):
            account_num (str):
            max_record_count (float):
            incremental_auth_amount (float):
            extra_data (bool, date, datetime, dict, float, int, list, str, none_type):
            check_type_id (str):
            posting_id (str):
            destination_property_id (str):
            account_detail (bool, date, datetime, dict, float, int, list, str, none_type):
            payment_amount (float):
            register_id (str):
            tndr_account_object (bool, date, datetime, dict, float, int, list, str, none_type):
            meal_period_id (str):

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

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.auth_amount = auth_amount
        self.server_emp_id = server_emp_id
        self.module_invoked = module_invoked
        self.cashier_emp_id = cashier_emp_id
        self.routing_id = routing_id
        self.auth_account_num = auth_account_num
        self.more_records_count = more_records_count
        self.payment_method_id = payment_method_id
        self.tag_data = tag_data
        self.total_auth_amount = total_auth_amount
        self.refund_flag = refund_flag
        self.close_time = close_time
        self.client_id = client_id
        self.change_amount = change_amount
        self.employee_id = employee_id
        self.training_mode_flag = training_mode_flag
        self.source_property_id = source_property_id
        self.associated_check_number = associated_check_number
        self.post_to_property_id = post_to_property_id
        self.unique_posting_id = unique_posting_id
        self.expire_date = expire_date
        self.by_name_flag = by_name_flag
        self.payment_slip_id = payment_slip_id
        self.financial_bin_detail = financial_bin_detail
        self.cvv2 = cvv2
        self.employee_grat_tip = employee_grat_tip
        self.card_swipe_track1 = card_swipe_track1
        self.card_swipe_track2 = card_swipe_track2
        self.check_number = check_number
        self.more_records_key = more_records_key
        self.tip_amount = tip_amount
        self.input_data = input_data
        self.profit_center_id = profit_center_id
        self.invoice_number = invoice_number
        self.receipt_text_image = receipt_text_image
        self.brokerage_amount = brokerage_amount
        self.amount = amount
        self.cover_count = cover_count
        self.more_records_flag = more_records_flag
        self.account_num = account_num
        self.max_record_count = max_record_count
        self.incremental_auth_amount = incremental_auth_amount
        self.extra_data = extra_data
        self.check_type_id = check_type_id
        self.posting_id = posting_id
        self.destination_property_id = destination_property_id
        self.account_detail = account_detail
        self.payment_amount = payment_amount
        self.register_id = register_id
        self.tndr_account_object = tndr_account_object
        self.meal_period_id = meal_period_id
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
    def __init__(self, id, created_at, updated_at, auth_amount, server_emp_id, module_invoked, cashier_emp_id, routing_id, auth_account_num, more_records_count, payment_method_id, tag_data, total_auth_amount, refund_flag, close_time, client_id, change_amount, employee_id, training_mode_flag, source_property_id, associated_check_number, post_to_property_id, unique_posting_id, expire_date, by_name_flag, payment_slip_id, financial_bin_detail, cvv2, employee_grat_tip, card_swipe_track1, card_swipe_track2, check_number, more_records_key, tip_amount, input_data, profit_center_id, invoice_number, receipt_text_image, brokerage_amount, amount, cover_count, more_records_flag, account_num, max_record_count, incremental_auth_amount, extra_data, check_type_id, posting_id, destination_property_id, account_detail, payment_amount, register_id, tndr_account_object, meal_period_id, *args, **kwargs):  # noqa: E501
        """Request - a model defined in OpenAPI

        Args:
            id (NanoID):
            created_at (datetime):
            updated_at (datetime):
            auth_amount (float):
            server_emp_id (str):
            module_invoked (bool, date, datetime, dict, float, int, list, str, none_type):
            cashier_emp_id (str):
            routing_id (str):
            auth_account_num (float):
            more_records_count (float):
            payment_method_id (str):
            tag_data (bool, date, datetime, dict, float, int, list, str, none_type):
            total_auth_amount (float):
            refund_flag (bool, date, datetime, dict, float, int, list, str, none_type):
            close_time (datetime):
            client_id (str):
            change_amount (float):
            employee_id (NanoID):
            training_mode_flag (bool, date, datetime, dict, float, int, list, str, none_type):
            source_property_id (str):
            associated_check_number (str):
            post_to_property_id (str):
            unique_posting_id (str):
            expire_date (datetime):
            by_name_flag (bool, date, datetime, dict, float, int, list, str, none_type):
            payment_slip_id (str):
            financial_bin_detail (bool, date, datetime, dict, float, int, list, str, none_type):
            cvv2 (str):
            employee_grat_tip (float):
            card_swipe_track1 (bool, date, datetime, dict, float, int, list, str, none_type):
            card_swipe_track2 (bool, date, datetime, dict, float, int, list, str, none_type):
            check_number (str):
            more_records_key (bool, date, datetime, dict, float, int, list, str, none_type):
            tip_amount (float):
            input_data (bool, date, datetime, dict, float, int, list, str, none_type):
            profit_center_id (str):
            invoice_number (str):
            receipt_text_image (bool, date, datetime, dict, float, int, list, str, none_type):
            brokerage_amount (float):
            amount (float):
            cover_count (float):
            more_records_flag (bool, date, datetime, dict, float, int, list, str, none_type):
            account_num (str):
            max_record_count (float):
            incremental_auth_amount (float):
            extra_data (bool, date, datetime, dict, float, int, list, str, none_type):
            check_type_id (str):
            posting_id (str):
            destination_property_id (str):
            account_detail (bool, date, datetime, dict, float, int, list, str, none_type):
            payment_amount (float):
            register_id (str):
            tndr_account_object (bool, date, datetime, dict, float, int, list, str, none_type):
            meal_period_id (str):

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

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.auth_amount = auth_amount
        self.server_emp_id = server_emp_id
        self.module_invoked = module_invoked
        self.cashier_emp_id = cashier_emp_id
        self.routing_id = routing_id
        self.auth_account_num = auth_account_num
        self.more_records_count = more_records_count
        self.payment_method_id = payment_method_id
        self.tag_data = tag_data
        self.total_auth_amount = total_auth_amount
        self.refund_flag = refund_flag
        self.close_time = close_time
        self.client_id = client_id
        self.change_amount = change_amount
        self.employee_id = employee_id
        self.training_mode_flag = training_mode_flag
        self.source_property_id = source_property_id
        self.associated_check_number = associated_check_number
        self.post_to_property_id = post_to_property_id
        self.unique_posting_id = unique_posting_id
        self.expire_date = expire_date
        self.by_name_flag = by_name_flag
        self.payment_slip_id = payment_slip_id
        self.financial_bin_detail = financial_bin_detail
        self.cvv2 = cvv2
        self.employee_grat_tip = employee_grat_tip
        self.card_swipe_track1 = card_swipe_track1
        self.card_swipe_track2 = card_swipe_track2
        self.check_number = check_number
        self.more_records_key = more_records_key
        self.tip_amount = tip_amount
        self.input_data = input_data
        self.profit_center_id = profit_center_id
        self.invoice_number = invoice_number
        self.receipt_text_image = receipt_text_image
        self.brokerage_amount = brokerage_amount
        self.amount = amount
        self.cover_count = cover_count
        self.more_records_flag = more_records_flag
        self.account_num = account_num
        self.max_record_count = max_record_count
        self.incremental_auth_amount = incremental_auth_amount
        self.extra_data = extra_data
        self.check_type_id = check_type_id
        self.posting_id = posting_id
        self.destination_property_id = destination_property_id
        self.account_detail = account_detail
        self.payment_amount = payment_amount
        self.register_id = register_id
        self.tndr_account_object = tndr_account_object
        self.meal_period_id = meal_period_id
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
