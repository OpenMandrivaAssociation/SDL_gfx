%define major 16
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	SDL graphics drawing primitives and other support functions
Name:		SDL_gfx
Version:	2.0.26
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/index.html
Source0:	http://www.ferzkopp.net/Software/SDL_gfx-2.0/%{name}-%{version}.tar.gz
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)

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

%package -n %{devname}
Summary:	Header files and more to develop SDL_gfx applications
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Header files and more to develop SDL_gfx applications.

%prep
%setup -q

%build
autoreconf -fvi
%configure \
	--disable-static \
	--disable-mmx
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libSDL_gfx.so.%{major}*

%files -n %{devname}
%doc README ChangeLog AUTHORS Docs
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

