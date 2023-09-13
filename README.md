# Set up Kubernetes service discovery in Prometheus

## Architecture
Prometheus consists of multiple components.

the main Prometheus server that scrapes and stores the times series data by pulling them,
the service discovery that discovers the Kubernetes targets,
the Prometheus web UI for querying and visualizing the data.

