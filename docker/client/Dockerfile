# Base image
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and yarn.lock to the working directory
COPY client/package.json client/yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy the entire client directory to the working directory
COPY client/ .

# Build the Vue app
RUN yarn build

# Expose the default port for the Vue app
# EXPOSE 8082

# Start the Vue app
CMD ["yarn", "dev"]
