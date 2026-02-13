## prefect V3:
- need to config profileu for different environments
- need to declare prefect server arl for each profile
- can separate profile for each kind of environment like dev, staging, prod
- user env to switch between profiles:
    ```bash
    export PREFECT_PROFILE=profile.dev.toml
    ``` 


## Deployment

### pre-configuration
- create profile: 
    - [profile.dev.toml](./profile.dev.toml)
    - [profiles.prod.toml](./profile.prod.toml) this one should be stored on server
- declare profile to be used: `export PREFECT_PROFILES_PATH=profile.dev.toml`
### via [prefetc.yaml](./prefect.yaml) file:
- check which profile is used: `prefect profile ls`
- `prefect deploy --prefect-file prefect.yaml --all`
