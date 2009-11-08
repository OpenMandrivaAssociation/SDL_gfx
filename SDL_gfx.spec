%define	major 13
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s

Summary:	SDL graphics drawing primitives and other support functions
Name:		SDL_gfx
Version:	2.0.20
Release:	%mkrel 2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/index.html
Source0:	http://www.ferzkopp.net/Software/SDL_gfx-2.0/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
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
Obsoletes:	%mklibname %{name} 0 -d

%description -n %{develname}
Header files and more to develop SDL_gfx applications.

%package -n %{staticname}
Summary:	Static SDL_gfx libraries
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%mklibname %{name} 0 -d -s

%description -n	%{staticname}
Static SDL_gfx libraries.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x --disable-mmx
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README ChangeLog AUTHORS Docs
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/lib*.a
