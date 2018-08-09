#
# Dockerfile for testing Veri-Py service
#

# Use minimal platform for just the Node runtime
FROM python:3.7

# Declare application root for easier copying of files
WORKDIR /app

# Copy version specs first so they can be cached by Docker
COPY dev-requirements.txt requirements.txt ./
RUN pip install -r dev-requirements.txt

# Copy source code last so it can be mounted in Compose
COPY . .

# Default command to get the application up and running
# CMD ["behave", "veripy/features"]
