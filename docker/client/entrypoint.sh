#!/bin/bash

# Check if the node_modules directory exists
if [ ! -d "node_modules" ]; then
  echo "Node modules not found. Running 'yarn install'..."
  yarn install --frozen-lockfile
fi

# Start the Vue app
yarn serve
