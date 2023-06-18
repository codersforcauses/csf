FROM node:18-slim as development-stage

# SET WORKING DIRECTORY
WORKDIR /app

# Copy runtime script & make it executable
COPY /docker/client/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy Application code into a directory called `app`
COPY ./client /app

# Install ALL Dependencies
RUN yarn install

# ========================================
# ---- Executed at Container Runtime ----
# ========================================

# CMD commands get executed at container runtime!
CMD ["/entrypoint.sh"]

# TODO: Production 