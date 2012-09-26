Name:       kchildlock
Version:    0.90.4.2
Release:    1%{?dist}
License:    GPLv2
Source0:    http://garr.dl.sourceforge.net/project/kchildlock/kchildlock/0.90.4.2/kchildlock-0.90.4.2.tar.gz 

Group:      Applications/System 
Summary:    KDE Parental Control Application 
URL:        http://sourceforge.net/projects/kchildlock/ 

BuildRequires:  kdelibs-devel
BuildRequires:  cmake >= 2.6

%description
kchildlock is a tool to monitor and restrict the time a children spends on the
computer. The limits can be specified per day of the week, by lower and upper
hour limits, maximum daily usage time, and maximum weekly usage time. The same
restriction limits can be applied to applications based on the user login. It
requires the KDE4 Desktop.

%prep
%setup -qn %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform} 

%install
make install/fast DESTDIR=${RPM_BUILD_ROOT} -C %{_target_platform}

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING INSTALL README TODO ChangeLog 
%{_kde4_libdir}/kde4/*
%{_kde4_configdir}/kchildlockrc
%doc %{_kde4_docdir}/*
%{_kde4_iconsdir}/*
%{_datadir}/kde4/services/*
%{_localstatedir}/opt/%{name}/*

%changelog
* Wed Sep 26 2012 Minh Ngo <nlminhtl@gmail.com> 0.90.4.2-1
- initial build 
