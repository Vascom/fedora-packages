Name:           kfaenza-icon-theme
Version:        0.8.9
Release:        3%{?dist}
Summary:        Faenza-Cupertino Icon Theme for KDE

Group:          User Interface/Desktops 
License:        GPLv3
URL:            http://kde-look.org/content/show.php?content=143890
Source0:        http://ompldr.org/vYjR0NQ/kfaenza-icon-theme-0.8.9.tar.gz
BuildArch:      noarch

Patch0:         index.patch

BuildRequires:  gtk2 >= 2.6.0

%description
Contains icons for Faenza-Cupertino theme for KDE.

%prep
%setup -qn KFaenza
%patch0

%install
rm INSTALL
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/icons/KFaenza
rm $(find . -name ".directory" |xargs)
cp -r . ${RPM_BUILD_ROOT}%{_datadir}/icons/KFaenza

%post
touch --no-create %{_datadir}/icons/KFaenza &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/KFaenza &>/dev/null
  gtk-update-icon-cache -f %{_datadir}/icons/KFaenza &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache -f %{_datadir}/icons/KFaenza &>/dev/null || :

%files
%{_datadir}/icons/KFaenza

%changelog
* Wed Sep 26 2012 Minh Ngo <nlminhtl@gmail.com> - 0.8.9-3
- Removing hidden files.

* Sun Jul 01 2012 Minh Ngo <ignotusp@fedoraproject.org> - 0.8.9-2
- Fixing inherited icon theme
- Updating icon cache

* Sat Jun 16 2012 Minh Ngo <nlminhtl@gmail.com> - 0.8.9-1
- Intial RPM release
