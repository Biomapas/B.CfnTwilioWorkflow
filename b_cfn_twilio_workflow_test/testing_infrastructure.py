from aws_cdk.core import Stack

from b_cfn_twilio_workflow.function import TwilioWorkflowSingletonFunction
from b_cfn_twilio_workflow.resource import TwilioWorkflowResource


class TestingInfrastructure(Stack):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'TestingStack',
            stack_name=f'TestingStack'
        )

        function = TwilioWorkflowSingletonFunction(
            scope=self,
            name='TestingFunction',
            twilio_account_sid='Test1',
            twilio_auth_token='Test2',
            twilio_workspace_sid='Test3',
            twilio_task_queue_sid='Test4',
        )

        TwilioWorkflowResource(
            scope=self,
            workflow_function=function,
            workflow_name='TestWorkflow'
        )
