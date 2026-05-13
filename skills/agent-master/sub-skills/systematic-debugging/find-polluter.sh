#!/usr/bin/env bash

# find-polluter.sh
# Usage: ./find-polluter.sh <marker_file> <test_glob>
# Example: ./find-polluter.sh '.git' 'src/**/*.test.ts'

MARKER=$1
TEST_GLOB=$2

if [ -z "$MARKER" ] || [ -z "$TEST_GLOB" ]; then
  echo "Usage: $0 <marker_file> <test_glob>"
  exit 1
fi

echo "Searching for tests that create $MARKER..."

# Get list of all test files
TEST_FILES=$(find . -name "$TEST_GLOB")
COUNT=0

for FILE in $TEST_FILES; do
  COUNT=$((COUNT + 1))
  echo "[$COUNT] Running: $FILE"
  
  # Run the specific test
  # Adjust the test command (npm test, jest, etc.) as needed
  npx jest "$FILE" --runInBand > /dev/null 2>&1
  
  # Check if marker was created
  if [ -e "$MARKER" ] || [ -d "$MARKER" ]; then
    echo ""
    echo "🚨 POLLUTER FOUND: $FILE"
    echo "This test created $MARKER and did not clean it up."
    
    # Optional: cleanup and exit or keep going
    rm -rf "$MARKER"
    exit 0
  fi
done

echo ""
echo "✅ No polluters found in $COUNT files."
