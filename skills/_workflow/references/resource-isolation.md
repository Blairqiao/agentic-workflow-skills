# Resource isolation

Read when the change needs local services or shared resources. Record every allocation and verify its identity before modifying or removing it. Cleanup requires authorization and must match recorded resources.

| Resource | Isolation |
| --- | --- |
| Ports | Record free ports and pass them through local configuration |
| SQL | Dedicated database or instance; verify migration targets |
| SQLite | Database file inside the task's allocated directory |
| Cache | Dedicated instance/database, or a scoped key prefix |
| Queues/workers | Unique queue/topic names; no consumption from shared queues |
| Containers | Unique project identity, volumes, and published ports |
| Object storage | Dedicated non-production bucket or emulator namespace |
| Files | Allocated directories for uploads, temporary data, and generated output |
| Email/webhooks | Local sinks or authorized test endpoints |

A key prefix is not a dedicated cache database: never flush a shared database to clean up prefixed keys. Container project names alone do not isolate explicitly shared volumes or external services. Inspect the actual configuration.

Use the installed service versions' documented commands. If safe isolation is unavailable, avoid the shared resource or obtain authorization before affecting it. Keep secret values out of recorded configuration and proof.
