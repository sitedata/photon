Summary:        ALSA Utilities
Name:           alsa-utils
Version:        1.2.8
Release:        1%{?dist}
License:        LGPLv2+
URL:            http://alsa-project.org
Group:          Applications/Internet
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://www.alsa-project.org/files/pub/utils/%{name}-%{version}.tar.bz2
%define sha512  %{name}=882e6f67467596ed273bf554fcce87d8ef287806bbdabd6c103de4980981f9e2102fb3800c6e8628ee8e86ffb165c1c92f9370c8145f28a6cb7cca563942330b

Patch0:         ens1371.patch

BuildRequires:  alsa-lib-devel
BuildRequires:  ncurses-devel
BuildRequires:  systemd-devel

Requires:       linux-drivers-sound
Requires:       alsa-lib
Requires:       ncurses

%description
The ALSA Utilities package contains various utilities which are useful for controlling your sound card.

%prep
%autosetup -p1

%build
%configure --disable-alsaconf \
           --disable-xmlto \
           --with-udev-rules-dir=%{_udevrulesdir} \
           --with-systemdsystemunitdir=%{_unitdir}

%make_build

%install
%make_install %{?_smp_mflags}
install -dm 755 %{buildroot}%{_sharedstatedir}/alsa
find %{buildroot} -name \*.la -delete

%post
alsactl init
alsactl -L store

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/*
%{_localstatedir}/*
%{_unitdir}/*
%{_udevrulesdir}/*
%{_libdir}/alsa-topology/libalsatplg_module_nhlt.so
%exclude %dir %{_libdir}/debug

%changelog
* Fri Oct 28 2022 Gerrit Photon <photon-checkins@vmware.com> 1.2.8-1
- Automatic Version Bump
* Mon Jul 11 2022 Gerrit Photon <photon-checkins@vmware.com> 1.2.7-1
- Automatic Version Bump
* Mon Feb 28 2022 Shreenidhi Shedi <sshedi@vmware.com> 1.2.4-2
- Fix binary path
* Mon Apr 12 2021 Gerrit Photon <photon-checkins@vmware.com> 1.2.4-1
- Automatic Version Bump
* Wed Jul 08 2020 Gerrit Photon <photon-checkins@vmware.com> 1.2.3-1
- Automatic Version Bump
* Mon Dec 10 2018 Alexey Makhalov <amakhalov@vmware.com> 1.1.7-1
- initial version, moved from Vivace
