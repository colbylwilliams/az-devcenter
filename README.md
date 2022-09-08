# az-devcenter

Microsoft Azure CLI DevCenter Helper 'az' Extension adds useful "utilities" for common tasks.

## Install

To install the Azure CLI DevCenter Helper extension, simply run the following command:

```sh
az extension add --source https://github.com/colbylwilliams/az-devcenter/releases/latest/download/dc-0.0.3-py3-none-any.whl -y
```

### Update

To update Azure CLI DevCenter Helper extension to the latest version:

```sh
az dc upgrade
```

or for the latest pre-release version:

```sh
az dc upgrade --pre
```

## Commands

This extension adds the following commands.  Use `az dc -h` for more information.
| Command | Description |
| ------- | ----------- |
| [az dc user check](#az-dc-user-check) | Check if a user has appropriate licenses to use dev box. |
| [az dc box list](#az-dc-box-list) | List dev boxes. |
| [az dc box start](#az-dc-box-start) | Start dev boxes. |
| [az dc box stop](#az-dc-box-stop) | Stop dev boxes. |
| [az dc project box list](#az-dc-project-box-list) | List project dev boxes. |
| [az dc project box start](#az-dc-project-box-start) | Start project dev boxes. |
| [az dc project box stop](#az-dc-project-box-stop) | Stop project dev boxes. |
| [az dc project user add](#az-dc-project-user-add) | Add a dev box user to a project. |
| [az dc project user remove](#az-dc-project-user-remove) | Remove a dev box user from a project. |
| [az dc project admin add](#az-dc-project-admin-add) | Add a project admin to a project. |
| [az dc project admin remove](#az-dc-project-admin-remove) | Remove a project admin from a project. |

---

### `az dc user check`

Check if a user has appropriate licenses to use dev box.

```sh
az dc user check --user
```

#### Examples

```sh
az dc user check --user user@example.com

# output: user@example.com has valid licenses for dev box: ['SPE_E3']
```

### `az dc box list`

List dev boxes.

```sh
box list --dev-center
         [--projects]
         [--pools]
         [--users]
```

#### Examples:

List all dev boxes in a dev center.

```sh
az dc box list -dc MyDevCenter
```

List all dev boxes in a specific project in a dev center.

```sh
az dc box list -dc MyDevCenter --projects MyProject
```

List all dev boxes in a dev center belonging to specific users.

```sh
az dc box list -dc MyDevCenter --users userA userB
```

### `az dc box start`

Start dev boxes.

```sh
box start --dev-center
          [--projects]
          [--pools]
          [--users]
```

#### Examples:

Start all dev boxes in a dev center.

```sh
az dc box start -dc MyDevCenter
```

Start all dev boxes in a specific project in a dev center.

```sh
az dc box start -dc MyDevCenter --projects MyProject
```

Start all dev boxes in a dev center belonging to specific users.

```sh
az dc box start -dc MyDevCenter --users userA userB
```

### `az dc box stop`

Stop dev boxes.

```sh
box stop --dev-center
         [--projects]
         [--pools]
         [--users]
```

#### Examples:

Stop all dev boxes in a dev center.

```sh
az dc box stop -dc MyDevCenter
```

Stop all dev boxes in a specific project in a dev center.

```sh
az dc box stop -dc MyDevCenter --projects MyProject
```

Stop all dev boxes in a dev center belonging to specific users.

```sh
az dc box stop -dc MyDevCenter --users userA userB
```

### `az dc project box list`

List project dev boxes.

```sh
project box list --dev-center
                 [--pools]
                 [--users]
```

#### Examples:

List all dev boxes in a project.

```sh
az dc project box list -dc MyDevCenter -p MyProject
```

List all dev boxes in specific pools in a project.

```sh
az dc project box list -dc MyDevCenter -p MyProject --pools poolA poolB
```

List all dev boxes in a project belonging to specific users.

```sh
az dc project box list -dc MyDevCenter -p MyProject --users userA userB
```

### `az dc project box start`

Start project dev boxes.

```sh
project box start --dev-center
                  [--pools]
                  [--users]
```

#### Examples:

Start all dev boxes in a project.

```sh
az dc project box start -dc MyDevCenter -p MyProject
```

Start all dev boxes in specific pools in a project.

```sh
az dc project box start -dc MyDevCenter -p MyProject --pools poolA poolB
```

Start all dev boxes in a project belonging to specific users.

```sh
az dc project box start -dc MyDevCenter -p MyProject --users userA userB
```

### `az dc project box stop`

Stop project dev boxes.

```sh
project box stop --dev-center
                 [--pools]
                 [--users]
```

#### Examples:

Stop all dev boxes in a project.

```sh
az dc project box stop -dc MyDevCenter -p MyProject
```

Stop all dev boxes in specific pools in a project.

```sh
az dc project box stop -dc MyDevCenter -p MyProject --pools poolA poolB
```

Stop all dev boxes in a project belonging to specific users.

```sh
az dc project box stop -dc MyDevCenter -p MyProject --users userA userB
```

### `az dc project user add`

Add a dev box user to a project.

```sh
project user add --project
                 --user-id
                 [--skip-license-check]
```

#### Examples:

Add a dev box user to a project.

```sh
az dc project user add -g projectRG -p MyProject -u me
```

### `az dc project user remove`

Remove a dev box user from a project.

```sh
project user remove --project
                    --user-id
```

#### Examples:

Remove a dev box user from a project.

```sh
az dc project user remove -g projectRG -p MyProject -u me
```

### `az dc project admin add`

Add a project admin to a project.

```sh
project admin add --project
                  --user-id
```

#### Examples:

Add a project admin to a project.

```sh
az dc project admin add -g projectRG -p MyProject -u me
```

### `az dc project admin remove`

Remove a project admin from a project.

```sh
project admin remove --project
                     --user-id
```

#### Examples:

Remove a project admin from a project.

```sh
az dc project admin remove -g projectRG -p MyProject -u me
```
