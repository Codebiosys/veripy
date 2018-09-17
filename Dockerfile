#
# Dockerfile for testing Veri-Py service
#

# Use minimal platform for just the Node runtime
FROM python:3.7 AS base

# Declare application root for easier copying of files
WORKDIR /app

# Copy version specs first so they can be cached by Docker
COPY requirements.txt .
RUN pip install -r requirements.txt


#
# Development multi-stage target
#
FROM base AS development

# Additional dependencies must be installed before copying source
COPY requirements-development.txt .
RUN pip install -r requirements-development.txt

# Copy source code last so it can be mounted in Compose
COPY . .
RUN pip install -e .


#
# Production multi-stage target
#
FROM base AS production

# Copy source code last so it can be mounted in Compose
COPY . .
RUN pip install .

# Default command to get the application up and running
