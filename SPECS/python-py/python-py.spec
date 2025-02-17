Name:           python3-py
Version:        1.9.0
Release:        2%{?dist}
Summary:        Python development support library
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/pytest-dev/py
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: https://github.com/pytest-dev/py/archive/refs/tags/py-%{version}.tar.gz
%define sha512 py=965b2adfe1b13177629ccfcdf6d0a13460683ca7a01d585163deb1af15d926fc86680d9e51660f6cbb8569f822a4d54ce281c029e363d244ddf67e33b102ad0a

Patch0: python-py-CVE-2020-29651.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-xml

%if 0%{?with_check}
BuildRequires: python3-pytest
%endif

Requires:       python3

BuildArch:      noarch

%description
The py lib is a Python development support library featuring the following tools and modules:

py.path: uniform local and svn path objects
py.apipkg: explicit API control and lazy-importing
py.iniconfig: easy parsing of .ini files
py.code: dynamic code generation and introspection

%prep
%autosetup -p1 -n py-%{version}

%build
%py3_build

%install
%py3_install

%if 0%{?with_check}
%check
%pytest
%endif

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
* Mon Jun 21 2021 Dweep Advani <dadvani@vmware.com> 1.9.0-2
- Patched for CVE-2020-29651
* Tue Jul 28 2020 Tapas Kundu <tkundu@vmware.com> 1.9.0-1
- Updated to version 1.9.0
* Tue Jun 16 2020 Tapas Kundu <tkundu@vmware.com> 1.6.0-2
- Mass removal python2
* Thu Sep 13 2018 Tapas Kundu <tkundu@vmware.com> 1.6.0-1
- Updated to versiob 1.6.0
* Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 1.4.33-3
- Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
* Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.4.33-2
- Use python2_sitelib
* Tue Apr 25 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.4.33-1
- Initial
