#!/usr/bin/env sh
wget $(cat kchildlock.spec | grep Source0 | awk '{print $2}')
mkdir -p ~/rpmbuild/SOURCES
mv kchildlock-*.tar.gz ~/rpmbuild/SOURCES
cp *.patch ~/rpmbuild/SOURCES
rpmbuild -ba --clean kchildlock.spec
