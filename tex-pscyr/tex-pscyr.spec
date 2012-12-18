Name:       tex-pscyr 
Version:    0.4d
Release:    1%{?dist}
License:    PSCyr License
Source0:    ftp://scon155.phys.msu.su/pub/russian/psfonts/PSCyr-0.4c-patch2-tex.tar.gz
Source1:    ftp://scon155.phys.msu.su/pub/russian/psfonts/PSCyr-0.4c-patch2-type1.tar.gz
Summary:    PSCyr Type1 Font Collection
URL:        ftp://scon155.phys.msu.su/pub/russian/psfonts/  
BuildArch:  noarch

BuildRequires: texlive 

%description
%{summary}.

%prep
mkdir -p %{name}-%{version}-%{release}
pushd %{name}-%{version}-%{release}
  tar -xvxf %{SOURCE0}
  tar -xvxf %{SOURCE1}
popd

%build

%install
export TEXMFMAIN=${RPM_BUILD_ROOT}/usr/share/texmf  
pushd %{name}-%{version}-%{release}
  ./install.sh
popd

%files
%doc LICENSE ChangeLog 
%doc %{_datadir}/texmf/doc/fonts/pscyr
%{_datadir}/texmf/fonts/afm/public/pscyr 
%{_datadir}/texmf/fonts/vf/public/pscyr
%{_datadir}/texmf/fonts/tfm/public/pscyr
%{_datadir}/texmf/fonts/type1/public/pscyr
%{_datadir}/texmf/ls-R
%{_datadir}/texmf/tex/latex/pscyr

%changelog
* Tue Dec 18 2012 Minh Ngo <minh@fedoraproject.org> 0.4d  
- initial build
