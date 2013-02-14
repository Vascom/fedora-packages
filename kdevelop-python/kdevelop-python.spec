Name:       kdevelop-python 
Version:    1.4.1 
Release:    2%{?dist}
License:    GPLv2
Source0:    http://download.kde.org/stable/kdevelop/kdev-python/1.4.1/src/kdev-python-v1.4.1.tar.bz2 
Patch0:     kdevelop-python-documentation-files.patch 

Summary:    Python Plugin for KDevelop 
URL:        http://kdevelop.org

BuildRequires:  kdevplatform-devel
BuildRequires:  kdevelop-devel 
BuildRequires:  kdevelop-pg-qt-devel
BuildRequires:  python2-devel

%description
Python language support for KDevelop Integrated Development
Environment.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc DESIGN TODO README TODO 
%{_kde4_libdir}/kde4/kdevpythonlanguagesupport.so
%{_kde4_libdir}/libkdev4pythonduchain.so
%{_kde4_libdir}/kde4/kdevpdb.so
%{_kde4_appsdir}/kdevappwizard/templates/*
%{_kde4_libdir}/libpython%{python_version}-kdevelop.so
%{_kde4_libdir}/libpython%{python_version}-kdevelop.so.1.0
%{_kde4_libdir}/libkdev4pythonparser.so
%{_kde4_libdir}/libkdev4pythoncompletion.so
%{_kde4_datadir}/kde4/services/kdevpdb.desktop
%{_kde4_datadir}/kde4/services/kdevpythonsupport.desktop 
%{_kde4_appsdir}/kdevpythonsupport

%changelog
* Thu Feb 14 2013 Minh Ngo <minh@fedoraproject.org> 1.4.1-2
- have added _kde4_appsdir macro
- have dropped updata-mime-database scriptlets
- have omitted cmake requirement
- have removed desktop-file-install script
- removing python2.7 hardcode

* Sun Dec 01 2012 Minh Ngo <minh@fedoraproject.org> 1.4.1-1
- initial buildOB
