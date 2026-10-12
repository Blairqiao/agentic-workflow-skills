# Resource isolation notes

Engine-specific details for `worktree-setup`. Check the versions the project actually uses.

## PostgreSQL

- Create with `CREATE DATABASE "<name>";` while connected to a maintenance database such as `postgres`.
- `DROP DATABASE IF EXISTS "<name>";` fails while other sessions are connected. PostgreSQL 13 and later accept `WITH (FORCE)` to end those sessions first.
- Point migrations at the new database through the workspace's config, and confirm the database name in the connection string before running them.

## MySQL and MariaDB

- `CREATE DATABASE` and `DROP DATABASE IF EXISTS`, with the name quoted in backticks.

## SQLite

- Keep the database file inside the workspace. Teardown is deleting that file.

## Redis and compatible caches

- Use a separate logical database index where available, or a key prefix. Redis Cluster supports only database 0, so use a prefix there.
- Teardown runs `FLUSHDB` against that index only. Never run `FLUSHALL`.

## Docker Compose

- Use a per-workspace project name, `docker compose -p <project>_wt_<id> ...`, so containers, networks and volumes stay separate.
- Teardown runs `docker compose -p <name> down -v`, which removes only that project's containers and volumes.
- Remap published ports through env variables or an override file so two workspaces don't collide.

## Ports

- Pick a free port by checking what is already listening, record it, and pass it through config instead of relying on defaults.

## Message queues

- Prefix queue, topic or stream names with the workspace ID, and don't run consumers against shared queues.

## Object storage and emulators

- Use a workspace-specific bucket, or a local emulator instance with its own data directory.
