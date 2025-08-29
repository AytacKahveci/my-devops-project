FROM jenkins/jenkins:lts-jdk17

# Switch to the root user to install tools, then switch back to jenkins user
USER root

# Install a set of dependencies to make sure subsequent installations go smoothly
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    software-properties-common \
    git \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Docker CLI using a more reliable method
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install the Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli

# Download the latest kubectl binary
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

RUN chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

RUN apt-get install -y ansible
