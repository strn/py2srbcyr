#!/bin/sh

git_add_push() {
    git add .
    git commit -m "$1"
    git push
}

if [ $# -ne 2 ]; then
    echo "ERROR: Program requires exactly 2 parameters:" >&2
    echo "ERROR: Git commit message and Sigil plugin version" >&2
fi

# Commit to py2srbcyr repository 
git_add_push "$1"

# Update epg2cyr
cd ../gedit-lat2cyr
cp ../py2srbcyr/__init__.py serbcyr.py
git_add_push "py2srbcyr upgrade: $1"
cd -

# Update sigil-lat2cyr
cd ../sigil-lat2cyr
cp ../py2srbcyr/__init__.py lib/py2srbcyr.py
git_add_push "py2srbcyr upgrade: $1"
[ -x ./make-sigil-plugin.sh ] && ./make-sigil-plugin.sh "$2"
cd -
