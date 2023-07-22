FROM node:18-slim as development-stage

# SET WORKING DIRECTORY
WORKDIR /app

# Copy runtime script & make it executable
COPY /docker/client/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./client/package.json ./client/yarn.lock ./

# Install ALL Dependencies
RUN yarn install

# Copy Application code into a directory called `app`
COPY ./client /app

# ========================================
# ---- Executed at Container Runtime ----
# ========================================

# CMD commands get executed at container runtime!
CMD ["/entrypoint.sh"]

# TODO: Production 