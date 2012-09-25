#!/usr/bin/env sh
wget $(cat qxmpp.spec | grep Source0 | awk '{print $2}')
mkdir -p ~/rpmbuild/SOURCES
mv qxmpp-*.tar.gz ~/rpmbuild/SOURCES
cp *.patch ~/rpmbuild/SOURCES
rpmbuild -ba --clean qxmpp.spec
