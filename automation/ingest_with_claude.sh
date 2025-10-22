#!/bin/bash
# Interactive script to ingest content using Claude Code (no API key required!)
# Uses your existing Claude Code subscription

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   Ignition Best Practices - Content Ingestion Helper      ║${NC}"
echo -e "${BLUE}║   Using Claude Code (No API Key Required!)                ║${NC}"
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo ""

# Check if URL was provided as argument
if [ -n "$1" ]; then
    URL="$1"
else
    # Prompt for URL
    echo -e "${YELLOW}Enter the URL to ingest:${NC}"
    read -r URL
fi

echo ""
echo -e "${GREEN}URL to process:${NC} $URL"
echo ""

# Check if Claude Code is available
if ! command -v claude &> /dev/null; then
    echo -e "${YELLOW}Warning: 'claude' command not found.${NC}"
    echo "Please make sure Claude Code is installed and in your PATH."
    echo ""
    echo "Continuing with manual instructions..."
    echo ""
fi

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Next Steps:${NC}"
echo ""
echo "1. Run Claude Code in this repository:"
echo -e "   ${YELLOW}claude${NC}"
echo ""
echo "2. Simply ask Claude to ingest the URL:"
echo -e "   ${YELLOW}Ingest this URL: $URL${NC}"
echo ""
echo "3. Claude will automatically:"
echo "   - Use the content-ingest skill"
echo "   - Fetch and analyze the content"
echo "   - Update section files"
echo "   - Show you what was added"
echo ""
echo ""
echo "4. Review the changes:"
echo -e "   ${YELLOW}git diff${NC}"
echo ""
echo "5. If you're happy, commit:"
echo -e "   ${YELLOW}git add sections/ && git commit -m 'Add content from URL'${NC}"
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}Tip:${NC} The URL has been copied to your clipboard (if available)"

# Try to copy to clipboard (works on macOS and Linux with xclip)
if command -v pbcopy &> /dev/null; then
    echo "$URL" | pbcopy
    echo -e "${GREEN}✓ URL copied to clipboard (macOS)${NC}"
elif command -v xclip &> /dev/null; then
    echo "$URL" | xclip -selection clipboard
    echo -e "${GREEN}✓ URL copied to clipboard (Linux)${NC}"
elif command -v clip.exe &> /dev/null; then
    echo "$URL" | clip.exe
    echo -e "${GREEN}✓ URL copied to clipboard (WSL)${NC}"
fi

echo ""
echo -e "${YELLOW}Ready to start? Just run: claude${NC}"
echo ""
