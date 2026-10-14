# Resource isolation

Read this reference when a change starts local services or touches shared resources. Record every allocation and verify its identity before modifying or removing it. Cleanup requires authorization and must match recorded allocations.

| Resource | Isolation |
| --- | --- |
| Ports | Select free ports and pass them through local configuration |
| SQL | Use a dedicated database or instance and verify migration targets |
| SQLite | Place the database file inside the task's allocated directory |
| Cache | Use a dedicated instance or database, or a scoped key prefix |
| Queues and workers | Use unique queue or topic names and never consume from shared queues |
| Containers | Set a unique project identity, volume set, and published port mapping |
| Object storage | Use a dedicated non-production bucket or emulator namespace |
| Files | Allocate dedicated directories for uploads, temporary data, and generated output |
| Email and webhooks | Route to local sinks or authorized test endpoints |

A key prefix is not a dedicated cache database; never flush a shared cache instance to clean up prefixed keys. Container project names alone do not isolate explicitly named volumes or external services, so inspect the compose or container configuration directly.

Use the installed service versions' documented commands. If safe isolation is unavailable, avoid touching the shared resource or obtain explicit user authorization first. Keep secret values out of recorded configuration and proof files.
