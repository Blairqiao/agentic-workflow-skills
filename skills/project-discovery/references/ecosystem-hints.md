# Ecosystem hints

Starting points to check, not answers. Confirm every command in the repository before recording it in the profile.

## JavaScript and TypeScript

- Package manager from the lockfile: `package-lock.json` for npm, `pnpm-lock.yaml` for pnpm, `yarn.lock` for Yarn, `bun.lock` or `bun.lockb` for Bun.
- Frozen installs: `npm ci`; `pnpm install --frozen-lockfile`; Yarn classic `yarn install --frozen-lockfile`; Yarn 2 and later `yarn install --immutable`; `bun install --frozen-lockfile`.
- Tests: read the `scripts` section of `package.json`. Vitest and Jest can write JUnit XML through reporter options; check the installed version's docs.
- Layout: `*.test.*`, `*.spec.*`, `__tests__/`, `__snapshots__/`, setup files named in the runner config.

## Python

- Managers: `uv.lock` for uv, where `uv sync --locked` refuses an outdated lock; `poetry.lock` for Poetry; `Pipfile.lock` for Pipenv, installed with `pipenv sync`; `requirements*.txt` for pip.
- Tests: pytest writes JUnit XML with `--junitxml=<path>`. Config may sit in `pyproject.toml`, `pytest.ini`, `tox.ini` or `setup.cfg`. Shared fixtures live in `conftest.py`.
- Doctests may run through `--doctest-modules`.

## Go

- `go.mod` and `go.sum`. Tests live beside the code in `_test.go` files.
- `go test ./...`; `go test -json` gives machine-readable events, which tools such as gotestsum can turn into JUnit XML.
- `go mod download` fetches modules; `go mod verify` checks them against `go.sum`.

## Rust

- `Cargo.lock`; `cargo build --locked` and `cargo test --locked` refuse to update the lockfile.
- Unit tests usually sit inside source files in a `#[cfg(test)]` module. Integration tests live in `tests/`. Doctests live in doc comments.
- cargo-nextest writes JUnit XML through a profile in `.config/nextest.toml`, but it does not run doctests, so run `cargo test --doc` as well.

## JVM

- Maven: `mvn -B verify`, with Surefire reports under `target/surefire-reports/`.
- Gradle: `./gradlew test`, with results under `build/test-results/`.
- Tests usually live under `src/test/`.

## Ruby

- `Gemfile.lock`; install with Bundler's frozen setting on, such as `BUNDLE_FROZEN=true`.
- RSpec needs a formatter gem such as `rspec_junit_formatter` for JUnit XML.

## .NET

- `packages.lock.json` when lock files are enabled; `dotnet restore --locked-mode`.
- `dotnet test --logger trx` writes TRX results; JUnit XML needs an extra logger package.

## Environment files

- Usually committed templates: `.env.example`, `.env.sample`, `.env.template`, `config/*.example.*`.
- Usually local-only: `.env`, `.env.local`, `.env.*.local`, `*.secrets.*`, credential JSON files.
