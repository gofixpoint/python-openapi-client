# coding: utf-8

"""
    fixpoint/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fixpoint_openapi.models.v1_tracing_filters import V1TracingFilters

class TestV1TracingFilters(unittest.TestCase):
    """V1TracingFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1TracingFilters:
        """Test V1TracingFilters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1TracingFilters`
        """
        model = V1TracingFilters()
        if include_optional:
            return V1TracingFilters(
                session_ids = [
                    ''
                    ],
                trace_ids = [
                    ''
                    ],
                span_ids = [
                    ''
                    ],
                parent_span_ids = [
                    ''
                    ]
            )
        else:
            return V1TracingFilters(
        )
        """

    def testV1TracingFilters(self):
        """Test V1TracingFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()