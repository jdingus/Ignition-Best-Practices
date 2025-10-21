#!/bin/bash
# Example batch processing script
# This shows how to process multiple URLs at once

# Example URLs (replace with actual Ignition-related content)
urls=(
    "https://inductiveautomation.com/blog/example1"
    "https://inductiveautomation.com/blog/example2"
    "https://inductiveautomation.com/blog/example3"
)

echo "Starting batch ingestion..."
echo "================================"

for url in "${urls[@]}"; do
    echo ""
    echo "Processing: $url"
    echo "--------------------------------"

    # Run with dry-run first to preview
    python ingest_content.py --dry-run "$url"

    # Uncomment the line below to actually process (remove dry-run)
    # python ingest_content.py "$url"

    # Add delay to respect rate limits
    sleep 2
done

echo ""
echo "================================"
echo "Batch processing complete!"
echo ""
echo "Review changes with: git diff"
echo "Commit changes with: git add . && git commit -m 'Add ingested content'"
