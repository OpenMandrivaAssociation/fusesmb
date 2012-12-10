%define name		fusesmb
%define version		0.8.7
%define release		%mkrel 3

Name:		%name
Version:	%version
Release:	%release
URL:		http://www.ricardis.tudelft.nl/~vincent/fusesmb/
BuildRequires:	libsmbclient-devel, fuse-devel, samba-client
Requires:	libsmbclient, fuse, samba-client
Source:		http://www.ricardis.tudelft.nl/~vincent/fusesmb/download/%{name}-%{version}.tar.gz
Patch0:		fusesmb-0.8.7-fix-str-fmt.patch
License:	GPLv2+
Summary:	Browse your network neighbourhood as if it were on your own filesystem
Group:		Networking/Other
BuildRoot:	%{_tmppath}/%{name}-root
%description
With SMB for Fuse you can seamlessly browse your network neighbourhood
as if it were on your own filesystem.

It's basically smbmount with a twist. Instead of mounting one Samba share
at a time, you mount all workgroups, hosts and shares at once. Only when
you're accessing a share a connection is made to the remote computer. 

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO AUTHORS README INSTALL ChangeLog COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}.cache
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.7-3mdv2011.0
+ Revision: 610779
- rebuild

* Tue Feb 02 2010 Funda Wang <fwang@mandriva.org> 0.8.7-2mdv2010.1
+ Revision: 499610
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 16 2008 Funda Wang <fwang@mandriva.org> 0.8.7-1mdv2009.0
+ Revision: 236564
- clearify the license

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Nicolas Vigier <nvigier@mandriva.com> 0.8.7-1mdv2008.1
+ Revision: 132282
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jun 19 2007 Nicolas Vigier <nvigier@mandriva.com> 0.8.6-1mdv2008.0
+ Revision: 41394
- update to version 0.8.6

* Wed May 23 2007 Nicolas Vigier <nvigier@mandriva.com> 0.8.5-1mdv2008.0
+ Revision: 30252
- Import fusesmb

