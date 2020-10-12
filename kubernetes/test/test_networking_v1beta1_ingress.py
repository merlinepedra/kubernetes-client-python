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
from kubernetes.client.models.networking_v1beta1_ingress import NetworkingV1beta1Ingress  # noqa: E501
from kubernetes.client.rest import ApiException

class TestNetworkingV1beta1Ingress(unittest.TestCase):
    """NetworkingV1beta1Ingress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetworkingV1beta1Ingress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.networking_v1beta1_ingress.NetworkingV1beta1Ingress()  # noqa: E501
        if include_optional :
            return NetworkingV1beta1Ingress(
                api_version = '0', 
                kind = '0', 
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : '0'
                        }, 
                    cluster_name = '0', 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        '0'
                        ], 
                    generate_name = '0', 
                    generation = 56, 
                    labels = {
                        'key' : '0'
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '0', 
                            fields_type = '0', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '0', 
                            operation = '0', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '0', 
                    namespace = '0', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '0', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '0', 
                            name = '0', 
                            uid = '0', )
                        ], 
                    resource_version = '0', 
                    self_link = '0', 
                    uid = '0', ), 
                spec = kubernetes.client.models.networking/v1beta1/ingress_spec.networking.v1beta1.IngressSpec(
                    backend = kubernetes.client.models.networking/v1beta1/ingress_backend.networking.v1beta1.IngressBackend(
                        service_name = '0', 
                        service_port = kubernetes.client.models.service_port.servicePort(), ), 
                    rules = [
                        kubernetes.client.models.networking/v1beta1/ingress_rule.networking.v1beta1.IngressRule(
                            host = '0', 
                            http = kubernetes.client.models.networking/v1beta1/http_ingress_rule_value.networking.v1beta1.HTTPIngressRuleValue(
                                paths = [
                                    kubernetes.client.models.networking/v1beta1/http_ingress_path.networking.v1beta1.HTTPIngressPath(
                                        backend = kubernetes.client.models.networking/v1beta1/ingress_backend.networking.v1beta1.IngressBackend(
                                            service_name = '0', 
                                            service_port = kubernetes.client.models.service_port.servicePort(), ), 
                                        path = '0', )
                                    ], ), )
                        ], 
                    tls = [
                        kubernetes.client.models.networking/v1beta1/ingress_tls.networking.v1beta1.IngressTLS(
                            hosts = [
                                '0'
                                ], 
                            secret_name = '0', )
                        ], ), 
                status = kubernetes.client.models.networking/v1beta1/ingress_status.networking.v1beta1.IngressStatus(
                    load_balancer = kubernetes.client.models.v1/load_balancer_status.v1.LoadBalancerStatus(
                        ingress = [
                            kubernetes.client.models.v1/load_balancer_ingress.v1.LoadBalancerIngress(
                                hostname = '0', 
                                ip = '0', )
                            ], ), )
            )
        else :
            return NetworkingV1beta1Ingress(
        )

    def testNetworkingV1beta1Ingress(self):
        """Test NetworkingV1beta1Ingress"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
