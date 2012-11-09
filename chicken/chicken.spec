Name:       chicken 
Version:    4.7.0.6 
Release:    1%{?dist}
License:    GPLv3
Source0:    http://code.call-cc.org/stability/4.7.0/chicken-4.7.0.6.tar.gz

Summary:    A compiler for the Scheme programming language
URL:        http://www.call-cc.org/ 

%description
CHICKEN is a compiler for the Scheme programming language. CHICKEN produces
portable and efficient C, supports almost all of the R5RS Scheme language
standard, and includes many enhancements and extensions. CHICKEN runs on Linux,
MacOS X, Windows, and many Unix flavours.

%package static
Summary:    CHICKEN static library
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description static
CHICKEN Scheme compiler static library.

%package doc
Summary:    CHICKEN compiler documentation
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description doc
CHICKEN Scheme compiler documentation.

%prep
%setup -q

%build
make %{?_smp_mflags} PLATFORM=linux STATICBUILD=1 

%install
%make_install PLATFORM=linux PREFIX=%{_prefix}

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files
%{_prefix}/lib/libchicken.so
%{_prefix}/lib/libchicken.so.6
%{_prefix}/lib/chicken
%{_includedir}/chicken
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

%files static 
%{_prefix}/lib/libchicken.a

%files doc
%doc %{_datadir}/chicken/doc
%doc %{_mandir}/man1/chicken*
%doc %{_mandir}/man1/cs?.1.gz

%changelog
* Fri Nov 09 2012 Minh Ngo <minh@fedoraproject.org> 4.7.0.6-1
- initial build
