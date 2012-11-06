#!/usr/bin/env sh
wget $(cat skb.spec | grep Source0 | awk '{print $2}')
mkdir -p ~/rpmbuild/SOURCES
mv skb-*.tar.gz ~/rpmbuild/SOURCES
rpmbuild -ba --clean skb.spec
