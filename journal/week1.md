# Week 1 — App Containerization

## Required Homework

### Learn more about Containerising local development environments.

This can be verified using following files

[Backend - Docker](../backend-flask/Dockerfile)
[Frontend - Docker](../frontend-react-js/Dockerfile)
[Docker compose](../docker-compose.yml)

### Containerise backend and frontend and add more features.

- Explored codebase and solved lint errors, here are few example of lint fixes

![Lint fixes # 1](assets/week1/lint-1.png)

![Lint fixes # 2](assets/week1/lint-2.png)

![Lint fixes # 3](assets/week1/lint-3.png)

- Added Notification endpoint and used it the React SPA.

![Crudder in local (gitpod) environment](assets/week1/working-crudder-after-lint.png)

### Setup docker compose to add local Dynamo DB and Postgres DB.

This can be verified using following files

[Docker compose](../docker-compose.yml)

### Learn about other CDEs like Git workspaces and AWS Cloud9.


## Optional home work

### Moved python installation to a bash script.

- This makes the installation and other bootstrap commands more maintainable and readable. 
- Here is the link to bash script

[init.sh](../backend-flask/init.sh)

### Added docker health-check for backend python api.

- Added health API endpoint (GET: /api/health) to be used for docker health check.
- These health checks can later be used in a dashboard indicating all unhealthy endpoint and potentially auto healing mrechanisms. 

![Health test endpoint](assets/week1/health-test.png)

![Sample unhealthy instance](assets/week1/unhealthy-backend-image.png)

### Moved Postgres database username and password to Gitpod environment variables.

- Moved Postgres username and password to environment variables so that they are secure and are not available in GIT.
- Secrets can later be moved to AWS Parameter store or Secrets manager.

![Gitpod environment variables](assets/week1/gitpod-env-variables.png)

