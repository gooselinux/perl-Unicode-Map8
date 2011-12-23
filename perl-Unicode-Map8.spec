%{!?perl_vendorarch: %define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)}

Name:           perl-Unicode-Map8
Version:        0.12
Release:        20%{?dist}

Summary:        Mapping table between 8-bit chars and Unicode for Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Unicode-Map8/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/Unicode-Map8-0.12.tar.gz
Patch0:         perl-Unicode-Map8-0.12-declaration.patch
Patch1:         perl-Unicode-Map8-0.12-type.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl(ExtUtils::MakeMaker), perl(Unicode::String)


%description
The Unicode::Map8 class implements efficient mapping tables between
8-bit character sets and 16 bit character sets like Unicode.  About
170 different mapping tables between various known character sets and
Unicode is distributed with this package.  The source of these tables
is the vendor mapping tables provided by Unicode, Inc. and the code
tables in RFC 1345.  New maps can easily be installed.


%prep
%setup -q -n Unicode-Map8-%{version}
%patch0 -p0 -b .declaration
%patch1 -p0 -b .type


%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install \
  PERL_INSTALL_ROOT=$RPM_BUILD_ROOT \
  INSTALLARCHLIB=$RPM_BUILD_ROOT%{perl_archlib}
find $RPM_BUILD_ROOT -type f -a \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/umap
%{perl_vendorarch}/auto/Unicode
%{perl_vendorarch}/Unicode
%{_mandir}/man[13]/*.[13]*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.12-18
- fix build

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.12-17
- Rebuild for perl 5.10 (again)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.12-16
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.12-15
- rebuild for new perl

* Thu Sep 27 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.12-14
- fix license tag again (thanks Tom)

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.12-13
- fix license tag (like perl itself)

* Mon Aug 13 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.12-12
- BR: perl-devel

* Sun Oct 29 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.12-11
- actually apply the patches

* Sat Oct 28 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.12-10
- add patches for x86_64

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.12-9
- rebuild

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 0.12-8
- ExcludeArch x86_64

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 0.12-7
- disable unit tests (map8.t fails on x86_64)

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.12-6
- rebuild for FC5

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.12-0.fdr.4
- Reduce directory ownership bloat.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.12-0.fdr.3
- Install into vendor dirs.
- Specfile cleanup.

* Mon Jul  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.12-0.fdr.2
- Regenerate %%install section with cpanflute2.

* Wed May  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.12-0.fdr.1
- Update to current Fedora guidelines.

* Sun Mar  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.12-1.fedora.1
- First Fedora release.
