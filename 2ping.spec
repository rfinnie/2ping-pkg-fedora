%if 0%{?rhel}
%global with_python3 0
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?py2_build: %global py2_build %{expand: CFLAGS="%{optflags}" %{__python2} setup.py %{?py_setup_args} build --executable="%{__python2} -s"}}
%{!?py2_install: %global py2_install %{expand: CFLAGS="%{optflags}" %{__python2} setup.py %{?py_setup_args} install -O1 --skip-build --root %{buildroot}}}
%endif

Name:           2ping
Version:        3.2.0
Release:        2%{?dist}
Summary:        Bi-directional ping utility
License:        GPLv2+
URL:            http://www.finnie.org/software/2ping
Source0:        http://www.finnie.org/software/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%{?python_provide:%python_provide python2-%{name}}

%description
2ping is a bi-directional ping utility. It uses 3-way pings (akin to TCP SYN, 
SYN/ACK, ACK) and after-the-fact state comparison between a 2ping listener and
a 2ping client to determine which direction packet loss occurs.

%prep
%setup -n %{name}-%{version}

%build
%py2_build

%install
%py2_install
install -d -m 0755 %{buildroot}/usr/share/man/man1
install -m 0644 doc/2ping.1 %{buildroot}/usr/share/man/man1/2ping.1
install -m 0644 doc/2ping.1 %{buildroot}/usr/share/man/man1/2ping6.1

%check
%{__python2} setup.py test

%files
%doc ChangeLog COPYING README
%{python2_sitelib}/*
%{_bindir}/2ping
%{_bindir}/2ping6
%{_mandir}/man1/2ping.1*
%{_mandir}/man1/2ping6.1*

%changelog
* Tue Mar 01 2016 Fabio Alessandro Locati <fabio@locati.cc> - 3.2.0-2
- Fix for EL6 and EPEL7
- Cleanup the SPEC file

* Tue Mar 01 2016 Fabio Alessandro Locati <fabio@locati.cc> - 3.2.0-1
- Update to 3.2.0

* Tue Mar 01 2016 Ryan Finnie <ryan@finnie.org> - 3.1.0-1
- Update to 3.1.0 (#1275261)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-5
- Perl 5.20 rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Christopher Meng <rpm@cicku.me> - 2.0-2
- Perl 5.18 Rebuild.

* Thu May 17 2012 Christopher Meng <rpm@cicku.me> - 2.0-1
- Initial Package.
