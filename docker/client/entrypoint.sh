#!/bin/bash

#!/bin/bash

echo "${APP_NAME^^} - Vue CONTAINER STARTING..."
echo $APP_NAME

# Display Docker Image / CI / Release details
echo "Image Build Date/Time: " "$(cat /app/build_timestamp.txt)" "UTC"

echo "-----------------------------------------------------------"
echo "APP_ENV: ${APP_ENV}"

# ====================================================================================
# Debug / Sanity check info
# ====================================================================================
echo "  "
echo "======= Current Dir / Files (Debug) ============================================================================="
pwd
ls -al

echo "  "
echo "======= Env Vars (Debug) ========================================================================================"
if [ "${APP_ENV^^}" != "PRODUCTION" ]; then
  # Only print environment vars in non-prod environments to prevent sensitive variables being sent to logging system
  printenv
fi

echo "  "
echo "======= Linux version (Debug) ==================================================================================="
cat /etc/os-release

echo "  "
echo "======= Node Path & Version (Debug) ==========================================================================="
node -v

# Check for required env vars, exit as failure if missing these critical env vars.
if [[ -z "${APP_ENV}" ]]; then
    echo "█████████████████████████████████████████████████████████████████████████████████████████████████████████████"
    echo "█ CRITICAL ERROR: Missing 'APP_ENV' environment variables."
    echo "█████████████████████████████████████████████████████████████████████████████████████████████████████████████"
    echo "APP_ENV=" $APP_ENV
    echo "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
    exit
fi

# ====================================================================================
# Install extra dependencies if ENV is LOCAL
# ====================================================================================
if [ "${APP_ENV^^}" = "DEVELOPMENT" ]; then

    # Install some extras
    echo "  "
    echo "======= Installing extra libraries just for DEVELOPMENT env ======================================================="
    yarn install --production=false
fi

# CI TEST DOWN THE TRACK

# ====================================================================================
# Run inbuilt Vue server if ENV is LOCAL
# ====================================================================================
if [ "${APP_ENV^^}" = "DEVELOPMENT" ]; then

    # Run developments
    echo "  "
    echo "======= Starting inbuilt Vue webserver ==================================================================="
    yarn dev
    exit
fi