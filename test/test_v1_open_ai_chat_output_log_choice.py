# coding: utf-8

"""
    fixpoint/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fixpoint_openapi.models.v1_open_ai_chat_output_log_choice import V1OpenAIChatOutputLogChoice

class TestV1OpenAIChatOutputLogChoice(unittest.TestCase):
    """V1OpenAIChatOutputLogChoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1OpenAIChatOutputLogChoice:
        """Test V1OpenAIChatOutputLogChoice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1OpenAIChatOutputLogChoice`
        """
        model = V1OpenAIChatOutputLogChoice()
        if include_optional:
            return V1OpenAIChatOutputLogChoice(
                index = '',
                message = fixpoint_openapi.models.v1_output_message.v1OutputMessage(
                    role = '', 
                    content = '', 
                    tool_calls = [
                        fixpoint_openapi.models.v1_tool_call.v1ToolCall(
                            id = '', 
                            type = '', 
                            function = fixpoint_openapi.models.tool_call_function.ToolCallFunction(
                                name = '', 
                                arguments = '', ), )
                        ], ),
                finish_reason = ''
            )
        else:
            return V1OpenAIChatOutputLogChoice(
        )
        """

    def testV1OpenAIChatOutputLogChoice(self):
        """Test V1OpenAIChatOutputLogChoice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
