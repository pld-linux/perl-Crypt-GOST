%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	GOST
Summary:	Crypt::GOST Perl module - the GOST Encryption Algorithm
Summary(pl):	Modu³ Perla Crypt::GOST - algorytm kodowania GOST
Name:		perl-Crypt-GOST
Version:	1.00
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements GOST encryption. It supports the Crypt::CBC
interface. GOST 28147-89 is a 64-bit symmetric block cipher with a
256-bit key developed in the former Soviet Union. Some information on
it is available at http://vipul.net/gost/.

%description -l pl
Ten modu³ jest implementacj± kodowania GOST. Obs³uguje interfejs
Crypt::CBC. GOST 28147-89 jest 64-bitowym symetrycznym szyfrem
blokowym z 256-bitowym kluczem. Zosta³ opracowany w by³ym Zwi±zku
Radzieckim. Wiêcej informacji na stronie http://vipul.net/gost/.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Crypt/GOST.pm
%dir %{perl_sitearch}/auto/Crypt/GOST
%{perl_sitearch}/auto/Crypt/GOST/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/GOST/*.so
%{_mandir}/man3/*
