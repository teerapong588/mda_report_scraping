# base image
FROM continuumio/miniconda3:4.5.11

# load in the environment.yml file
COPY .devcontainer/environment.yml /

# Copy default endpoint specific user settings overrides into container to specify Python path
COPY .devcontainer/settings.vscode.json /root/.vscode-server-insiders/data/Machine/settings.json

ENV SSH_AUTH_SOCK=/tmp/.ssh-auth-sock
LABEL com.ensody.ssh-agent-inject=

# Install git, process tools
RUN apt-get update \
    && apt-get -y install git procps

# create the environment
RUN conda update -n base conda -y && conda env update