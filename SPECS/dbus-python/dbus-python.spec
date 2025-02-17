%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%global __python3 \/usr\/bin\/python3

Name:           dbus-python3
Version:        1.3.2
Release:        1%{?dist}
Summary:        Python bindings for D-Bus
License:        MIT
Group:          Development/Libraries/Python
Url:            http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0:        http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz
%define         sha512 dbus-python=9b2885c9c2914142c72487f766b1cdd28a255d9f5a87eaf8f4eb420c6e096a77f210ac5a4fac9843c6531974872880cc28b7e45940e198856e984dcc0715519a
Vendor:         VMware, Inc.
Distribution:   Photon

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-docutils
BuildRequires:  dbus-devel
BuildRequires:  glib-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-devel

Requires:       python3-xml
Requires:       dbus

%description
D-Bus python bindings for use with python programs.

%package -n     dbus-python3-devel
Summary:        Python bindings for D-Bus
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       dbus-devel

%description -n dbus-python3-devel
Developer files for Python bindings for D-Bus.

%prep
%autosetup  -n dbus-python-%{version}

%build
%configure PYTHON="%{__python3}"
%make_build %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}
cp -r dbus_python*egg-info %{buildroot}%{python3_sitelib}
rm -f %{buildroot}%{python3_sitelib}/*.la

%check
# make doesn't support _smp_mflags
make check

%files
%defattr(-,root,root)
%doc NEWS
%license COPYING
%{python3_sitelib}/*.so
%{python3_sitelib}/dbus/
%{python3_sitelib}/dbus_python*egg-info

%files devel
%defattr(-,root,root)
%doc README ChangeLog doc/API_CHANGES.txt doc/tutorial.txt
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
* Tue Nov 01 2022 Susant Sahani <ssahani@vmware.com> 1.3.2-1
- version bump
* Mon Dec 14 2020 Susant Sahani <ssahani@vmware.com> 1.2.16-2
- Add build requires
* Thu Mar 19 2020 Tapas Kundu <tkundu@vmware.com> 1.2.16-1
- Initial release
