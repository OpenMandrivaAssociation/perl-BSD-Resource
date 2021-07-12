%define	upstream_name	 BSD-Resource
%define upstream_version 1.2911

Summary:	BSD process resource limit and priority functions
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/BSD::Resource
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/BSD/BSD-Resource-%{upstream_version}.tar.gz
BuildRequires:	perl-devel

%description
%{upstream_name} module for perl

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%make_install

%files
%doc ChangeLog README
%{perl_vendorarch}/BSD
%{perl_vendorarch}/auto/BSD
%{_mandir}/man3/*


