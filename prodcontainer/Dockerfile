# base image
FROM continuumio/miniconda3:4.5.11

# Create new directory and setup workspace
RUN mkdir /workspace
WORKDIR /workspace

# load in the environment.yml file
COPY prodcontainer/environment.yml /
COPY mda_reports /workspace/

ENV SSH_AUTH_SOCK=/tmp/.ssh-auth-sock
LABEL com.ensody.ssh-agent-inject=

# Install git, process tools
RUN apt-get update \
    && apt-get -y install git procps

# create the environment
RUN conda update -n base conda -y && conda env update