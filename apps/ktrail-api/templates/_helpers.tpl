{{- define "ktrail-api.name" -}}
ktrail-api
{{- end -}}

{{- define "ktrail-api.labels" -}}
app.kubernetes.io/name: ktrail-api
app.kubernetes.io/instance: ktrail-api
app.kubernetes.io/managed-by: Helm
{{- end -}}
