%define srcname concurrent-log-handler

Name:           python3-ConcurrentLogHandler
Version:        0.9.20
Release:        1%{?dist}
Summary:        Concurrent logging handler (drop-in replacement for RotatingFileHandler) Python 2.6+
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Preston-Landers/concurrent-log-handler
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: %{srcname}-%{version}.tar.gz
%define sha512 %{srcname}=fd9e66c713f6be675fd8aa8001254641ba354ba04b95fade4b101ce9cdddc66444de60c87832bd3270d004ef97c52a266a3345e9f9df8f5dea13d6ce80f05e57

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?with_check}
BuildRequires:  python3-pytest
%endif

Requires:       python3
Requires:       python3-setuptools

BuildArch:      noarch

%description
ConcurrentLogHandler is a module that provides an additional log handler for Python’s standard logging package (PEP 282). This handler will write log events to log file which is rotated when the log file reaches a certain size. Multiple processes can safely write to the same log file concurrently.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%defattr(-,root,root)
%exclude %{_usr}/tests/stresstest.py
%{python3_sitelib}/*

%changelog
* Tue Nov 15 2022 Shreenidhi Shedi <sshedi@vmware.com> 0.9.20-1
- Upgrade to v0.9.20
* Tue Dec 15 2020 Shreenidhi Shedi <sshedi@vmware.com> 0.9.1-5
- Fix build with new rpm
* Tue Jun 16 2020 Tapas Kundu <tkundu@vmware.com> 0.9.1-4
- Mass removal python2
* Mon Dec 03 2018 Ashwin H <ashwinh@vmware.com> 0.9.1-3
- Add %check
* Thu Sep 21 2017 Bo Gan <ganb@vmware.com> 0.9.1-2
- Disable test as no tests are available
* Fri Aug 25 2017 Vinay Kulkarni <kulkarniv@vmware.com> 0.9.1-1
- Initial version of python-ConcurrentLogHandler package for Photon.
