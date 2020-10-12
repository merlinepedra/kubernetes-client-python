# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta1_mutating_webhook import V1beta1MutatingWebhook  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1MutatingWebhook(unittest.TestCase):
    """V1beta1MutatingWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1MutatingWebhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_mutating_webhook.V1beta1MutatingWebhook()  # noqa: E501
        if include_optional :
            return V1beta1MutatingWebhook(
                admission_review_versions = [
                    '0'
                    ], 
                kubernetes.client_config = kubernetes.client.models.admissionregistration/v1beta1/webhook_client_config.admissionregistration.v1beta1.WebhookClientConfig(
                    ca_bundle = 'YQ==', 
                    service = kubernetes.client.models.admissionregistration/v1beta1/service_reference.admissionregistration.v1beta1.ServiceReference(
                        name = '0', 
                        namespace = '0', 
                        path = '0', 
                        port = 56, ), 
                    url = '0', ), 
                failure_policy = '0', 
                match_policy = '0', 
                name = '0', 
                namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ), 
                object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ), 
                reinvocation_policy = '0', 
                rules = [
                    kubernetes.client.models.v1beta1/rule_with_operations.v1beta1.RuleWithOperations(
                        api_groups = [
                            '0'
                            ], 
                        api_versions = [
                            '0'
                            ], 
                        operations = [
                            '0'
                            ], 
                        resources = [
                            '0'
                            ], 
                        scope = '0', )
                    ], 
                side_effects = '0', 
                timeout_seconds = 56
            )
        else :
            return V1beta1MutatingWebhook(
                kubernetes.client_config = kubernetes.client.models.admissionregistration/v1beta1/webhook_client_config.admissionregistration.v1beta1.WebhookClientConfig(
                    ca_bundle = 'YQ==', 
                    service = kubernetes.client.models.admissionregistration/v1beta1/service_reference.admissionregistration.v1beta1.ServiceReference(
                        name = '0', 
                        namespace = '0', 
                        path = '0', 
                        port = 56, ), 
                    url = '0', ),
                name = '0',
        )

    def testV1beta1MutatingWebhook(self):
        """Test V1beta1MutatingWebhook"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
