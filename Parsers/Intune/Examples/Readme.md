

## Event Logs

### Audit Logs

*Log Syntax*

```json
{
  "time": "2024-12-20T00:33:45.9126000Z",
  "tenantId": "[TENANT_ID]",
  "category": "AuditLogs",
  "operationName": [Operation],
  "properties": {
    "ActivityDate": [Activity Date],
    "ActivityResultStatus": 1,
    "ActivityType": 0,
    "Actor": {
      "ActorType": 1,
      "Application": null,
      "ApplicationName": null,
      "IsDelegatedAdmin": false,
      "Name": "[ACTOR_NAME]",
      "ObjectId": "[OBJECT_ID]",
      "PartnerTenantId": "[PARTNER_TENANT_ID]",
      "UserPermissions": ["[PERMISSION]"],
      "UPN": "[EMAIL]"
    },
    "AdditionalDetails": "",
    "AuditEventId": "[AUDIT_EVENT_ID]",
    "Category": 1,
    "RelationId": null,
    "TargetDisplayNames": ["<null>"],
    "TargetObjectIds": ["[TARGET_OBJECT_ID]"],
    "Targets": [
      {
        "ModifiedProperties": [
          {
            "Name": "AccountContextId",
            "Old": null,
            "New": "[ACCOUNT_CONTEXT_ID]"
          },
          {
            "Name": "deviceID",
            "Old": null,
            "New": "[DEVICE_ID]"
          },
          {
            "Name": "DeviceEnrollmentType",
            "Old": null,
            "New": "10"
          },
          {
            "Name": "Thumbprint",
            "Old": null,
            "New": "[THUMBPRINT]"
          }
        ],
        "Name": null
      }
    ]
  },
  "resultType": "Success",
  "resultDescription": "None",
  "correlationId": "[CORRELATION_ID]",
  "identity": "[EMAIL]"
}
```

* Sample log *

```json
{
  "time": "2024-12-21T01:45:10.1234000Z",
  "tenantId": "b53a5e71-a22f-41a3-b56c-23d42ab2df33",
  "category": "AuditLogs",
  "operationName": "Update ClientCertificate",
  "properties": {
    "ActivityDate": "12/21/2024 1:45:10 AM",
    "ActivityResultStatus": 0,
    "ActivityType": 1,
    "Actor": {
      "ActorType": 2,
      "Application": null,
      "ApplicationName": null,
      "IsDelegatedAdmin": true,
      "Name": "Alexandra Rodriguez",
      "ObjectId": "432f8c11-4e45-48a6-b1b5-e63d92ab75ac",
      "PartnerTenantId": "11111111-0000-0000-0000-000000001234",
      "UserPermissions": ["*"],
      "UPN": "alex.rodriguez@examplecorp.com"
    },
    "AdditionalDetails": "",
    "AuditEventId": "654321aa-bc23-c456-a789-f0123456789a",
    "Category": 1,
    "RelationId": null,
    "TargetDisplayNames": [
            "\u003cnull\u003e"
        ],
    "TargetObjectIds": ["4F3B1CB1DC7957A814998A3E9D3919E5D3601E88"],
    "Targets": [
      {
        "ModifiedProperties": [
          {
            "Name": "AccountContextId",
            "Old": null,
            "New": "b53a5e71-a22f-41a3-b56c-23d42ab2df33"
          },
          {
            "Name": "deviceID",
            "Old": null,
            "New": "12345678-9012-3456-7890-abcd1234ef01"
          },
          {
            "Name": "DeviceEnrollmentType",
            "Old": null,
            "New": "20"
          },
          {
            "Name": "Thumbprint",
            "Old": null,
            "New": "9A2B3C1D8E7F6G5H4I3J2K9L0N8M7P6Q5R4S3T2U1V0"
          }
        ],
        "Name": "Certificate for Test Purpose"
      }
    ]
  },
  "resultType": "Success",
  "resultDescription": "Operation completed successfully.",
  "correlationId": "98765432-10fe-cdab-a890-bcdef0123456",
  "identity": "alex.rodriguez@examplecorp.com"
}
```

*One Line*

```json
{"time":"2024-12-21T01:45:10.1234000Z","tenantId":"b53a5e71-a22f-41a3-b56c-23d42ab2df33","category":"AuditLogs","operationName":"Update ClientCertificate","properties":{"ActivityDate":"12/21/2024 1:45:10 AM","ActivityResultStatus":0,"ActivityType":1,"Actor":{"ActorType":2,"Application":null,"ApplicationName":null,"IsDelegatedAdmin":true,"Name":"Alexandra Rodriguez","ObjectId":"432f8c11-4e45-48a6-b1b5-e63d92ab75ac","PartnerTenantId":"11111111-0000-0000-0000-000000001234","UserPermissions":["*"],"UPN":"alex.rodriguez@examplecorp.com"},"AdditionalDetails":"","AuditEventId":"654321aa-bc23-c456-a789-f0123456789a","Category":1,"RelationId":null,"TargetDisplayNames":["\u003cnull\u003e"],"TargetObjectIds":["4F3B1CB1DC7957A814998A3E9D3919E5D3601E88"],"Targets":[{"ModifiedProperties":[{"Name":"AccountContextId","Old":null,"New":"b53a5e71-a22f-41a3-b56c-23d42ab2df33"},{"Name":"deviceID","Old":null,"New":"12345678-9012-3456-7890-abcd1234ef01"},{"Name":"DeviceEnrollmentType","Old":null,"New":"20"},{"Name":"Thumbprint","Old":null,"New":"9A2B3C1D8E7F6G5H4I3J2K9L0N8M7P6Q5R4S3T2U1V0"}],"Name":"
```

## Operational Logs

* Log Syntax *

```json
{
  "time": "2024-12-20T00:33:46.2052000Z",
  "tenantId": "[TENANT_ID]",
  "category": "OperationalLogs",
  "operationName": "Enrollment",
  "resultType": "Success",
  "properties": {
    "AADDeviceId": "[AAD_DEVICE_ID]",
    "IntuneDeviceId": "[INTUNE_DEVICE_ID]",
    "IntuneAccountId": "[INTUNE_ACCOUNT_ID]",
    "IntuneUserId": "[INTUNE_USER_ID]",
    "MessageId": "[MESSAGE_ID]",
    "AADTenantId": "[AAD_TENANT_ID]",
    "OperationalLogCategory": "DeviceEnrollment",
    "EnrollmentTimeUTC": "2024-12-20T00:33:46.2052Z",
    "ScenarioName": "Microsoft.Management.Services.Diagnostics.SLAEvents.EnrollmentSLAEvent",
    "OsVersion": "[OS_VERSION]",  // Depending on the context, this might not need to be redacted
    "ScaleUnit": "[SCALE_UNIT]",
    "Os": "Windows",
    "EnrollmentType": "WindowsAutoEnrollment",
    "FailureReason": "Unknown",
    "FailureCategory": "Not Applicable"
  }
}
```

* Example Log *

```json
{
  "time": "2024-12-20T00:33:46.2052000Z",
  "tenantId": "49f8a7b6-e2d1-41ac-b3c5-64c7e18f1234",
  "category": "OperationalLogs",
  "operationName": "Enrollment",
  "resultType": "Success",
  "properties": {
    "AADDeviceId": "83d9a21b-d67e-45ab-a32d-9bae85c67890",
    "IntuneDeviceId": "15f64a2f-b41a-4a5c-93ce-111e3ac8bf56",
    "IntuneAccountId": "25b6c79f-e511-43da-81af-f6be5d9f2310",
    "IntuneUserId": "42c1a51d-75cd-4212-ba95-85c21a432109",
    "MessageId": "93ce4a3e-c21b-41ab-a98c-e53211ac43fd",
    "AADTenantId": "19f8a7b6-e2d1-41ac-b3c5-64c7e18f1234",
    "OperationalLogCategory": "DeviceEnrollment",
    "EnrollmentTimeUTC": "2024-12-20T00:33:46.2052Z",
    "ScenarioName": "Microsoft.Management.Services.Diagnostics.SLAEvents.EnrollmentSLAEvent",
    "OsVersion": "10.0.12345.6789",
    "ScaleUnit": "SU001",
    "Os": "Windows",
    "EnrollmentType": "WindowsAutoEnrollment",
    "FailureReason": "None",
    "FailureCategory": "Not Applicable"
  }
}
```


*One Line*

```json
{"time":"2024-12-20T00:33:46.2052000Z","tenantId":"49f8a7b6-e2d1-41ac-b3c5-64c7e18f1234","category":"OperationalLogs","operationName":"Enrollment","resultType":"Success","properties":{"AADDeviceId":"83d9a21b-d67e-45ab-a32d-9bae85c67890","IntuneDeviceId":"15f64a2f-b41a-4a5c-93ce-111e3ac8bf56","IntuneAccountId":"25b6c79f-e511-43da-81af-f6be5d9f2310","IntuneUserId":"42c1a51d-75cd-4212-ba95-85c21a432109","MessageId":"93ce4a3e-c21b-41ab-a98c-e53211ac43fd","AADTenantId":"19f8a7b6-e2d1-41ac-b3c5-64c7e18f1234","OperationalLogCategory":"DeviceEnrollment","EnrollmentTimeUTC":"2024-12-20T00:33:46.2052Z","ScenarioName":"Microsoft.Management.Services.Diagnostics.SLAEvents.EnrollmentSLAEvent","OsVersion":"10.0.12345.6789","ScaleUnit":"SU001","Os":"Windows","EnrollmentType":"WindowsAutoEnrollment","FailureReason":"None","FailureCategory":"Not Applicable"}}
```