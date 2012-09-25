#!/usr/bin/env sh
wget $(cat kfaenza-icon-theme.spec | grep Source0 | awk '{print $2}')
mkdir -p ~/rpmbuild/SOURCES
mv kfaenza-icon-theme-*.tar.gz ~/rpmbuild/SOURCES
cp *.patch ~/rpmbuild/SOURCES
rpmbuild -ba --clean kfaenza-icon-theme.spec
