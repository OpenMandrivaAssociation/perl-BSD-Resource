%define	upstream_name	 BSD-Resource
%define upstream_version 1.2904

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	10

Summary:	BSD process resource limit and priority functions
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/BSD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install

%makeinstall_std

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorarch}/BSD
%{perl_vendorarch}/auto/BSD
%{_mandir}/man*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.290.400-7mdv2012.0
+ Revision: 765077
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.290.400-6
+ Revision: 763529
- bump to what's higher than what's actually in cooker (wtf?)
- rebuild
- rebuilt for perl-5.14.x

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.2904

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.290.400-5
+ Revision: 676886
- rebuild
- rebuild
- rebuild
- rebuild
- mass rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.2904
    - update to new version 1.2904

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.290.400-4mdv2011.0
+ Revision: 564360
- rebuild for perl 5.12.1

* Tue Jul 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.400-3mdv2011.0
+ Revision: 555688
- rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.290.400-2mdv2011.0
+ Revision: 555440
- rebuild

* Mon Mar 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.400-1mdv2010.1
+ Revision: 519947
- update to 1.2904

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.2903

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.300-2mdv2010.0
+ Revision: 405787
- bumping mkrel to force rebuild
- rebuild

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.300-1mdv2010.0
+ Revision: 395064
- update to 1.2903
- using %%perl_convert_version
- fixed license field

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.29-3mdv2009.1
+ Revision: 351680
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.29-2mdv2009.0
+ Revision: 223569
- rebuild

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2008.1
+ Revision: 159931
- update to new version 1.29

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.28-3mdv2008.1
+ Revision: 151466
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 09:25:58 (63274)
- rebuild

* Sat Oct 07 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-06 07:11:30 (62910)
- Import perl-BSD-Resource

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.28-1mdv2007.0
- New release 1.28

* Wed May 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.26-1mdk
- 1.26

* Wed Apr 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-2mdk
- better source URL

* Wed Apr 12 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.25-1mdk
- 1.25

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-4mdk
- %%mkrel
- fix optimisations
- fix directory ownership
- better summary
- rpmbuildupdate aware
- spec cleanup

* Fri Jun 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.24-3mdk
- Rebuild

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.24-2mdk
- Rebuild for new perl

* Tue Apr 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.24-1mdk
- 1.24
- disable test

