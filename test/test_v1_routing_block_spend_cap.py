# coding: utf-8

"""
    fixpoint/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fixpoint_openapi.models.v1_routing_block_spend_cap import V1RoutingBlockSpendCap

class TestV1RoutingBlockSpendCap(unittest.TestCase):
    """V1RoutingBlockSpendCap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1RoutingBlockSpendCap:
        """Test V1RoutingBlockSpendCap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1RoutingBlockSpendCap`
        """
        model = V1RoutingBlockSpendCap()
        if include_optional:
            return V1RoutingBlockSpendCap(
                fallback_strategy = 'FALLBACK_STRATEGY_UNSPECIFIED',
                terminal_state = 'TERMINAL_STATE_UNSPECIFIED',
                models = [
                    fixpoint_openapi.models.v1_spend_cap_model.v1SpendCapModel(
                        provider = '', 
                        name = '', 
                        spend_cap = fixpoint_openapi.models.fixpointv1_spend_cap.fixpointv1SpendCap(
                            amount = '', 
                            currency = '', 
                            reset_interval = 'RESET_INTERVAL_UNSPECIFIED', ), 
                        usage_totals = fixpoint_openapi.models.v1_usage_totals.v1UsageTotals(
                            amount = '', 
                            currency = '', 
                            tokens_used = 56, 
                            usage_reset_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ]
            )
        else:
            return V1RoutingBlockSpendCap(
        )
        """

    def testV1RoutingBlockSpendCap(self):
        """Test V1RoutingBlockSpendCap"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
