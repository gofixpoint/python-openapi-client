# coding: utf-8

"""
    fixpoint/llmproxy/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v1_open_ai_chat_output_log import V1OpenAIChatOutputLog

class TestV1OpenAIChatOutputLog(unittest.TestCase):
    """V1OpenAIChatOutputLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1OpenAIChatOutputLog:
        """Test V1OpenAIChatOutputLog
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1OpenAIChatOutputLog`
        """
        model = V1OpenAIChatOutputLog()
        if include_optional:
            return V1OpenAIChatOutputLog(
                name = '',
                input_name = '',
                openai_id = '',
                model_name = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                choices = [
                    openapi_client.models.v1_open_ai_chat_output_log_choice.v1OpenAIChatOutputLogChoice(
                        index = '', 
                        message = openapi_client.models.v1_output_message.v1OutputMessage(
                            role = '', 
                            content = '', 
                            tool_calls = [
                                openapi_client.models.v1_tool_call.v1ToolCall(
                                    id = '', 
                                    type = '', 
                                    function = openapi_client.models.tool_call_function.ToolCallFunction(
                                        name = '', 
                                        arguments = '', ), )
                                ], ), 
                        finish_reason = '', )
                    ],
                usage = openapi_client.models.v1_open_ai_chat_output_log_usage.v1OpenAIChatOutputLogUsage(
                    prompt_tokens = 56, 
                    completion_tokens = 56, 
                    total_tokens = 56, ),
                trace_id = ''
            )
        else:
            return V1OpenAIChatOutputLog(
        )
        """

    def testV1OpenAIChatOutputLog(self):
        """Test V1OpenAIChatOutputLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
