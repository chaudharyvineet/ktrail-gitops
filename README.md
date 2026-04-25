# Platform GitOps Demo on Self-Managed GCP Kubernetes

Production-grade  GitOps, Kubernetes, observability, and security controls.

## Stack

- Kubernetes on GCP self-managed cluster
- ArgoCD for GitOps
- Helm for app packaging
- Prometheus + Grafana via kube-prometheus-stack
- ServiceMonitor for app metrics
- NetworkPolicy, RBAC, securityContext, resource limits
- GitHub Actions + Trivy image scanning

## Repo Layout

```text
platform-gitops-demo/
├── app/                         #  Python API with /metrics
├── apps/demo-api/               # Helm chart for app
├── argocd/                      # ArgoCD Application manifests
├── monitoring/                  # kube-prometheus-stack values
├── security/                    # Optional namespace/security policies
└── .github/workflows/           # CI security scan example
```

## 1. Install ArgoCD

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Get initial password:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath='{.data.password}' | base64 --decode && echo
```

## 2. Update repo URL

Edit these files and replace `YOUR_USERNAME`:

- `argocd/monitoring-app.yaml`
- `argocd/demo-api-app.yaml`

## 3. Deploy monitoring through ArgoCD

```bash
kubectl apply -f argocd/monitoring-app.yaml
```

Check pods:

```bash
kubectl get pods -n monitoring
```

Access Grafana:

```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```

Login:

```text
admin / admin
```

## 4. Deploy demo app through ArgoCD

```bash
kubectl apply -f argocd/demo-api-app.yaml
kubectl get pods -n demo-api
```

Access app:

```bash
kubectl port-forward svc/demo-api -n demo-api 8080:80
curl http://localhost:8080/
curl http://localhost:8080/metrics
```

## 5. Demo GitOps self-healing

Manually scale the app:

```bash
kubectl scale deployment demo-api -n demo-api --replicas=1
```

ArgoCD should detect drift and restore it back to the desired replica count from Git.

## 6. Resume Bullet

Built a secure GitOps platform on self-managed GCP Kubernetes using ArgoCD, Helm, Prometheus, Grafana, RBAC, NetworkPolicies, and hardened pod security controls to demonstrate automated deployments, drift correction, observability, and secure platform operations.
