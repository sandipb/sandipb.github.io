# gcloud runbook

CLI commands I found useful while working with GCP projects.

## General

### Fetch list of projects accessible by the user id

```console
$ gcloud projects list --filter "PROJECT_ID:*k8s*"
PROJECT_ID              NAME                    PROJECT_NUMBER
sb-gcp-k8s              sb-gcp-k8s              123456789012
```

### Create and download keys for a service account

```shell-session
$ SVC_ACCT="reader@PROJECT_NAME.iam.gserviceaccount.com"

$ gcloud  --project PROJECT_NAME iam service-accounts keys create --iam-account="${SVC_ACCT}" "${SVC_ACCT}.json"
...
```

### List SSH keys added to project

```bash
gcloud  --project PROJECT_NAME compute project-info describe\
   | yq e '.commonInstanceMetadata.items[]|select(.key=="ssh-keys")|.value'
```

### Adding SSH keys to a project

You need to download the list from the previous commands to a file, edit it for adding/modifying/deleting keys,
and then add the new file back using:

```bash
gcloud --project PROJECT_NAME compute project-info add-metadata --metadata-from-file ssh-keys=PATH_TO_FILE
```

[Reference](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys#gcloud_1)

## Logging

### Search for logs for an operation

Use the operation ID to look up the start (`operation.first==true`) or end (`operation.last==true`) of the operation,

```bash
gcloud logging read --format=json 'operation.id="operation-162871234567-45678"' \
  | jq '.[] | { operation, timestamp, \
       request: .protoPayload.request, \
       response: .protoPayload.response, \
       metadata: .protoPayload.metadata}'
```

## Kubernetes

### List kubernetes clusters in your project

```shell-session
$ gcloud  --project PROJECT_NAME container clusters list
NAME     LOCATION     MASTER_VERSION   MASTER_IP      MACHINE_TYPE    NODE_VERSION      NUM_NODES  STATUS
cluster-a  us-central1  1.20.9-gke.1001  10.100.100.100  n1-standard-32  1.20.9-gke.701 *  5         RUNNING

* - There is an upgrade available for your cluster(s).
```

### Describe Master Control plane

```bash
gcloud container clusters describe "cluster-a"  \
                                   --project PROJECT_NAME \
                                   --region "us-east4" --format "json" \
    | jq '{currentMasterVersion, releaseChannel, notificationConfig}'
```

```json
{
  "currentMasterVersion": "1.20.8-gke.900",
  "releaseChannel": {
    "channel": "REGULAR"
  },
  "notificationConfig": {
    "pubsub": {
      "enabled": true,
      "topic": "projects/PROJECT_NAME/topics/upgrade-notifications"
    }
  }
}
```

### View Nodepools

```shell-session
$ gcloud container node-pools  list --cluster cluster-a --project PROJECT_NAME
NAME                      MACHINE_TYPE    DISK_SIZE_GB  NODE_VERSION
ingress                   n1-standard-16  100           1.20.8-gke.900
egress                    n2-standard-8   110           1.20.8-gke.900
main-node-pool            n2-standard-32  300           1.20.8-gke.900
```
