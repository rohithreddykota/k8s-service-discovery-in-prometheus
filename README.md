# Set up Kubernetes service discovery in Prometheus

## Architecture
Prometheus consists of multiple components.

the main Prometheus server that scrapes and stores the times series data by pulling them,
the service discovery that discovers the Kubernetes targets,
the Prometheus web UI for querying and visualizing the data.

## Execution Steps

- create k8s resources

```sh
kubectl apply -f manifests/namespace.yaml && kubectal apply -f manifests/
```

- check the created objects

```sh
kubectl get all -n monitoring
```

- port-forward to prometheus service

```sh
kubectl -n monitoring port-forward svc/prometheus 9090:9090
```
