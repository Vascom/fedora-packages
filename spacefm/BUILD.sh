#!/usr/bin/env sh
wget $(cat spacefm.spec | grep Source0 | awk '{print $2}')
mkdir -p ~/rpmbuild/SOURCES
mv spacefm-*.tar.xz ~/rpmbuild/SOURCES
rpmbuild -ba --clean spacefm.spec
