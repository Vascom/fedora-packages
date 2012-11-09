#!/usr/bin/env sh
wget $(cat chicken.spec | grep Source0 | awk '{print $2}')
mkdir -p ~/rpmbuild/SOURCES
mv chicken-*.tar.gz ~/rpmbuild/SOURCES
rpmbuild -ba --clean chicken.spec
