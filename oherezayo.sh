#!/bin/bash

# Prompt for the commit message
read -p "Enter commit message: " commit_message

if [ -z "$commit_message" ]; then
    echo "Error: Commit message cannot be empty."
    exit 1
fi

# Check if a filename argument is provided
if [ "$#" -eq 1 ]; then
    # Add the specified file
    if ! git add "$1" 2>/dev/null; then
        echo "Error: Failed to add file. Check if the file path is correct."
        exit 1
    fi
else
    # Add all changes
    git add .
fi

echo ""
echo "1. Committing ----------------------------------------------------------"
# Commit with the provided message
if ! git commit -m "$commit_message"; then
    echo "Error: Commit failed. Check for untracked files or other issues."
    exit 1
fi

echo ""
echo "2. Pulling ----------------------------------------------------------"
# Pull the latest changes from the remote repository
branch=$(git rev-parse --abbrev-ref HEAD)
if ! git rev-parse --abbrev-ref @{u} >/dev/null 2>&1; then
    echo "No upstream branch set for $branch. Please set it with:"
    echo "git branch --set-upstream-to=origin/$branch $branch"
    exit 1
fi
if ! git pull origin --no-rebase $branch; then
    echo "Error: Pull failed. Resolve conflicts and try again."
    exit 1
fi

echo ""
echo "3. Pushing ----------------------------------------------------------"
# Push to the current branch
if ! git push origin $branch; then
    echo "Error: Push failed. Check your remote repository or network connection."
    exit 1
fi

echo "Success: Changes have been committed, pulled, and pushed."

