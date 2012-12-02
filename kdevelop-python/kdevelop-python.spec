Name:       kdevelop-python 
Version:    1.4.1 
Release:    1%{?dist}
License:    GPLv2
Source0:    http://download.kde.org/stable/kdevelop/kdev-python/1.4.1/src/kdev-python-v1.4.1.tar.bz2 
Patch0:     kdevelop-python-documentation-files.patch 

Summary:    Python Plugin for KDevelop 
URL:        http://kdevelop.org

BuildRequires:  kdevplatform-devel
BuildRequires:  kdevelop-devel 
BuildRequires:  kdevelop-pg-qt-devel
BuildRequires:  cmake >= 2.6

%description

%prep
%setup -qn kdev-python-v%{version}
%patch0

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform} 

%install
make install/fast DESTDIR=${RPM_BUILD_ROOT} -C %{_target_platform}

%files
%doc DESIGN TODO README TODO 
%{_kde4_libdir}/kde4/kdevpythonlanguagesupport.so
%{_kde4_libdir}/libkdev4pythonduchain.so
%{_kde4_libdir}/kde4/kdevpdb.so
%{_kde4_datadir}/kde4/apps/kdevappwizard/templates/*
%{_kde4_libdir}/libpython2.7-kdevelop.so
%{_kde4_libdir}/libpython2.7-kdevelop.so.1.0
%{_kde4_libdir}/libkdev4pythonparser.so
%{_kde4_libdir}/libkdev4pythoncompletion.so
%{_kde4_datadir}/kde4/services/kdevpdb.desktop
%{_kde4_datadir}/kde4/services/kdevpythonsupport.desktop 
%{_kde4_datadir}/kde4/apps/kdevpythonsupport

%changelog
* Sun Dec 01 2012 Minh Ngo <minh@fedoraproject.org> 1.4.1-1
- initial build
