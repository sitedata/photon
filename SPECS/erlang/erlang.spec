Name:          erlang
Summary:       erlang
Version:       25.1.2
Release:       1%{?dist}
Group:         Development/Languages
Vendor:        VMware, Inc.
Distribution:  Photon
License:       ASL2.0
URL:           https://www.erlang.org

Source0: https://github.com/erlang/otp/archive/refs/tags/OTP-%{version}.tar.gz
%define sha512 OTP=a478799cb7df70a552043da55757b811e8b97182be15ab928e05b58537bb7bc4899aee406648767f538d8bd5c09e0a9d7e3655c99a8df0e6a0b77db83a720fb8

Patch0: 0001-erlang-fix-vernemq-build-fail.patch

Requires:     ncurses-libs

BuildRequires: unzip
BuildRequires: openssl-devel

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%prep
%autosetup -p1 -n otp-OTP-%{version}

%build
export ERL_TOP="${PWD}"
export CFLAGS="-Wno-error=implicit-function-declaration -O2 -g"

%configure \
    --enable-dynamic-ssl-lib \
    --enable-fips

%make_build

%install
%make_install %{?_smp_mflags}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/%{name}/*
%exclude %dir %{_usrsrc}
%exclude %dir %{_libdir}/debug

%changelog
* Fri Oct 28 2022 Gerrit Photon <photon-checkins@vmware.com> 25.1.2-1
- Automatic Version Bump
* Wed Sep 28 2022 Shreenidhi Shedi <sshedi@vmware.com> 24.3.4.5-1
- Upgrade to v24.3.4.5
* Tue Mar 01 2022 Shreenidhi Shedi <sshedi@vmware.com> 23.3.2-4
- Fix binary path
* Tue Jan 11 2022 Nitesh Kumar <kunitesh@vmware.com> 23.3.2-3
- Enable FIPS, Adding ncurses-libs as Requires.
* Fri Jun 04 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 23.3.2-2
- openssl 3.0.0 support
* Mon May 03 2021 Gerrit Photon <photon-checkins@vmware.com> 23.3.2-1
- Automatic Version Bump
* Mon Apr 12 2021 Gerrit Photon <photon-checkins@vmware.com> 23.3.1-1
- Automatic Version Bump
* Wed Sep 23 2020 Satya Naga Vasamsetty <svasamsetty@vmware.com> 23.1-2
- Make openssl changes
* Wed Sep 23 2020 Gerrit Photon <photon-checkins@vmware.com> 23.1-1
- Automatic Version Bump
* Mon Sep 21 2020 Gerrit Photon <photon-checkins@vmware.com> 23.0.4-1
- Automatic Version Bump
* Fri Aug 21 2020 Gerrit Photon <photon-checkins@vmware.com> 23.0.3-1
- Automatic Version Bump
* Mon Jun 22 2020 Gerrit Photon <photon-checkins@vmware.com> 23.0-1
- Automatic Version Bump
* Tue Oct 29 2019 Keerthana K <keerthanak@vmware.com> 22.1-1
- Update to latest version 22.1
* Thu Jan 31 2019 Siju Maliakkal <smaliakkal@vmware.com> 19.3-3
- Revert to old version to fix rabbitmq-server startup failure
* Fri Dec 07 2018 Ashwin H <ashwinh@vmware.com> 21.1.4-1
- Update to version 21.1.4
* Mon Sep 24 2018 Dweep Advani <dadvani@vmware.com> 21.0-1
- Update to version 21.0
* Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 19.3-2
- Remove BuildArch
* Thu Apr 06 2017 Chang Lee <changlee@vmware.com> 19.3-1
- Updated Version
* Mon Dec 12 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 19.1-1
- Initial.
