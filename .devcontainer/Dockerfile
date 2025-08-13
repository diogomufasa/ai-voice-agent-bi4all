# Arguments
ARG PYTHON_VER="3.10"
FROM python:$PYTHON_VER
ARG ENV_NAME="ai-voice-agent-bi4all"
ARG PROJECT_NAME="ai-voice-agent-bi4all"

# Environment variables
ENV ENV_NAME=$ENV_NAME
ENV PYTHON_VER=$PYTHON_VER
ENV PROJECT_NAME=$PROJECT_NAME

# Set working directory
WORKDIR /workspace

# Copy install script from current directory
COPY install_dependencies.sh ./
RUN chmod +x install_dependencies.sh

# Install system dependencies
RUN ./install_dependencies.sh

# Create virtual environment
RUN python3 -m venv /workspace/.venv && \
    /workspace/.venv/bin/pip install --upgrade pip

# Set the virtual environment as default
ENV PATH="/workspace/.venv/bin:$PATH"
