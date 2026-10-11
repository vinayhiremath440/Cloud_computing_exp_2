# syntax=docker/dockerfile:1
# ==============================================================================
# Cloud Computing Laboratory - Experiment 2
# Dockerfile: Sysbench Memory & Micro-Benchmarking Suite
# Base OS: Ubuntu 24.04 LTS (Noble Numbat)
# ==============================================================================

FROM ubuntu:24.04

LABEL maintainer="Cloud Computing Lab Student"
LABEL version="1.1.0"
LABEL description="Optimized containerized benchmark image featuring Sysbench, FIO, iPerf3, and system telemetry tools"

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update system repositories and install required benchmark suites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        sysbench \
        fio \
        iperf3 \
        python3 \
        python3-pip \
        procps \
        sysstat \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establish benchmarking workspace
WORKDIR /workspace/benchmark

# Health verification / default container entrypoint
CMD ["sysbench", "--version"]
