Name:       spacefm 
Version:    0.8.4
Release:    1%{?dist}
License:    GPLv3 and LGPLv3
Source0:    http://downloads.sourceforge.net/spacefm/spacefm-0.8.4.tar.xz

Summary:    Space FM File Manager 
URL:        http://ignorantguru.github.com/spacefm/  

BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libudev-devel
BuildRequires:  desktop-file-utils
BuildRequires:  startup-notification-devel 

%description
SpaceFM is a multiple panel tabbed file manager for Linux with built-in VFS,
udev-based device manager, customizable menu system, and bash integration. 

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%find_lang %{name}

%check
desktop-file-validate ${RPM_BUILD_ROOT}/%{_datadir}/applications/spacefm-find.desktop
desktop-file-validate ${RPM_BUILD_ROOT}/%{_datadir}/applications/spacefm-folder-handler.desktop
desktop-file-validate ${RPM_BUILD_ROOT}/%{_datadir}/applications/spacefm.desktop

%post
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%files -f %{name}.lang
%doc COPYING COPYING-LGPL AUTHORS README TRANSLATE 
%{_bindir}/spacefm
%{_bindir}/spacefm-auth
%{_datadir}/applications/spacefm-find.desktop
%{_datadir}/applications/spacefm-folder-handler.desktop
%{_datadir}/applications/spacefm.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/Faenza/apps/48/*
%doc %{_datadir}/doc/spacefm
%{_datadir}/mime/packages/spacefm-mime.xml
%{_datadir}/spacefm

%changelog
* Tue Jan 14 2013 Minh Ngo <minh@fedoraproject.org> 0.8.4-1
- New version

* Thu Nov 22 2012 Minh Ngo <minh@fedoraproject.org> 0.8.2-4
- Removing INSTALL and NEWS files

* Sun Nov 04 2012 Minh Ngo <minh@fedoraproject.org> 0.8.2-3
- fixing licenses
- updating dependencies

* Sun Nov 04 2012 Minh Ngo <minh@fedoraproject.org> 0.8.2-2
- validate desktop files
- adding some scriptlets for mime files

* Sun Nov 04 2012 Minh Ngo <minh@fedoraproject.org> 0.8.2-1
- initial build
