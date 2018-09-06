# Developer: Jeury Mejia
# Parameters:
# 1. Version Name (optional)
# Execution Example: ./project-id-prod.sh dev-version
#
# - If parameter is passed: A new version with name (parameter) will be created and version will not be promoted.
# - If parameter is missing: A new version with name (date and time) will be created and version will be promoted
#   - Only do this, whenever you want to promote the version.

gcloud config configurations activate project-id

if [ -z "$1" ]
then
    gcloud app deploy -v `date +%Y-%m-%d`
else
    gcloud app deploy -v $1 --no-promote
fi
