{{- define "demo-api.name" -}}
demo-api
{{- end -}}

{{- define "demo-api.labels" -}}
app.kubernetes.io/name: demo-api
app.kubernetes.io/instance: demo-api
app.kubernetes.io/managed-by: Helm
{{- end -}}
