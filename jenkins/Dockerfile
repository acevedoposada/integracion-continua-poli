FROM jenkins/jenkins:lts-jdk21
USER root
# Cliente Docker y Docker Compose (binarios oficiales)
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/docker
COPY --from=docker:cli /usr/local/libexec/docker/cli-plugins /usr/local/libexec/docker/cli-plugins
USER jenkins
RUN jenkins-plugin-cli --plugins git github github-branch-source workflow-aggregator \
    pipeline-graph-view docker-workflow credentials-binding junit matrix-auth
