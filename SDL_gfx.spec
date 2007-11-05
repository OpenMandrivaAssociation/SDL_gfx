%define	name	SDL_gfx
%define	version	2.0.16
%define	release %mkrel 2
%define	major 0
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname -d %name
%define staticname %mklibname -d -s %name

Summary:	SDL graphics drawing primitives and other support functions
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
Source0:	http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/%{name}-%{version}.tar.bz2
URL:		http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/index.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	automake1.8
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The SDL_gfx library evolved out of the SDL_gfxPrimitives code.

The current components of the SDL_gfx library are:
- Graphic Primitives (SDL_gfxPrimitves.h)
- Rotozoomer (SDL_rotozoom.h)
- Framerate control (SDL_framerate.h)
- MMX image filters (SDL_imageFilter.h)

The library is backwards compatible to the above mentioned code. It's
is written in plain C and can be used in C++ code.

%package -n	%{libname}
Summary:	SDL graphics drawing primitives and other support functions
Group:		System/Libraries

%description -n	%{libname}
The SDL_gfx library evolved out of the SDL_gfxPrimitives code.

The current components of the SDL_gfx library are:
- Graphic Primitives (SDL_gfxPrimitves.h)
- Rotozoomer (SDL_rotozoom.h)
- Framerate control (SDL_framerate.h)
- MMX image filters (SDL_imageFilter.h)

The library is backwards compatible to the above mentioned code. It's
is written in plain C and can be used in C++ code.

%package -n	%develname
Summary:	Header files and more to develop SDL_gfx applications
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	SDL-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %version-%release
Obsoletes: %mklibname -d %name 0

%description -n	%develname
Header files and more to develop SDL_gfx applications.

%package -n	%staticname
Summary:	Static SDL_gfx libraries
Group:		Development/C
Requires:	%develname = %{version}-%{release}
Obsoletes: %mklibname -d -s %name 0

%description -n	%staticname
Static SDL_gfx libraries.

%prep
%setup -q

%build
rm -f missing acinclude.m4 configure
libtoolize --force
aclocal-1.8
automake-1.8 -a
autoconf

%configure2_5x --disable-mmx
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc README ChangeLog AUTHORS Docs
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files -n %staticname
%defattr(-,root,root)
%{_libdir}/lib*.a


