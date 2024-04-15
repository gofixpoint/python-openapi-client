# coding: utf-8

"""
    fixpoint/llmproxy/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.llmproxyv1_model import Llmproxyv1Model

class TestLlmproxyv1Model(unittest.TestCase):
    """Llmproxyv1Model unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Llmproxyv1Model:
        """Test Llmproxyv1Model
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Llmproxyv1Model`
        """
        model = Llmproxyv1Model()
        if include_optional:
            return Llmproxyv1Model(
                provider = '',
                name = '',
                spend_cap = openapi_client.models.v1_spend_cap.v1SpendCap(
                    amount = '', 
                    currency = '', 
                    reset_interval = 'RESET_INTERVAL_UNSPECIFIED', ),
                usage_totals = openapi_client.models.v1_usage_totals.v1UsageTotals(
                    amount = '', 
                    currency = '', 
                    tokens_used = 56, 
                    usage_reset_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return Llmproxyv1Model(
        )
        """

    def testLlmproxyv1Model(self):
        """Test Llmproxyv1Model"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
