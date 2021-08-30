Name:           Nikitatest
Version:        1.0
Release:        1%{?dist}
Summary:        Test application

License:        GPL
URL:            http://oracle-base.com/articles/linux/linux-build-simple-rpm-packages.php
Source0:        %{name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
TestTask by Nikita Fedorov

%global debug_package %{nil}

%prep
%setup -q


%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 0755 Nikitatest $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/bin/Nikitatest

%changelog
* Mon Aug 30 2021 Nikita
- 
