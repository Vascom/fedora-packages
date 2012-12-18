#!/usr/bin/env sh
wget $(cat tex-pscyr.spec | grep "Source0:" | awk '{print $2}')
wget $(cat tex-pscyr.spec | grep "Source1:" | awk '{print $2}')
mkdir -p ~/rpmbuild/SOURCES
mv *.tar.gz ~/rpmbuild/SOURCES
rpmbuild -ba --clean tex-pscyr.spec
