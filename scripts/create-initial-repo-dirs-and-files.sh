#!/bin/bash
COLUMN_LENGTH=60

DIRECTORIES=(
  ansible/playbooks
  ansible/roles
  docker
  packer
  terraform
  vagrant/base
)

EXIT_STATUS=0

FILES=(
  .gitignore
  LICENSE.md
  README.md
)

FG_DEFAULT=39
FG_GREEN=32
FG_RED=31

SET_COLOR_DEFAULT="\e[${FG_DEFAULT}m"
SET_COLOR_GREEN="\e[${FG_GREEN}m"
SET_COLOR_RED="\e[${FG_RED}m"

function echo_OK {
  echo -en "[  $SET_COLOR_GREEN"
  echo -n "OK"
  echo -en "$SET_COLOR_DEFAULT  ]"
}

function echo_FAILED {
  echo -en "[$SET_COLOR_RED"
  echo -n "FAILED"
  echo -en "$SET_COLOR_DEFAULT]"
}

function echo_usage {
  echo -e "Usage: $0 [\e[3mpath\e[0m]"
  echo "Creates a set of initial directories and files for a Git repository."
}

if [ "$1" = "--help" ]; then
  echo_usage
  EXIT_STATUS=1
else
  for i in "${DIRECTORIES[@]}"; do
    { \
    mkdir -p "${1:-.}/$i" && \
    printf "%-${COLUMN_LENGTH}s" "Creating the '$i' directory" && \
    echo_OK; } || { \
    echo_FAILED; \
    EXIT_STATUS=1; }
    echo
  done

  for i in "${FILES[@]}"; do
    { \
    touch -a "${1:-.}/$i" && \
    printf "%-${COLUMN_LENGTH}s" "Creating the '$i' file" && \
    echo_OK; } || { \
    echo_FAILED; \
    EXIT_STATUS=1; }
    echo
  done
fi

exit $EXIT_STATUS
