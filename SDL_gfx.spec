%define major 13
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s

Summary:	SDL graphics drawing primitives and other support functions
Name:		SDL_gfx
Version:	2.0.23
Release:	3
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/index.html
Source0:	http://www.ferzkopp.net/Software/SDL_gfx-2.0/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	tiff-devel

%description
The SDL_gfx library evolved out of the SDL_gfxPrimitives code.

The current components of the SDL_gfx library are:
- Graphic Primitives (SDL_gfxPrimitves.h)
- Rotozoomer (SDL_rotozoom.h)
- Framerate control (SDL_framerate.h)
- MMX image filters (SDL_imageFilter.h)

The library is backwards compatible to the above mentioned code. It's
is written in plain C and can be used in C++ code.

%package -n %{libname}
Summary:	SDL graphics drawing primitives and other support functions
Group:		System/Libraries

%description -n %{libname}
The SDL_gfx library evolved out of the SDL_gfxPrimitives code.

The current components of the SDL_gfx library are:
- Graphic Primitives (SDL_gfxPrimitves.h)
- Rotozoomer (SDL_rotozoom.h)
- Framerate control (SDL_framerate.h)
- MMX image filters (SDL_imageFilter.h)

The library is backwards compatible to the above mentioned code. It's
is written in plain C and can be used in C++ code.

%package -n %{develname}
Summary:	Header files and more to develop SDL_gfx applications
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	SDL-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Header files and more to develop SDL_gfx applications.

%package -n %{staticname}
Summary:	Static SDL_gfx libraries
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}

%description -n	%{staticname}
Static SDL_gfx libraries.

%prep
%setup -q

%build
%configure2_5x --disable-mmx
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc README ChangeLog AUTHORS Docs
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files -n %{staticname}
%{_libdir}/lib*.a


%changelog
* Tue Feb 21 2012 Götz Waschk <waschk@mandriva.org> 2.0.23-2mdv2012.0
+ Revision: 778751
- manually remove libtool archive

* Mon Dec 05 2011 Götz Waschk <waschk@mandriva.org> 2.0.23-1
+ Revision: 737732
- new version

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.22-2
+ Revision: 671969
- mass rebuild

* Sun Sep 12 2010 Götz Waschk <waschk@mandriva.org> 2.0.22-1mdv2011.0
+ Revision: 577663
- update to new version 2.0.22

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 2.0.21-1mdv2011.0
+ Revision: 550289
- new version

* Sun Nov 08 2009 Funda Wang <fwang@mandriva.org> 2.0.20-2mdv2010.1
+ Revision: 463102
- rebuild

* Sun Sep 27 2009 Funda Wang <fwang@mandriva.org> 2.0.20-1mdv2010.0
+ Revision: 449952
- use autoreconf
- fix file list

  + Götz Waschk <waschk@mandriva.org>
    - new version
    - new major
    - update source URL

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.18-2mdv2010.0
+ Revision: 413008
- rebuild

* Sun Dec 21 2008 Götz Waschk <waschk@mandriva.org> 2.0.18-1mdv2009.1
+ Revision: 317117
- update to new version 2.0.18

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.0.17-2mdv2009.0
+ Revision: 265681
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 2.0.17-1mdv2009.0
+ Revision: 216799
- New version 2.0.17

* Thu Jan 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.16-4mdv2008.1
+ Revision: 153934
- rebuild due to wrong tag

* Sun Jan 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.16-3mdv
+ Revision: 150944
- new license policy
- drop br on old automake-1.8

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 05 2007 Götz Waschk <waschk@mandriva.org> 2.0.16-2mdv2008.1
+ Revision: 106109
- new devel name


* Tue Feb 06 2007 Götz Waschk <waschk@mandriva.org> 2.0.16-1mdv2007.0
+ Revision: 116601
- new version

* Wed Dec 27 2006 Götz Waschk <waschk@mandriva.org> 2.0.15-2mdv2007.1
+ Revision: 102136
- rebuild
- new version

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 2.0.14-1mdv2007.1
+ Revision: 100505
- Import SDL_gfx

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 2.0.14-1mdv2007.1
- new major
- New version 2.0.14

* Tue Aug 01 2006 Götz Waschk <waschk@mandriva.org> 2.0.13-1mdv2007.0
- Rebuild

* Thu Jul 20 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.13-5mdv2007.0
- fix provides

* Tue May 16 2006 Stefan van der Eijk <stefan@eijk.nu> 2.0.13-4mdk
- rebuild for sparc

* Sun Jan 08 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.0.13-3mdk
- Rebuild

* Wed Dec 28 2005 Götz Waschk <waschk@mandriva.org> 2.0.13-2mdk
- Rebuild
- use mkrel

* Wed Dec 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.13-1mdk
- 2.0.13
- major 13

* Tue Nov 09 2004 G?tz Waschk <waschk@linux-mandrake.com> 2.0.12-1mdk
- drop patch
- major 12
- New release 2.0.12

* Sat Jun 05 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.11-3mdk
- auto* fix

* Thu May 20 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.11-2mdk
- fix typo breaking SDL-perl

* Wed May 19 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.11-1mdk
- fix source URL
- new major
- New release 2.0.11

