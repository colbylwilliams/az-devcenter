# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AttachedNetworkConnection
    from ._models_py3 import AttachedNetworkListResult
    from ._models_py3 import Capability
    from ._models_py3 import Catalog
    from ._models_py3 import CatalogListResult
    from ._models_py3 import CatalogProperties
    from ._models_py3 import CatalogUpdate
    from ._models_py3 import CatalogUpdateProperties
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import DevBoxDefinition
    from ._models_py3 import DevBoxDefinitionListResult
    from ._models_py3 import DevBoxDefinitionProperties
    from ._models_py3 import DevBoxDefinitionUpdate
    from ._models_py3 import DevBoxDefinitionUpdateProperties
    from ._models_py3 import DevCenter
    from ._models_py3 import DevCenterListResult
    from ._models_py3 import DevCenterSku
    from ._models_py3 import DevCenterUpdate
    from ._models_py3 import EnvironmentRole
    from ._models_py3 import EnvironmentType
    from ._models_py3 import EnvironmentTypeListResult
    from ._models_py3 import EnvironmentTypeUpdate
    from ._models_py3 import Gallery
    from ._models_py3 import GalleryListResult
    from ._models_py3 import GitCatalog
    from ._models_py3 import HealthCheck
    from ._models_py3 import HealthCheckStatusDetails
    from ._models_py3 import HealthCheckStatusDetailsListResult
    from ._models_py3 import Image
    from ._models_py3 import ImageListResult
    from ._models_py3 import ImageReference
    from ._models_py3 import ImageValidationErrorDetails
    from ._models_py3 import ImageVersion
    from ._models_py3 import ImageVersionListResult
    from ._models_py3 import ListUsagesResult
    from ._models_py3 import ManagedServiceIdentity
    from ._models_py3 import NetworkConnection
    from ._models_py3 import NetworkConnectionListResult
    from ._models_py3 import NetworkConnectionUpdate
    from ._models_py3 import NetworkConnectionUpdateProperties
    from ._models_py3 import NetworkProperties
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationStatus
    from ._models_py3 import OperationStatusError
    from ._models_py3 import Pool
    from ._models_py3 import PoolListResult
    from ._models_py3 import PoolProperties
    from ._models_py3 import PoolUpdate
    from ._models_py3 import PoolUpdateProperties
    from ._models_py3 import Project
    from ._models_py3 import ProjectEnvironmentType
    from ._models_py3 import ProjectEnvironmentTypeListResult
    from ._models_py3 import ProjectEnvironmentTypeProperties
    from ._models_py3 import ProjectEnvironmentTypeUpdate
    from ._models_py3 import ProjectEnvironmentTypeUpdateProperties
    from ._models_py3 import ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignment
    from ._models_py3 import ProjectListResult
    from ._models_py3 import ProjectProperties
    from ._models_py3 import ProjectUpdate
    from ._models_py3 import ProjectUpdateProperties
    from ._models_py3 import ProxyResource
    from ._models_py3 import RecommendedMachineConfiguration
    from ._models_py3 import Resource
    from ._models_py3 import ResourceRange
    from ._models_py3 import Schedule
    from ._models_py3 import ScheduleListResult
    from ._models_py3 import ScheduleProperties
    from ._models_py3 import ScheduleUpdate
    from ._models_py3 import ScheduleUpdateProperties
    from ._models_py3 import Sku
    from ._models_py3 import SkuListResult
    from ._models_py3 import SystemData
    from ._models_py3 import TrackedResource
    from ._models_py3 import TrackedResourceUpdate
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import UserRoleAssignmentValue
except (SyntaxError, ImportError):
    from ._models import AttachedNetworkConnection  # type: ignore
    from ._models import AttachedNetworkListResult  # type: ignore
    from ._models import Capability  # type: ignore
    from ._models import Catalog  # type: ignore
    from ._models import CatalogListResult  # type: ignore
    from ._models import CatalogProperties  # type: ignore
    from ._models import CatalogUpdate  # type: ignore
    from ._models import CatalogUpdateProperties  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import DevBoxDefinition  # type: ignore
    from ._models import DevBoxDefinitionListResult  # type: ignore
    from ._models import DevBoxDefinitionProperties  # type: ignore
    from ._models import DevBoxDefinitionUpdate  # type: ignore
    from ._models import DevBoxDefinitionUpdateProperties  # type: ignore
    from ._models import DevCenter  # type: ignore
    from ._models import DevCenterListResult  # type: ignore
    from ._models import DevCenterSku  # type: ignore
    from ._models import DevCenterUpdate  # type: ignore
    from ._models import EnvironmentRole  # type: ignore
    from ._models import EnvironmentType  # type: ignore
    from ._models import EnvironmentTypeListResult  # type: ignore
    from ._models import EnvironmentTypeUpdate  # type: ignore
    from ._models import Gallery  # type: ignore
    from ._models import GalleryListResult  # type: ignore
    from ._models import GitCatalog  # type: ignore
    from ._models import HealthCheck  # type: ignore
    from ._models import HealthCheckStatusDetails  # type: ignore
    from ._models import HealthCheckStatusDetailsListResult  # type: ignore
    from ._models import Image  # type: ignore
    from ._models import ImageListResult  # type: ignore
    from ._models import ImageReference  # type: ignore
    from ._models import ImageValidationErrorDetails  # type: ignore
    from ._models import ImageVersion  # type: ignore
    from ._models import ImageVersionListResult  # type: ignore
    from ._models import ListUsagesResult  # type: ignore
    from ._models import ManagedServiceIdentity  # type: ignore
    from ._models import NetworkConnection  # type: ignore
    from ._models import NetworkConnectionListResult  # type: ignore
    from ._models import NetworkConnectionUpdate  # type: ignore
    from ._models import NetworkConnectionUpdateProperties  # type: ignore
    from ._models import NetworkProperties  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationStatus  # type: ignore
    from ._models import OperationStatusError  # type: ignore
    from ._models import Pool  # type: ignore
    from ._models import PoolListResult  # type: ignore
    from ._models import PoolProperties  # type: ignore
    from ._models import PoolUpdate  # type: ignore
    from ._models import PoolUpdateProperties  # type: ignore
    from ._models import Project  # type: ignore
    from ._models import ProjectEnvironmentType  # type: ignore
    from ._models import ProjectEnvironmentTypeListResult  # type: ignore
    from ._models import ProjectEnvironmentTypeProperties  # type: ignore
    from ._models import ProjectEnvironmentTypeUpdate  # type: ignore
    from ._models import ProjectEnvironmentTypeUpdateProperties  # type: ignore
    from ._models import ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignment  # type: ignore
    from ._models import ProjectListResult  # type: ignore
    from ._models import ProjectProperties  # type: ignore
    from ._models import ProjectUpdate  # type: ignore
    from ._models import ProjectUpdateProperties  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import RecommendedMachineConfiguration  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceRange  # type: ignore
    from ._models import Schedule  # type: ignore
    from ._models import ScheduleListResult  # type: ignore
    from ._models import ScheduleProperties  # type: ignore
    from ._models import ScheduleUpdate  # type: ignore
    from ._models import ScheduleUpdateProperties  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuListResult  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import TrackedResourceUpdate  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageName  # type: ignore
    from ._models import UserAssignedIdentity  # type: ignore
    from ._models import UserRoleAssignmentValue  # type: ignore

from ._dev_center_enums import (
    ActionType,
    CreatedByType,
    DomainJoinType,
    EnableStatus,
    HealthCheckStatus,
    ImageValidationStatus,
    LicenseType,
    LocalAdminStatus,
    ManagedServiceIdentityType,
    Origin,
    ScheduledFrequency,
    ScheduledType,
    SkuTier,
    UsageUnit,
)

__all__ = [
    'AttachedNetworkConnection',
    'AttachedNetworkListResult',
    'Capability',
    'Catalog',
    'CatalogListResult',
    'CatalogProperties',
    'CatalogUpdate',
    'CatalogUpdateProperties',
    'CloudErrorBody',
    'DevBoxDefinition',
    'DevBoxDefinitionListResult',
    'DevBoxDefinitionProperties',
    'DevBoxDefinitionUpdate',
    'DevBoxDefinitionUpdateProperties',
    'DevCenter',
    'DevCenterListResult',
    'DevCenterSku',
    'DevCenterUpdate',
    'EnvironmentRole',
    'EnvironmentType',
    'EnvironmentTypeListResult',
    'EnvironmentTypeUpdate',
    'Gallery',
    'GalleryListResult',
    'GitCatalog',
    'HealthCheck',
    'HealthCheckStatusDetails',
    'HealthCheckStatusDetailsListResult',
    'Image',
    'ImageListResult',
    'ImageReference',
    'ImageValidationErrorDetails',
    'ImageVersion',
    'ImageVersionListResult',
    'ListUsagesResult',
    'ManagedServiceIdentity',
    'NetworkConnection',
    'NetworkConnectionListResult',
    'NetworkConnectionUpdate',
    'NetworkConnectionUpdateProperties',
    'NetworkProperties',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'OperationStatus',
    'OperationStatusError',
    'Pool',
    'PoolListResult',
    'PoolProperties',
    'PoolUpdate',
    'PoolUpdateProperties',
    'Project',
    'ProjectEnvironmentType',
    'ProjectEnvironmentTypeListResult',
    'ProjectEnvironmentTypeProperties',
    'ProjectEnvironmentTypeUpdate',
    'ProjectEnvironmentTypeUpdateProperties',
    'ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignment',
    'ProjectListResult',
    'ProjectProperties',
    'ProjectUpdate',
    'ProjectUpdateProperties',
    'ProxyResource',
    'RecommendedMachineConfiguration',
    'Resource',
    'ResourceRange',
    'Schedule',
    'ScheduleListResult',
    'ScheduleProperties',
    'ScheduleUpdate',
    'ScheduleUpdateProperties',
    'Sku',
    'SkuListResult',
    'SystemData',
    'TrackedResource',
    'TrackedResourceUpdate',
    'Usage',
    'UsageName',
    'UserAssignedIdentity',
    'UserRoleAssignmentValue',
    'ActionType',
    'CreatedByType',
    'DomainJoinType',
    'EnableStatus',
    'HealthCheckStatus',
    'ImageValidationStatus',
    'LicenseType',
    'LocalAdminStatus',
    'ManagedServiceIdentityType',
    'Origin',
    'ScheduledFrequency',
    'ScheduledType',
    'SkuTier',
    'UsageUnit',
]
