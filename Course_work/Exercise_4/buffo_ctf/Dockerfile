# Use x86-64 Ubuntu 22.04 even on ARM hosts
FROM --platform=linux/amd64 ubuntu:22.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install build tools, debugger, and editor
RUN apt update && \
    apt install -y g++ gdb vim python3 && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Set working directory for your project
WORKDIR /work
