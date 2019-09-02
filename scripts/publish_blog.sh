#!/bin/bash
set -ev

SCRIPT_DIR=`dirname "$0"`
BLOG_DIR=SCRIPT_DIR/..
SITE_DIR=BLOG_DIR/site
PUB_DIR=`mktemp -d`

pushd $SITE_DIR
JEKYLL_ENV=production jekyll build -d $PUB_DIR
popd

pushd $BLOG_DIR
git checkout gh-pages
cp -R $PUB_DIR/* .
git add .
git commit -a -m "Update blog"
git push origin gh-pages
git checkout master
popd

rm -Rf $PUB_DIR
