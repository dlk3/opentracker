%define  debug_package %{nil}

Name:		opentracker
Version:	2024.08.14
Release:	1%{?dist}
Summary:	Opentracker Bittorrent Tracker

License:	Beerware
URL:		https://erdgeist.org/arts/software/opentracker/
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.conf
Source2:	%{name}.service
BuildArch:	x86_64

BuildRequires:	make
BuildRequires:	zlib-devel
BuildRequires:	clang

%description
opentracker is a open and free bittorrent tracker project. It aims for
minimal resource usage and is intended to run at your wlan router.
By default it is deployed as an open and free tracker instance but
access may be restricted through configuration if necessary.

%prep
%setup

%build
cd libowfat
make pic pie
cd ../opentracker
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} opentracker/opentracker
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 -t %{buildroot}%{_sysconfdir} %{SOURCE1}
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 -t %{buildroot}/usr/lib/systemd/system %{SOURCE2}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 -t %{buildroot}%{_mandir}/man1 opentracker/man1/opentracker.1
mkdir -p %{buildroot}%{_mandir}/man4
install -m 644 -t %{buildroot}%{_mandir}/man4 opentracker/man4/opentracker.conf.4

%files
%doc opentracker/README
%doc opentracker/README_v6
%{_sysconfdir}/opentracker.conf
%{_bindir}/opentracker
/usr/lib/systemd/system/opentracker.service
%{_mandir}/man1/opentracker.1.gz
%{_mandir}/man4/opentracker.conf.4.gz

%changelog
* Thu Aug 15 2024 David King <dave@daveking.com> - 2024.08.14-1
	Replace use of sysconfig file with /etc/ config file.
* Wed Aug 14 2024 David King <dave@daveking.com> - 2024.08.14-0
	Upgrade to libowfat-0.34 and latest development version of opentracker
* Sun Sep 10 2023 David King <dave@daveking.com> - 2018.05.26-4
	Upgrade to libowfat-0.33 to correct compile errors
* Sun Apr 26 2020 David King <dave@daveking.com> - 2018.05.26-3
	Added clang to build requirements
	Upgrade to libowfat-0.32 to correct compile errors
	Patch libowfat to remove duplicate definition
* Mon Dec 23 2019 David King <dave@daveking.com> - 2018.05.26-2
	Added systemd control file
* Sat Dec 21 2019 David King <dave@daveking.com> - 2018.05.26-1
	Initial Version
