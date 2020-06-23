Summary:	Google's C++ logging module
Name:		glog
Version:	0.4.0
Release:	1%{?dist}
License:	BSD
URL:		https://github.com/google/glog
Source0:	https://github.com/google/glog/archive/%{name}-%{version}.tar.gz
%define sha1 glog=0d79fb524591dee0f46213e9a23f609f74e0cbb2
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution: 	Photon
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libgcc
BuildRequires:  libtool

%description
Google's C++ logging module

%package devel
Summary:        glog devel
Group:          Development/Tools
%description devel
This contains development tools and libraries for glog.

%package docs
Summary:        glog docs
Group:          Development/Tools
%description docs
The contains glog package doc files.

%prep
%setup -n %{name}-%{version}

%build
./autogen.sh
%configure \
    --disable-silent-rules
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%files
%defattr(-,root,root)
%{_libdir}/libglog.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*
%{_libdir}/libglog.a
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc

%files docs
%defattr(-,root,root)
%{_docdir}/*

%changelog
*   Mon Jun 22 2020 Gerrit Photon <photon-checkins@vmware.com> 0.4.0-1
-   Automatic Version Bump
*   Mon Sep 10 2018 Michelle Wang <michellew@vmware.com> 0.3.5-1
-   Update version to 0.3.5.
*   Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 0.3.4-3
-   Use standard configure macros
*   Thu Jun 1  2017 Bo Gan <ganb@vmware.com> 0.3.4-2
-   Fix file paths
*   Sat Mar 25 2017 Vinay Kulkarni <kulkarniv@vmware.com> 0.3.4-1
-   Initial version of glog for Photon.
