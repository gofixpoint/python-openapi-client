# coding: utf-8

"""
    fixpoint/llmproxy/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v1_create_app_logs_request import V1CreateAppLogsRequest

class TestV1CreateAppLogsRequest(unittest.TestCase):
    """V1CreateAppLogsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CreateAppLogsRequest:
        """Test V1CreateAppLogsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CreateAppLogsRequest`
        """
        model = V1CreateAppLogsRequest()
        if include_optional:
            return V1CreateAppLogsRequest(
                app_logs = [
                    openapi_client.models.v1_app_log.v1AppLog(
                        name = '', 
                        trace_id = '', 
                        level = 'TRACE', 
                        message = '', 
                        additional_info = openapi_client.models.additional_info.additionalInfo(), 
                        event_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return V1CreateAppLogsRequest(
        )
        """

    def testV1CreateAppLogsRequest(self):
        """Test V1CreateAppLogsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
