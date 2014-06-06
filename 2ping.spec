Name:           2ping
Version:        2.0
Release:        3%{?dist}
Summary:        Bi-directional ping utility
License:        GPLv2+
URL:            http://www.finnie.org/software/2ping
Source0:        http://www.finnie.org/software/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Digest::CRC)
Requires:       perl(Digest::MD5)
Requires:       perl(Digest::SHA)
Requires:       perl(IO::Socket::INET6)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
2ping is a bi-directional ping utility. It uses 3-way pings (akin to TCP SYN, 
SYN/ACK, ACK) and after-the-fact state comparison between a 2ping listener and
a 2ping client to determine which direction packet loss occurs.

%prep
%setup -q

%build
make EXTRAVERSION=-%{release} %{?_smp_mflags}

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%doc ChangeLog COPYING README
%{_bindir}/2ping
%{_bindir}/2ping6
%{_mandir}/man8/2ping.8*
%{_mandir}/man8/2ping6.8*

%changelog
* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Christopher Meng <rpm@cicku.me> - 2.0-2
- Perl 5.18 Rebuild.

* Thu May 17 2012 Christopher Meng <rpm@cicku.me> - 2.0-1
- Initial Package.
