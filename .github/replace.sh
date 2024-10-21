#!/bin/bash

# Generate the table of contents
toc=$(python .github/toc.py)

toc_index=$(CUR_DIR=docs python .github/toc.py)

# Update README.md
sed '/{{table_of_contents}}/r /dev/stdin' .github/README.md.template < <(echo "$toc") | sed '/{{table_of_contents}}/d' > README.md

# Update docs/index.md
sed '/{{table_of_contents}}/r /dev/stdin' .github/index.md.template < <(echo "$toc_index") | sed '/{{table_of_contents}}/d' > docs/index.md

echo "Table of contents updated in README.md and docs/index.md"