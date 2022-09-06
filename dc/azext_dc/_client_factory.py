# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from azure.cli.core.commands.client_factory import get_mgmt_service_client
from azure.cli.core.profiles import ResourceType


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


def devcenter_client_factory(cli_ctx, *_):
    from azext_dc.vendored_sdks.devcenter import DevCenter
    return get_mgmt_service_client(cli_ctx, DevCenter)

# below from:
# https://github.com/tbyfield/azure-cli-extensions/blob/main/src/devcenter/azext_devcenter/manual/_client_factory.py


def cf_devcenter_dataplane(cli_ctx, dev_center, *_):

    from azure.cli.core._profile import Profile

    from azext_dc.vendored_sdks.devcenter_dataplane import \
        DevCenterDataplaneClient

    # Temporary set to Fidalgo until 1st party app is updated.
    cli_ctx.cloud.endpoints.active_directory_resource_id = 'https://devcenter.azure.com'

    profile = Profile(cli_ctx=cli_ctx)
    subscription = profile.get_subscription()
    tenant_id = subscription['tenantId']
    cloud = subscription['environmentName']
    dev_center_dns_suffix = get_dns_suffix(cloud)

    # Override the client to use DevCenter resource rather than ARM's.
    # The .default scope will be appended by the mgmt service client
    # cli_ctx.cloud.endpoints.active_directory_resource_id = 'https://devcenter.azure.com'

    return get_mgmt_service_client(
        cli_ctx,
        DevCenterDataplaneClient,
        subscription_bound=False,
        base_url_bound=False,
        tenant_id=tenant_id,
        dev_center=dev_center,
        dev_center_dns_suffix=dev_center_dns_suffix)


def get_dns_suffix(cloud):
    if cloud == "Dogfood":
        return 'devcenter.azure-test.net'
    return 'devcenter.azure.com'


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
