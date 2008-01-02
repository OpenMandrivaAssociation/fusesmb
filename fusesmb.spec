%define name		fusesmb
%define version		0.8.7
%define release		%mkrel 1

Name:		%name
Version:	%version
Release:	%release
URL:		http://www.ricardis.tudelft.nl/~vincent/fusesmb/
BuildRequires:	libsmbclient-devel, fuse-devel, samba-client
Requires:	libsmbclient, fuse, samba-client
Source:		http://www.ricardis.tudelft.nl/~vincent/fusesmb/download/%{name}-%{version}.tar.gz
License:	GPL
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

%build
%configure
%make

%install
%makeinstall

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO AUTHORS README INSTALL ChangeLog COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}.cache
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*

