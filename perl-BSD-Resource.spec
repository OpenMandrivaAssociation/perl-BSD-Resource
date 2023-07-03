%undefine _debugsource_packages
%define	upstream_name	 BSD-Resource

Summary:	BSD process resource limit and priority functions
Name:		perl-%{upstream_name}
Version:	1.2911
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/BSD::Resource
Source0:	http://www.cpan.org/modules/by-module/BSD/BSD-Resource-%{version}.tar.gz
BuildRequires:	perl-devel

%description
%{upstream_name} module for perl

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

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


