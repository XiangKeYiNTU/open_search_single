#!/bin/bash

# test.sh: Test setup script for search-qa project

# Exit immediately if a command exits with a non-zero status
set -e

QUESTION=${1:-}
IMAGE_PATH=${2:-}

# Prompt if arguments were not given
if [ -z "$QUESTION" ]; then
  read -p "Enter your question: " QUESTION
fi

if [ -z "$IMAGE_PATH" ]; then
  read -p "Enter public image URL (or press Enter to skip): " IMAGE_PATH
fi

# ========== STEP 6: Run the Workflow ==========
echo "[*] Running question: $QUESTION"
if [ -n "$IMAGE_PATH" ]; then
  echo "[*] With image: $IMAGE_PATH"
  python workflow.py "$QUESTION" "$IMAGE_PATH"
else
  python workflow.py "$QUESTION"
fi

echo "[✓] Workflow completed."