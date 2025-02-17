%define GCORE_VERSION   1.6.0
%define GDB_VERSION     7.6

Name:          crash
Version:       7.3.0
Release:       1%{?dist}
Summary:       kernel crash analysis utility for live systems, netdump, diskdump, kdump, LKCD or mcore dumpfiles
Group:         Development/Tools
Vendor:        VMware, Inc.
Distribution:  Photon
URL:           http://people.redhat.com/anderson
License:       GPL

Source0: http://people.redhat.com/anderson/crash-%{version}.tar.gz
%define sha512 %{name}=bc288821892c3d7ecbf192d9fe6ea9e73216f8074a24d12a00fbcaf967a1faa38ee69c4a5a97aa93bf75426293f5b275f5ab496c154b4e7be265ba0e263b2bc8

Source1: http://people.redhat.com/anderson/extensions/crash-gcore-command-%{GCORE_VERSION}.tar.gz
%define sha512 crash-gcore=877cb46c54f9059ca0b89f793a0e907102db3921994fa676124bdd688f219a07761fffea6c3369fed836e7049b3611da164d780e7ba8741a4d0a30f7601290c2

Source2: https://ftp.gnu.org/gnu/gdb/gdb-%{GDB_VERSION}.tar.gz
%define sha512 gdb=02d9c62fa73bcb79138d14c7fc182443f0ca82d4545b4d260b67d3f0074ed75f899a657814a56727e601032a668b0ddd7b48aabd49215fc012eeea6077bca368

%ifarch aarch64
Patch0: gcore_defs.patch
%endif

BuildRequires: binutils
BuildRequires: glibc-devel
BuildRequires: ncurses-devel
BuildRequires: zlib-devel

Requires: binutils
Requires: ncurses-libs
Requires: zlib

%description
The core analysis suite is a self-contained tool that can be used to investigate either live systems, kernel core dumps created from the netdump, diskdump and kdump packages from Red Hat Linux, the mcore kernel patch offered by Mission Critical Linux, or the LKCD kernel patch.

%package devel
Group:         Development/Libraries
Summary:       Libraries and headers for %{name}
Requires:      %{name} = %{version}-%{release}

%description devel
The core analysis suite is a self-contained tool that can be used to investigate either live systems, kernel core dumps created from the netdump, diskdump and kdump packages from Red Hat Linux, the mcore kernel patch offered by Mission Critical Linux, or the LKCD kernel patch.

This package contains libraries and header files need for development.

%prep
# Using autosetup is not feasible
%setup -q -n %{name}-%{version}
# Using autosetup is not feasible
%setup -q -a 1
%ifarch aarch64
pushd crash-gcore-command-%{GCORE_VERSION}
%patch0 -p1
popd
%endif

%build
sed -i "s/tar --exclude-from/tar --no-same-owner --exclude-from/" Makefile
cp %{SOURCE2} .
make %{?_smp_mflags} GDB=gdb-%{GDB_VERSION} RPMPKG=%{version}-%{release}
cd crash-gcore-command-%{GCORE_VERSION}
%ifarch x86_64
make %{?_smp_mflags} -f gcore.mk ARCH=SUPPORTED TARGET=X86_64
%endif
%ifarch aarch64
make %{?_smp_mflags} -f gcore.mk ARCH=SUPPORTED TARGET=ARM64
%endif

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_mandir}/man8 \
         %{buildroot}%{_includedir}/crash \
         %{buildroot}%{_libdir}/crash

%make_install %{?_smp_mflags}

install -pm 644 crash.8 %{buildroot}%{_mandir}/man8/crash.8
chmod 0644 defs.h
cp -p defs.h %{buildroot}%{_includedir}/crash
install -pm 755 crash-gcore-command-%{GCORE_VERSION}/gcore.so %{buildroot}%{_libdir}/crash/

%clean
rm -rf "%{buildroot}"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/crash
%{_libdir}/crash/gcore.so
%{_mandir}/man8/crash.8.gz

%files devel
%defattr(-,root,root)
%dir %{_includedir}/crash
%{_includedir}/crash/*.h

%changelog
* Mon May 03 2021 Gerrit Photon <photon-checkins@vmware.com> 7.3.0-1
- Automatic Version Bump
* Mon Nov 30 2020 Alexey Makhalov <amakhalov@vmware.com> 7.2.9-1
- Version update
* Mon May 04 2020 Alexey Makhalov <amakhalov@vmware.com> 7.2.8-1
- Version update
* Fri Sep 07 2018 Ajay Kaher <akaher@vmware.com> 7.2.3-1
- Upgrading to version 7.2.3
* Tue Nov 14 2017 Alexey Makhalov <amakhalov@vmware.com> 7.1.8-2
- Aarch64 support
* Wed Mar 22 2017 Alexey Makhalov <amakhalov@vmware.com> 7.1.8-1
- Update version to 7.1.8 (it supports linux-4.9)
- Disable a patch - it requires a verification.
* Fri Oct 07 2016 Alexey Makhalov <amakhalov@vmware.com> 7.1.5-2
- gcore-support-linux-4.4.patch
* Fri Sep 30 2016 Alexey Makhalov <amakhalov@vmware.com> 7.1.5-1
- Update version to 7.1.5 (it supports linux-4.4)
- Added gcore plugin
- Remove zlib-devel requirement from -devel subpackage
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 7.1.4-2
- GA - Bump release of all rpms
* Fri Jan 22 2016 Xiaolin Li <xiaolinl@vmware.com> 7.1.4-1
- Updated to version 7.1.4
* Wed Nov 18 2015 Anish Swaminathan <anishs@vmware.com> 7.1.3-1
- Initial build. First version
