%global _missing_build_ids_terminate_build 0
Name:       chicken 
Version:    4.7.0.6
Release:    3%{?dist}
License:    GPLv2 and BSD and MIT
Source0:    http://code.call-cc.org/stability/4.7.0/chicken-4.7.0.6.tar.gz

Summary:    A compiler for the Scheme programming language
URL:        http://www.call-cc.org/ 

%description
CHICKEN is a compiler for the Scheme programming language. CHICKEN produces
portable and efficient C, supports almost all of the R5RS Scheme language
standard, and includes many enhancements and extensions. CHICKEN runs on Linux,
MacOS X, Windows, and many Unix flavours.

%package devel
Summary:    CHICKEN compiler devel package
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
CHICKEN Scheme compiler development package

%package doc
Summary:    CHICKEN compiler documentation
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description doc
CHICKEN Scheme compiler documentation.

%prep
%setup -q

%build
CFLAGS="%{optflags}" make %{?_smp_mflags}  PLATFORM=linux STATICBUILD=1 PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
%make_install PLATFORM=linux PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm ${RPM_BUILD_ROOT}/%{_libdir}/libchicken.a

cp -r manual-html ${RPM_BUILD_ROOT}/%{_datadir}/chicken/doc/

%{?filter_setup:
%filter_provides_in %{_libdir}/%{name}/?/
%filter_setup
}

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%check
%__arch_install_post \
/usr/lib/rpm/check-rpaths \
/usr/lib/rpm/check-buildroot

%files
%doc LICENSE NEWS* README*
%doc %{_mandir}/man1/chicken*
%doc %{_mandir}/man1/cs?.1.*
%{_libdir}/libchicken.so.6
%{_libdir}/chicken
%{_bindir}/csc
%{_bindir}/csi
%{_bindir}/chicken
%{_bindir}/chicken-install
%{_bindir}/chicken-profile
%{_bindir}/chicken-status
%{_bindir}/chicken-uninstall
%{_bindir}/chicken-bug
%dir %{_datadir}/chicken
%{_datadir}/chicken/setup.defaults

%files devel
%{_libdir}/libchicken.so
%{_includedir}/chicken

%files doc
%doc %{_datadir}/chicken/doc

%changelog
* Thu Feb 14 2013 Minh Ngo <minh@fedoraproject.org> 4.7.0.6-3
- Adding LICENSE NEWS* README* files to the base package
- Moving man pages to the base package 
- Adding html manuals into the doc package
- Adding %{optflags} before building
- Adding library filter
- Moving include files to the devel package

* Tue Jan 14 2013 Minh Ngo <minh@fedoraproject.org> 4.7.0.6-2
- Removing the static lib
- optflags
- devel package

* Fri Nov 09 2012 Minh Ngo <minh@fedoraproject.org> 4.7.0.6-1
- initial build
