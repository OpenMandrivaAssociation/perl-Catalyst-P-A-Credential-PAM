%define realname Catalyst-Plugin-Authentication-Credential-PAM
%define abbrevname Catalyst-P-A-Credential-PAM
%define	modprefix Catalyst

Summary:	Authenticate a user against PAM
Name:		perl-%{abbrevname}
Version:	0.01
Release:	11
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Authen::PAM)
BuildRequires:	perl(Catalyst)
Provides:	perl-%{realname} = %{version}-%{release}
BuildArch:	noarch

%description
This is an authentication credential checker that verifies passwords
using a specified PAM service.

%prep
%setup -q -n %{realname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.01-8mdv2011.0
+ Revision: 680724
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.01-7mdv2011.0
+ Revision: 430268
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.01-6mdv2009.0
+ Revision: 255527
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.01-4mdv2008.1
+ Revision: 136671
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-4mdv2008.0
+ Revision: 85926
- rebuild


* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 01:55:16 (54289)
- Rebuild, spec file cleanup

* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 01:50:48 (54287)
- import perl-Catalyst-P-A-Credential-PAM-0.01-2mdk

* Tue May 16 2006 Scott Karns <scottk@mandriva.org> 0.01-2mdk
- Cleaned up handling of module abbreviation

* Tue May 16 2006 Scott Karns <scottk@mandriva.org> 0.01-1mdk
- Initial MDV RPM

