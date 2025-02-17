Name:           python3-bcrypt
Version:        3.2.0
Release:        1%{?dist}
Summary:        Good password hashing for your software and your servers.
License:        Apache License, Version 2.0
Group:          Development/Languages/Python
Url:            https://github.com/pyca/bcrypt
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: https://github.com/pyca/bcrypt/archive/refs/tags/bcrypt-%{version}.tar.gz
%define sha512 bcrypt=aa782aa6a725434e0b0737973e33e6c2bf4e82d39e8dfba0913da5d7dd051d55217adab8004c3eaf896fc3c3e145ba543da1b5162a667a3d82a4eb6b07430b80

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
BuildRequires:  python3-xml

%if 0%{?with_check}
BuildRequires:  curl-devel
%endif

Requires:       python3

%description
Good password hashing for your software and your servers.

%prep
%autosetup -n bcrypt-%{version}

%build
%py3_build

%install
%py3_install

%if 0%{?with_check}
%check
easy_install_3=$(ls /usr/bin |grep easy_install |grep 3)
$easy_install_3 pytest
python3 setup.py test
%endif

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
* Wed Aug 19 2020 Gerrit Photon <photon-checkins@vmware.com> 3.2.0-1
- Automatic Version Bump
* Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 3.1.7-1
- Automatic Version Bump
* Fri Jun 19 2020 Tapas Kundu <tkundu@vmware.com> 3.1.6-3
- Mass removal python2
* Tue Sep 03 2019 Shreyas B. <shreyasb@vmware.com> 3.1.6-2
- Fix make check errors.
* Wed Mar 06 2019 Tapas Kundu <tkundu@vmware.com> 3.1.6-1
- Initial packaging for Photon
