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
from kubernetes.client.models.v1_replica_set_spec import V1ReplicaSetSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ReplicaSetSpec(unittest.TestCase):
    """V1ReplicaSetSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ReplicaSetSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_replica_set_spec.V1ReplicaSetSpec()  # noqa: E501
        if include_optional :
            return V1ReplicaSetSpec(
                min_ready_seconds = 56, 
                replicas = 56, 
                selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(
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
                    spec = kubernetes.client.models.v1/pod_spec.v1.PodSpec(
                        active_deadline_seconds = 56, 
                        affinity = kubernetes.client.models.v1/affinity.v1.Affinity(
                            node_affinity = kubernetes.client.models.v1/node_affinity.v1.NodeAffinity(
                                preferred_during_scheduling_ignored_during_execution = [
                                    kubernetes.client.models.v1/preferred_scheduling_term.v1.PreferredSchedulingTerm(
                                        preference = kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                                            match_expressions = [
                                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                                    key = '0', 
                                                    operator = '0', 
                                                    values = [
                                                        '0'
                                                        ], )
                                                ], 
                                            match_fields = [
                                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                                    key = '0', 
                                                    operator = '0', )
                                                ], ), 
                                        weight = 56, )
                                    ], 
                                required_during_scheduling_ignored_during_execution = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
                                    node_selector_terms = [
                                        kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm()
                                        ], ), ), 
                            pod_affinity = kubernetes.client.models.v1/pod_affinity.v1.PodAffinity(), 
                            pod_anti_affinity = kubernetes.client.models.v1/pod_anti_affinity.v1.PodAntiAffinity(), ), 
                        automount_service_account_token = True, 
                        containers = [
                            kubernetes.client.models.v1/container.v1.Container(
                                args = [
                                    '0'
                                    ], 
                                command = [
                                    '0'
                                    ], 
                                env = [
                                    kubernetes.client.models.v1/env_var.v1.EnvVar(
                                        name = '0', 
                                        value = '0', 
                                        value_from = kubernetes.client.models.v1/env_var_source.v1.EnvVarSource(
                                            config_map_key_ref = kubernetes.client.models.v1/config_map_key_selector.v1.ConfigMapKeySelector(
                                                key = '0', 
                                                name = '0', 
                                                optional = True, ), 
                                            field_ref = kubernetes.client.models.v1/object_field_selector.v1.ObjectFieldSelector(
                                                api_version = '0', 
                                                field_path = '0', ), 
                                            resource_field_ref = kubernetes.client.models.v1/resource_field_selector.v1.ResourceFieldSelector(
                                                container_name = '0', 
                                                divisor = '0', 
                                                resource = '0', ), 
                                            secret_key_ref = kubernetes.client.models.v1/secret_key_selector.v1.SecretKeySelector(
                                                key = '0', 
                                                name = '0', 
                                                optional = True, ), ), )
                                    ], 
                                env_from = [
                                    kubernetes.client.models.v1/env_from_source.v1.EnvFromSource(
                                        config_map_ref = kubernetes.client.models.v1/config_map_env_source.v1.ConfigMapEnvSource(
                                            name = '0', 
                                            optional = True, ), 
                                        prefix = '0', 
                                        secret_ref = kubernetes.client.models.v1/secret_env_source.v1.SecretEnvSource(
                                            name = '0', 
                                            optional = True, ), )
                                    ], 
                                image = '0', 
                                image_pull_policy = '0', 
                                lifecycle = kubernetes.client.models.v1/lifecycle.v1.Lifecycle(
                                    post_start = kubernetes.client.models.v1/handler.v1.Handler(
                                        exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(), 
                                        http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                                            host = '0', 
                                            http_headers = [
                                                kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                                    name = '0', 
                                                    value = '0', )
                                                ], 
                                            path = '0', 
                                            port = kubernetes.client.models.port.port(), 
                                            scheme = '0', ), 
                                        tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                                            host = '0', 
                                            port = kubernetes.client.models.port.port(), ), ), 
                                    pre_stop = kubernetes.client.models.v1/handler.v1.Handler(), ), 
                                liveness_probe = kubernetes.client.models.v1/probe.v1.Probe(
                                    failure_threshold = 56, 
                                    initial_delay_seconds = 56, 
                                    period_seconds = 56, 
                                    success_threshold = 56, 
                                    timeout_seconds = 56, ), 
                                name = '0', 
                                ports = [
                                    kubernetes.client.models.v1/container_port.v1.ContainerPort(
                                        container_port = 56, 
                                        host_ip = '0', 
                                        host_port = 56, 
                                        name = '0', 
                                        protocol = '0', )
                                    ], 
                                readiness_probe = kubernetes.client.models.v1/probe.v1.Probe(
                                    failure_threshold = 56, 
                                    initial_delay_seconds = 56, 
                                    period_seconds = 56, 
                                    success_threshold = 56, 
                                    timeout_seconds = 56, ), 
                                resources = kubernetes.client.models.v1/resource_requirements.v1.ResourceRequirements(
                                    limits = {
                                        'key' : '0'
                                        }, 
                                    requests = {
                                        'key' : '0'
                                        }, ), 
                                security_context = kubernetes.client.models.v1/security_context.v1.SecurityContext(
                                    allow_privilege_escalation = True, 
                                    capabilities = kubernetes.client.models.v1/capabilities.v1.Capabilities(
                                        add = [
                                            '0'
                                            ], 
                                        drop = [
                                            '0'
                                            ], ), 
                                    privileged = True, 
                                    proc_mount = '0', 
                                    read_only_root_filesystem = True, 
                                    run_as_group = 56, 
                                    run_as_non_root = True, 
                                    run_as_user = 56, 
                                    se_linux_options = kubernetes.client.models.v1/se_linux_options.v1.SELinuxOptions(
                                        level = '0', 
                                        role = '0', 
                                        type = '0', 
                                        user = '0', ), 
                                    windows_options = kubernetes.client.models.v1/windows_security_context_options.v1.WindowsSecurityContextOptions(
                                        gmsa_credential_spec = '0', 
                                        gmsa_credential_spec_name = '0', 
                                        run_as_user_name = '0', ), ), 
                                startup_probe = kubernetes.client.models.v1/probe.v1.Probe(
                                    failure_threshold = 56, 
                                    initial_delay_seconds = 56, 
                                    period_seconds = 56, 
                                    success_threshold = 56, 
                                    timeout_seconds = 56, ), 
                                stdin = True, 
                                stdin_once = True, 
                                termination_message_path = '0', 
                                termination_message_policy = '0', 
                                tty = True, 
                                volume_devices = [
                                    kubernetes.client.models.v1/volume_device.v1.VolumeDevice(
                                        device_path = '0', 
                                        name = '0', )
                                    ], 
                                volume_mounts = [
                                    kubernetes.client.models.v1/volume_mount.v1.VolumeMount(
                                        mount_path = '0', 
                                        mount_propagation = '0', 
                                        name = '0', 
                                        read_only = True, 
                                        sub_path = '0', 
                                        sub_path_expr = '0', )
                                    ], 
                                working_dir = '0', )
                            ], 
                        dns_config = kubernetes.client.models.v1/pod_dns_config.v1.PodDNSConfig(
                            nameservers = [
                                '0'
                                ], 
                            options = [
                                kubernetes.client.models.v1/pod_dns_config_option.v1.PodDNSConfigOption(
                                    name = '0', 
                                    value = '0', )
                                ], 
                            searches = [
                                '0'
                                ], ), 
                        dns_policy = '0', 
                        enable_service_links = True, 
                        ephemeral_containers = [
                            kubernetes.client.models.v1/ephemeral_container.v1.EphemeralContainer(
                                image = '0', 
                                image_pull_policy = '0', 
                                name = '0', 
                                stdin = True, 
                                stdin_once = True, 
                                target_container_name = '0', 
                                termination_message_path = '0', 
                                termination_message_policy = '0', 
                                tty = True, 
                                working_dir = '0', )
                            ], 
                        host_aliases = [
                            kubernetes.client.models.v1/host_alias.v1.HostAlias(
                                hostnames = [
                                    '0'
                                    ], 
                                ip = '0', )
                            ], 
                        host_ipc = True, 
                        host_network = True, 
                        host_pid = True, 
                        hostname = '0', 
                        image_pull_secrets = [
                            kubernetes.client.models.v1/local_object_reference.v1.LocalObjectReference(
                                name = '0', )
                            ], 
                        init_containers = [
                            kubernetes.client.models.v1/container.v1.Container(
                                image = '0', 
                                image_pull_policy = '0', 
                                name = '0', 
                                stdin = True, 
                                stdin_once = True, 
                                termination_message_path = '0', 
                                termination_message_policy = '0', 
                                tty = True, 
                                working_dir = '0', )
                            ], 
                        node_name = '0', 
                        node_selector = {
                            'key' : '0'
                            }, 
                        overhead = {
                            'key' : '0'
                            }, 
                        preemption_policy = '0', 
                        priority = 56, 
                        priority_class_name = '0', 
                        readiness_gates = [
                            kubernetes.client.models.v1/pod_readiness_gate.v1.PodReadinessGate(
                                condition_type = '0', )
                            ], 
                        restart_policy = '0', 
                        runtime_class_name = '0', 
                        scheduler_name = '0', 
                        security_context = kubernetes.client.models.v1/pod_security_context.v1.PodSecurityContext(
                            fs_group = 56, 
                            run_as_group = 56, 
                            run_as_non_root = True, 
                            run_as_user = 56, 
                            supplemental_groups = [
                                56
                                ], 
                            sysctls = [
                                kubernetes.client.models.v1/sysctl.v1.Sysctl(
                                    name = '0', 
                                    value = '0', )
                                ], ), 
                        service_account = '0', 
                        service_account_name = '0', 
                        share_process_namespace = True, 
                        subdomain = '0', 
                        termination_grace_period_seconds = 56, 
                        tolerations = [
                            kubernetes.client.models.v1/toleration.v1.Toleration(
                                effect = '0', 
                                key = '0', 
                                operator = '0', 
                                toleration_seconds = 56, 
                                value = '0', )
                            ], 
                        topology_spread_constraints = [
                            kubernetes.client.models.v1/topology_spread_constraint.v1.TopologySpreadConstraint(
                                label_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                                    match_labels = {
                                        'key' : '0'
                                        }, ), 
                                max_skew = 56, 
                                topology_key = '0', 
                                when_unsatisfiable = '0', )
                            ], 
                        volumes = [
                            kubernetes.client.models.v1/volume.v1.Volume(
                                aws_elastic_block_store = kubernetes.client.models.v1/aws_elastic_block_store_volume_source.v1.AWSElasticBlockStoreVolumeSource(
                                    fs_type = '0', 
                                    partition = 56, 
                                    read_only = True, 
                                    volume_id = '0', ), 
                                azure_disk = kubernetes.client.models.v1/azure_disk_volume_source.v1.AzureDiskVolumeSource(
                                    caching_mode = '0', 
                                    disk_name = '0', 
                                    disk_uri = '0', 
                                    fs_type = '0', 
                                    kind = '0', 
                                    read_only = True, ), 
                                azure_file = kubernetes.client.models.v1/azure_file_volume_source.v1.AzureFileVolumeSource(
                                    read_only = True, 
                                    secret_name = '0', 
                                    share_name = '0', ), 
                                cephfs = kubernetes.client.models.v1/ceph_fs_volume_source.v1.CephFSVolumeSource(
                                    monitors = [
                                        '0'
                                        ], 
                                    path = '0', 
                                    read_only = True, 
                                    secret_file = '0', 
                                    user = '0', ), 
                                cinder = kubernetes.client.models.v1/cinder_volume_source.v1.CinderVolumeSource(
                                    fs_type = '0', 
                                    read_only = True, 
                                    volume_id = '0', ), 
                                config_map = kubernetes.client.models.v1/config_map_volume_source.v1.ConfigMapVolumeSource(
                                    default_mode = 56, 
                                    items = [
                                        kubernetes.client.models.v1/key_to_path.v1.KeyToPath(
                                            key = '0', 
                                            mode = 56, 
                                            path = '0', )
                                        ], 
                                    name = '0', 
                                    optional = True, ), 
                                csi = kubernetes.client.models.v1/csi_volume_source.v1.CSIVolumeSource(
                                    driver = '0', 
                                    fs_type = '0', 
                                    node_publish_secret_ref = kubernetes.client.models.v1/local_object_reference.v1.LocalObjectReference(
                                        name = '0', ), 
                                    read_only = True, 
                                    volume_attributes = {
                                        'key' : '0'
                                        }, ), 
                                downward_api = kubernetes.client.models.v1/downward_api_volume_source.v1.DownwardAPIVolumeSource(
                                    default_mode = 56, ), 
                                empty_dir = kubernetes.client.models.v1/empty_dir_volume_source.v1.EmptyDirVolumeSource(
                                    medium = '0', 
                                    size_limit = '0', ), 
                                fc = kubernetes.client.models.v1/fc_volume_source.v1.FCVolumeSource(
                                    fs_type = '0', 
                                    lun = 56, 
                                    read_only = True, 
                                    target_ww_ns = [
                                        '0'
                                        ], 
                                    wwids = [
                                        '0'
                                        ], ), 
                                flex_volume = kubernetes.client.models.v1/flex_volume_source.v1.FlexVolumeSource(
                                    driver = '0', 
                                    fs_type = '0', 
                                    read_only = True, ), 
                                flocker = kubernetes.client.models.v1/flocker_volume_source.v1.FlockerVolumeSource(
                                    dataset_name = '0', 
                                    dataset_uuid = '0', ), 
                                gce_persistent_disk = kubernetes.client.models.v1/gce_persistent_disk_volume_source.v1.GCEPersistentDiskVolumeSource(
                                    fs_type = '0', 
                                    partition = 56, 
                                    pd_name = '0', 
                                    read_only = True, ), 
                                git_repo = kubernetes.client.models.v1/git_repo_volume_source.v1.GitRepoVolumeSource(
                                    directory = '0', 
                                    repository = '0', 
                                    revision = '0', ), 
                                glusterfs = kubernetes.client.models.v1/glusterfs_volume_source.v1.GlusterfsVolumeSource(
                                    endpoints = '0', 
                                    path = '0', 
                                    read_only = True, ), 
                                host_path = kubernetes.client.models.v1/host_path_volume_source.v1.HostPathVolumeSource(
                                    path = '0', 
                                    type = '0', ), 
                                iscsi = kubernetes.client.models.v1/iscsi_volume_source.v1.ISCSIVolumeSource(
                                    chap_auth_discovery = True, 
                                    chap_auth_session = True, 
                                    fs_type = '0', 
                                    initiator_name = '0', 
                                    iqn = '0', 
                                    iscsi_interface = '0', 
                                    lun = 56, 
                                    portals = [
                                        '0'
                                        ], 
                                    read_only = True, 
                                    target_portal = '0', ), 
                                name = '0', 
                                nfs = kubernetes.client.models.v1/nfs_volume_source.v1.NFSVolumeSource(
                                    path = '0', 
                                    read_only = True, 
                                    server = '0', ), 
                                persistent_volume_claim = kubernetes.client.models.v1/persistent_volume_claim_volume_source.v1.PersistentVolumeClaimVolumeSource(
                                    claim_name = '0', 
                                    read_only = True, ), 
                                photon_persistent_disk = kubernetes.client.models.v1/photon_persistent_disk_volume_source.v1.PhotonPersistentDiskVolumeSource(
                                    fs_type = '0', 
                                    pd_id = '0', ), 
                                portworx_volume = kubernetes.client.models.v1/portworx_volume_source.v1.PortworxVolumeSource(
                                    fs_type = '0', 
                                    read_only = True, 
                                    volume_id = '0', ), 
                                projected = kubernetes.client.models.v1/projected_volume_source.v1.ProjectedVolumeSource(
                                    default_mode = 56, 
                                    sources = [
                                        kubernetes.client.models.v1/volume_projection.v1.VolumeProjection(
                                            secret = kubernetes.client.models.v1/secret_projection.v1.SecretProjection(
                                                name = '0', 
                                                optional = True, ), 
                                            service_account_token = kubernetes.client.models.v1/service_account_token_projection.v1.ServiceAccountTokenProjection(
                                                audience = '0', 
                                                expiration_seconds = 56, 
                                                path = '0', ), )
                                        ], ), 
                                quobyte = kubernetes.client.models.v1/quobyte_volume_source.v1.QuobyteVolumeSource(
                                    group = '0', 
                                    read_only = True, 
                                    registry = '0', 
                                    tenant = '0', 
                                    user = '0', 
                                    volume = '0', ), 
                                rbd = kubernetes.client.models.v1/rbd_volume_source.v1.RBDVolumeSource(
                                    fs_type = '0', 
                                    image = '0', 
                                    keyring = '0', 
                                    monitors = [
                                        '0'
                                        ], 
                                    pool = '0', 
                                    read_only = True, 
                                    user = '0', ), 
                                scale_io = kubernetes.client.models.v1/scale_io_volume_source.v1.ScaleIOVolumeSource(
                                    fs_type = '0', 
                                    gateway = '0', 
                                    protection_domain = '0', 
                                    read_only = True, 
                                    secret_ref = kubernetes.client.models.v1/local_object_reference.v1.LocalObjectReference(
                                        name = '0', ), 
                                    ssl_enabled = True, 
                                    storage_mode = '0', 
                                    storage_pool = '0', 
                                    system = '0', 
                                    volume_name = '0', ), 
                                secret = kubernetes.client.models.v1/secret_volume_source.v1.SecretVolumeSource(
                                    default_mode = 56, 
                                    optional = True, 
                                    secret_name = '0', ), 
                                storageos = kubernetes.client.models.v1/storage_os_volume_source.v1.StorageOSVolumeSource(
                                    fs_type = '0', 
                                    read_only = True, 
                                    volume_name = '0', 
                                    volume_namespace = '0', ), 
                                vsphere_volume = kubernetes.client.models.v1/vsphere_virtual_disk_volume_source.v1.VsphereVirtualDiskVolumeSource(
                                    fs_type = '0', 
                                    storage_policy_id = '0', 
                                    storage_policy_name = '0', 
                                    volume_path = '0', ), )
                            ], ), )
            )
        else :
            return V1ReplicaSetSpec(
                selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
        )

    def testV1ReplicaSetSpec(self):
        """Test V1ReplicaSetSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
