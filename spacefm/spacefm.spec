Name:       spacefm 
Version:    0.8.2
Release:    1%{?dist}
License:    GPLv3 or LGPLv3
Source0:    http://downloads.sourceforge.net/spacefm/spacefm-0.8.2.tar.xz

Summary:    Space FM File Manager 
URL:        http://ignorantguru.github.com/spacefm/  

BuildRequires:  xz
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  libudev-devel

%description
SpaceFM is a multi-panel tabbed file manager for Linux with built-in VFS,
udev-based device manager, customizable menu system, and bash integration. 

%prep
%setup -qn %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING COPYING-LGPL AUTHORS INSTALL README NEWS TRANSLATE 
%{_bindir}/spacefm
%{_bindir}/spacefm-auth
%{_datadir}/applications/spacefm-find.desktop
%{_datadir}/applications/spacefm-folder-handler.desktop
%{_datadir}/applications/spacefm.desktop
%doc %{_datadir}/doc/spacefm
%{_datadir}/mime/packages/spacefm-mime.xml
%{_datadir}/pixmaps/spacefm*
%{_datadir}/spacefm

%changelog
* Sun Nov 04 2012 Minh Ngo <minh@fedorapeople.org> 0.8.2-1
- initial build
