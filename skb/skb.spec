Name:       skb 
Version:    0.4
Release:    1%{?dist}
License:    GPLv2
Source0:    http://plhk.ru/static/skb/skb-0.4.tar.gz  

Summary:    Simple keyboard layout indicator
URL:        http://plhk.ru/ 

BuildRequires:  libX11-devel

%description
%{summary}.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=${RPM_BUILD_ROOT} PREFIX=%{_prefix}

%files
%doc LICENSE README 
%{_bindir}/skb

%changelog
* Tue Nov 05 2012 Minh Ngo <minh@fedorapeople.org> 0.4-1
- initial build
