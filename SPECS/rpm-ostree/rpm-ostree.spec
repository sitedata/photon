Summary:        Commit RPMs to an OSTree repository
Name:           rpm-ostree
Version:        2022.13
Release:        3%{?dist}
License:        LGPLv2+
Group:          Applications/System
URL:            https://github.com/projectatomic/rpm-ostree
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: https://github.com/projectatomic/rpm-ostree/releases/download/v%{version}/rpm-ostree-%{version}.tar.xz
%define sha512 %{name}=09f8d7554d694e8fbd61d713d0b01f3076c3638f81698fc8208055e11fc6f1e79f77d8e18386ef579a819b8db5c26178b3926775d87e2eb1a47e0ebf9c606a89

Source1:        mk-ostree-host.sh
Source2:        function.inc
Source3:        mkostreerepo

Patch0:         rpm-ostree-libdnf-build.patch
Patch1:         util-Fix-fpermissive-warning.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  git
BuildRequires:  json-glib-devel
BuildRequires:  json-c-devel
BuildRequires:  gtk-doc
BuildRequires:  libcap-devel
BuildRequires:  sqlite-devel
BuildRequires:  cppunit-devel
BuildRequires:  polkit-devel
BuildRequires:  ostree-devel
BuildRequires:  docbook-xsl
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  openssl-devel
BuildRequires:  rpm-devel
BuildRequires:  librepo-devel
BuildRequires:  attr-devel
BuildRequires:  python3-devel
BuildRequires:  autogen
BuildRequires:  libsolv-devel >= 0.7.19
BuildRequires:  systemd-devel
BuildRequires:  libarchive-devel
BuildRequires:  gperf
BuildRequires:  which
BuildRequires:  popt-devel
BuildRequires:  createrepo_c
BuildRequires:  photon-release
BuildRequires:  photon-repos
BuildRequires:  bubblewrap
BuildRequires:  dbus
BuildRequires:  rust
BuildRequires:  libmodulemd-devel
BuildRequires:  gpgme-devel

Requires:       libcap
Requires:       rpm-libs
Requires:       sqlite-libs
Requires:       systemd
Requires:       gpgme
Requires:       glib
Requires:       json-c
Requires:       polkit
Requires:       libarchive
Requires:       libmodulemd
Requires:       libgcc
Requires:       librepo
Requires:       openssl
Requires:       ostree
Requires:       ostree-libs
Requires:       ostree-grub2
Requires:       json-glib
Requires:       libsolv
Requires:       bubblewrap

%description
This tool takes a set of packages, and commits them to an OSTree
repository.  At the moment, it is intended for use on build servers.

%package devel
Summary: Development headers for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Includes the header files for the %{name} library.

%package host
Summary: File for %{name}-host creation
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description host
Includes the scripts for %{name} host creation

%package repo
Summary: File for Repo Creation to act as server
Group: Applications/System
Requires: %{name} = %{version}-%{release}

%description repo
Includes the scripts for %{name} repo creation to act as server

%prep
%autosetup -p1

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules --enable-gtk-doc
%make_build

%install
%make_install %{?_smp_mflags}
install -d %{buildroot}%{_bindir}/%{name}-host
install -d %{buildroot}%{_bindir}/%{name}-server
install -p -m 755 -D %{SOURCE1} %{buildroot}%{_bindir}/%{name}-host
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_bindir}/%{name}-host
install -p -m 755 -D %{SOURCE3} %{buildroot}%{_bindir}/%{name}-server

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/%{name}/
%{_libdir}/*.so.1*
%{_libdir}/girepository-1.0/*.typelib
%{_unitdir}/*.service
%{_libexecdir}/*
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/dbus-1/system-services/*
%config(noreplace) %{_sysconfdir}/rpm-ostreed.conf
%{_unitdir}/%{name}-countme.timer
%{_libdir}/systemd/system/rpm-ostreed-automatic.timer
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/dbus-1/interfaces/org.projectatomic.rpmostree1.xml
%{_datadir}/polkit-1/actions/org.projectatomic.rpmostree1.policy
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man5/rpm-ostreed*
%{_mandir}/man8/%{name}*

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/*-1.0.gir

%files host
%defattr(-,root,root)
%{_bindir}/rpm-ostree-host/mk-ostree-host.sh
%{_bindir}/rpm-ostree-host/function.inc

%files repo
%defattr(-,root,root)
%{_bindir}/rpm-ostree-server/mkostreerepo

%changelog
* Thu Nov 03 2022 Ankit Jain <ankitja@vmware.com> 2022.13-3
- Fix build issue after glib update
* Fri Oct 07 2022 Shreenidhi Shedi <sshedi@vmware.com> 2022.13-2
- Bump version as a part of libxslt upgrade
* Fri Oct 07 2022 Shreenidhi Shedi <sshedi@vmware.com> 2022.13-1
- Upgrade to v2022.13
* Tue Oct 04 2022 Shreenidhi Shedi <sshedi@vmware.com> 2021.12-8
- Bump version as a part of polkit upgrade
* Wed Sep 28 2022 Shreenidhi Shedi <sshedi@vmware.com> 2021.12-7
- Bump version as a part of libsolv upgrade
* Sat Jul 30 2022 Shreenidhi Shedi <sshedi@vmware.com> 2021.12-6
- Bump version as a part of sqlite upgrade
* Sun Jul 03 2022 Shreenidhi Shedi <sshedi@vmware.com> 2021.12-5
- Bump version as a part of rpm upgrade
* Thu Jun 16 2022 Ashwin Dayanand Kamat <kashwindayan@vmware.com> 2021.12-4
- Bump version as a part of libxslt upgrade
* Wed Nov 10 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 2021.12-3
- openssl 3.0.0 compatibility
* Wed Oct 20 2021 Shreenidhi Shedi <sshedi@vmware.com> 2021.12-2
- Bump version as a part of rpm upgrade
* Sat Oct 16 2021 Shreenidhi Shedi <sshedi@vmware.com> 2021.12-1
- Bump version & changes for open-vm-tools spec refactoring
- libdnf & libglnx are part of rpm-ostree source.
* Fri Jun 11 2021 Oliver Kurth <okurth@vmware.com> 2020.5-6
- build with libsolv 0.7.19
* Mon Jan 11 2021 Ankit Jain <ankitja@vmware.com> 2020.5-5
- Added systemd-udev in mkostreerepo
* Tue Nov 03 2020 Ankit Jain <ankitja@vmware.com> 2020.5-4
- Adding grub2-efi-image for both x86 and aarch64 in mkostreerepo
* Mon Oct 05 2020 Ankit Jain <ankitja@vmware.com> 2020.5-3
- Changing branch to 4.0 in mkostreerepo
* Mon Oct 05 2020 Ankit Jain <ankitja@vmware.com> 2020.5-2
- Re-enabling ostree
* Mon Sep 21 2020 Ankit Jain <ankitja@vmware.com> 2020.5-1
- Updated to 2020.5
* Tue Sep 08 2020 Ankit Jain <ankitja@vmware.com> 2020.4-2
- Updated mkostreerepo as per photon-base.json
* Thu Aug 13 2020 Ankit Jain <ankitja@vmware.com> 2020.4-1
- Updated to 2020.4
* Mon Jun 22 2020 Tapas Kundu <tkundu@vmware.com> 2019.3-4
- Build with python3
- Mass removal python2
* Thu Oct 24 2019 Ankit Jain <ankitja@vmware.com> 2019.3-3
- Added for ARM Build
* Fri Sep 20 2019 Ankit Jain <ankitja@vmware.com> 2019.3-2
- Added script to create repo data to act as ostree-server
* Tue May 14 2019 Ankit Jain <ankitja@vmware.com> 2019.3-1
- Initial version of rpm-ostree
