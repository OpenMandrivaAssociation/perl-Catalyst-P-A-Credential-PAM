%define realname Catalyst-Plugin-Authentication-Credential-PAM
%define abbrevname Catalyst-P-A-Credential-PAM
%define name	perl-%{abbrevname}
%define	modprefix Catalyst

%define version	0.01
%define release	%mkrel 3

Summary:	Authenticate a user against PAM
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Authen::PAM)
BuildRequires:	perl(Catalyst)
Provides:	perl-%{realname}
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is an authentication credential checker that verifies passwords
using a specified PAM service.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}



