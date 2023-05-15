# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from azure.cli.core.commands.client_factory import (_prepare_mgmt_client_kwargs_track2, configure_common_settings,
                                                    get_mgmt_service_client)
from azure.cli.core.profiles import ResourceType
from azure.developer.devcenter import DevCenterClient
from azure.developer.devcenter.operations import DevBoxesOperations, DevCenterOperations, EnvironmentsOperations
from azure.mgmt.devcenter import DevCenterMgmtClient


def resource_client_factory(cli_ctx, subscription_id=None, **_):
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_RESOURCE_RESOURCES,
                                   subscription_id=subscription_id)


def auth_client_factory(cli_ctx, scope=None):
    import re
    subscription_id = None
    if scope:
        matched = re.match('/subscriptions/(?P<subscription>[^/]*)/', scope)
        if matched:
            subscription_id = matched.groupdict()['subscription']
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_AUTHORIZATION, subscription_id=subscription_id)


# def _graph_client_factory(cli_ctx, **_):
#     from ._msgrpah import GraphClient
#     client = GraphClient(cli_ctx)
#     return client

def get_graph_client(cli_ctx):
    from azure.cli.command_modules.role import graph_client_factory
    return graph_client_factory(cli_ctx)


def cf_dc_mgmt(cli_ctx, *_) -> DevCenterMgmtClient:
    return get_mgmt_service_client(cli_ctx, DevCenterMgmtClient)


def cf_dc_data(cli_ctx, dev_center, *_) -> DevCenterClient:

    from azure.cli.core._profile import Profile

    # Temporary set to Fidalgo until 1st party app is updated.
    dev_center_dns_suffix = 'devcenter.azure.com'
    dev_center_endpoint = f'https://{dev_center_dns_suffix}'

    # Temporary set to Fidalgo until 1st party app is updated.
    cli_ctx.cloud.endpoints.active_directory_resource_id = dev_center_endpoint

    profile = Profile(cli_ctx=cli_ctx)
    cred, subscription_id, tenant_id = profile.get_login_credentials(resource=dev_center_endpoint)
    client_kwargs = _prepare_mgmt_client_kwargs_track2(cli_ctx, cred)

    client = DevCenterClient(tenant_id=tenant_id, dev_center=dev_center, credential=cred,
                             dev_center_dns_suffix=dev_center_dns_suffix, **client_kwargs)

    return client


def cf_dc_data_dev_center(cli_ctx, dev_center, *_) -> DevCenterOperations:
    return cf_dc_data(cli_ctx, dev_center).dev_center


def cf_dc_data_dev_boxes(cli_ctx, dev_center, *_) -> DevBoxesOperations:
    return cf_dc_data(cli_ctx, dev_center).dev_boxes


def cf_dc_data_environments(cli_ctx, dev_center, *_) -> EnvironmentsOperations:
    return cf_dc_data(cli_ctx, dev_center).environments


# def cf_project_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).project


# def cf_pool_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).pool


# def cf_schedule_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).schedule


# def cf_dev_box_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).dev_box


# def cf_environment_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).environments


# def cf_artifact_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).artifacts


# def cf_catalog_item_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).catalog_item


# def cf_catalog_item_version_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).catalog_item_versions


# def cf_environment_type_dp(cli_ctx, dev_center, *_):
#     return cf_devcenter_dataplane(cli_ctx, dev_center).environment_type
