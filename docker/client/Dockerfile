# Base image
FROM node:18-slim

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and yarn.lock to the working directory
COPY client/package.json client/yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy the entire client directory to the working directory
COPY client/ .

# Start the Vue app
CMD ["yarn", "dev"]
