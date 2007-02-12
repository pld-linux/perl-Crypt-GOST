#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	GOST
Summary:	Crypt::GOST Perl module - the GOST encryption algorithm
Summary(pl.UTF-8):   Moduł Perla Crypt::GOST - algorytm kodowania GOST
Name:		perl-Crypt-GOST
Version:	1.00
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0250fb0539db739baf6608318894d67d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements GOST encryption. It supports the Crypt::CBC
interface. GOST 28147-89 is a 64-bit symmetric block cipher with a
256-bit key developed in the former Soviet Union. Some information on
it is available at http://vipul.net/gost/.

%description -l pl.UTF-8
Ten moduł jest implementacją kodowania GOST. Obsługuje interfejs
Crypt::CBC. GOST 28147-89 jest 64-bitowym symetrycznym szyfrem
blokowym z 256-bitowym kluczem. Został opracowany w byłym Związku
Radzieckim. Więcej informacji na stronie http://vipul.net/gost/.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/GOST.pm
%dir %{perl_vendorarch}/auto/Crypt/GOST
%{perl_vendorarch}/auto/Crypt/GOST/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/GOST/*.so
%{_mandir}/man3/*
