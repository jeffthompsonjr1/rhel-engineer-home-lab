#!/usr/bin/env bash
set -euo pipefail

TARGET_HOST="centos_servera"
TARGET_USER="testuser1"

if ! command -v ansible >/dev/null 2>&1; then
    echo "ERROR: ansible command not found."
    exit 1
fi

if [[ ! -f "./ansible.cfg" || ! -f "./inventory" ]]; then
    echo "ERROR: Run this script from the rhel-engineer-home-lab project root."
    exit 1
fi

if ! ansible-inventory --host "${TARGET_HOST}" >/dev/null 2>&1; then
    echo "ERROR: ${TARGET_HOST} is not present in the current inventory."
    exit 1
fi

ansible "${TARGET_HOST}" -b -m ansible.builtin.user     -a "name=${TARGET_USER} shell=/sbin/nologin" >/dev/null

echo "Break/fix lab staged successfully."
echo "Scenario: ${TARGET_USER} on ${TARGET_HOST} can no longer obtain a normal interactive login."
echo "Do not inspect this script until after you have diagnosed and repaired the problem."

