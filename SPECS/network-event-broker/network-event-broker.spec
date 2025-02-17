%ifarch aarch64
%global gohostarch      arm64
%else
%global gohostarch      amd64
%endif

Summary:        Manages network configuration
Name:           network-event-broker
Version:        0.2.1
Release:        4%{?dist}
License:        Apache-2.0
URL:            https://github.com/vmware/%{name}
Source0:        https://github.com/vmware/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
%define sha512  %{name}=d51fa2df334a94a3761479a3e0a175026d8e9f17c8dfaa7b61a44cbfc42e9c486b853699a80947fe122afe49d158277be2bc281c35d30b9f485e6a6625356989
Group:          Networking
Vendor:         VMware, Inc.
Distribution:   Photon

BuildRequires:  go
BuildRequires:  systemd-rpm-macros

Requires:         systemd
Requires(pre):    /usr/sbin/useradd /usr/sbin/groupadd
Requires(postun): /usr/sbin/userdel /usr/sbin/groupdel

%global debug_package %{nil}

%description
A daemon that configures the network and executes scripts on network events such as
systemd-networkd's DBus events or dhclient gaining a lease. It also watches
when an address gets added/removed/modified or links get added/removed.

%prep -p exit
%autosetup -p1 -n %{name}-%{version}

%build
export ARCH=%{gohostarch}
export VERSION=%{version}
export PKG=github.com/%{name}/%{name}
export GOARCH=${ARCH}
export GOHOSTARCH=${ARCH}
export GOOS=linux
export GOHOSTOS=linux
export GOROOT=/usr/lib/golang
export GOPATH=/usr/share/gocode
export GOBIN=/usr/share/gocode/bin
export PATH=$PATH:$GOBIN

mkdir -p ${GOPATH}/src/${PKG}
cp -rf . ${GOPATH}/src/${PKG}
pushd ${GOPATH}/src/${PKG}
go build -o bin/network-broker ./cmd/network-broker
popd

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_sysconfdir}/network-broker
install -m 755 -d %{buildroot}%{_unitdir}

install -pm 755 -t %{buildroot}%{_bindir} ${GOPATH}/src/github.com/%{name}/%{name}/bin/network-broker

install -pm 755 -t %{buildroot}%{_sysconfdir}/network-broker ${GOPATH}/src/github.com/%{name}/%{name}/conf/network-broker.toml
install -pm 755 -t %{buildroot}%{_unitdir}/ ${GOPATH}/src/github.com/%{name}/%{name}/units/network-broker.service

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/network-broker

%{_sysconfdir}/network-broker/network-broker.toml
%{_unitdir}/network-broker.service

%pre
if ! getent group network-broker >/dev/null; then
    /sbin/groupadd -r network-broker
fi

if ! getent passwd network-broker >/dev/null; then
    /sbin/useradd -g network-broker network-broker -s /sbin/nologin
fi

%post
%systemd_post network-broker.service

%preun
%systemd_preun network-broker.service

%postun
%systemd_postun_with_restart network-broker.service

if [ $1 -eq 0 ] ; then
    if getent passwd network-broker >/dev/null; then
        /sbin/userdel network-broker
    fi
    if getent group network-broker >/dev/null; then
        /sbin/groupdel network-broker
    fi
fi

%changelog
* Mon Nov 21 2022 Piyush Gupta <gpiyush@vmware.com> 0.2.1-4
- Bump up version to compile with new go
* Wed Oct 26 2022 Piyush Gupta <gpiyush@vmware.com> 0.2.1-3
- Bump up version to compile with new go
* Fri Jun 17 2022 Piyush Gupta <gpiyush@vmware.com> 0.2.1-2
- Bump up version to compile with new go
* Wed Dec 22 2021 Susant Sahani <ssahani@vmware.com> 0.2.1-1
- Version bump and add groupadd and useradd to requires.
* Tue Dec 14 2021 Susant Sahani <ssahani@vmware.com> 0.2-1
- Version bump.
* Wed Jun 30 2021 Susant Sahani <ssahani@vmware.com> 0.1-1
- Initial rpm release.
