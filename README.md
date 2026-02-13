# Prefect V3:

## Local simple setup:
- `docker run -p 4200:4200 -d prefecthq/prefect:3-latest -- prefect server start --host 0.0.0.0`

## Lint
- `pre-commit run --all-files` as cli for coding conventions check

## Deployment

### pre-configuration
- create profile:
    - [profile.dev.toml](./profile.dev.toml)
    - [profiles.prod.toml](./profile.prod.toml) this one should be stored on server
- declare profile to be used: `export PREFECT_PROFILES_PATH=profile.dev.toml`
- `uv sync --frozen`

### deployt via [prefetc.yaml](./prefect.yaml) file:
- check which profile is used: `prefect profile ls`
- `prefect deploy --prefect-file prefect.yaml --all`



## Reference
- https://docs.prefect.io/v3/how-to-guides/
