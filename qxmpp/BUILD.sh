#!/usr/bin/env sh
wget http://qxmpp.googlecode.com/files/qxmpp-0.7.3.tar.gz
mkdir -p ~/rpmbuild/SOURCES
mv qxmpp-0.7.3.tar.gz ~/rpmbuild/SOURCES
cp *.patch ~/rpmbuild/SOURCES
rpmbuild -ba --clean qxmpp.spec
