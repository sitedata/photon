Summary:    Tool to analyze BIOS DMI data
Name:       dmidecode
Version:    3.4
Release:    1%{?dist}
License:    GPLv2+
URL:        http://www.nongnu.org/dmidecode
Group:      System Environment/Base
Vendor:     VMware, Inc.
Distribution:   Photon

Source0: http://download.savannah.gnu.org/releases/dmidecode/%{name}-%{version}.tar.xz
%define sha512 %{name}=62990b6159e5a7c8688d37e44957e7948391d2c6afeabaa4514ba9dad2d08b020297676e2dbbfcb6471efc6fb6f3682750422931a953f78f358bb3dd3745e95b

%description
Dmidecode reports information about your system's hardware as described in
your system BIOS according to the SMBIOS/DMI standard. This information
typically includes system manufacturer, model name, serial number,
BIOS version, asset tag as well as a lot of other details of varying
level of interest and reliability depending on the manufacturer.

This will often include usage status for the CPU sockets, expansion
slots (e.g. AGP, PCI, ISA) and memory module slots, and the list of
I/O ports (e.g. serial, parallel, USB).

%prep
%autosetup -p1

%build
%make_build

%install
%make_install prefix=%{_prefix} %{?_smp_mflags}

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_docdir}/%{name}/*
%{_mandir}/man8/*

%changelog
* Wed Aug 17 2022 Shreenidhi Shedi <sshedi@vmware.com> 3.4-1
- Upgrade to v3.4
* Mon Apr 12 2021 Gerrit Photon <photon-checkins@vmware.com> 3.3-1
- Automatic Version Bump
* Thu Jun 25 2020 Gerrit Photon <photon-checkins@vmware.com> 3.2-1
- Automatic Version Bump
* Mon Sep 10 2018 Ajay Kaher <akaher@vmware.com> 3.1-1
- Upgraded to version 3.1
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.0-2
- GA - Bump release of all rpms
* Mon Nov 02 2015 Divya Thaluru <dthaluru@vmware.com> 3.0-1
- Initial build. First version
