import aws_cdk as core
import aws_cdk.assertions as assertions

from scalable_django_graphql.scalable_django_graphql_stack import ScalableDjangoGraphqlStack

# example tests. To run these tests, uncomment this file along with the example
# resource in scalable_django_graphql/scalable_django_graphql_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ScalableDjangoGraphqlStack(app, "scalable-django-graphql")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
