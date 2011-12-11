%define api 1.0
%define major 3
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	Implements resource discovery and announcement over SSDP
Name:		gssdp
Version:	0.12.1
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gssdp/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
BuildRequires:	libsoup-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gobject-introspection-devel

%description
GSSDP implements resource discovery and announcement over SSDP.

%package -n %{libname}
Summary:	Main library for gssdp
Group:		System/Libraries
Obsoletes:	%{mklibname gssdp 1} < 0.6.1
Obsoletes:	%{mklibname gssdp 2} < 0.10.0
Conflicts: gir-repository < 0.6.5-11
Conflicts: %mklibname %{name} %{api} 2

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gssdp.

%package -n %{develname}
Summary:	Headers for developing programs that will use gssdp
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts: gir-repository < 0.6.5-11

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use gssdp.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' | xargs rm

%files
%doc AUTHORS README ChangeLog NEWS
%{_bindir}/gssdp-device-sniffer
%{_datadir}/%{name}/*.ui

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%_libdir/girepository-1.0/GSSDP-1.0.typelib

%files -n %{develname}
%{_libdir}/pkgconfig/gssdp*.pc
%{_includedir}/gssdp-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/*
%_datadir/gir-1.0/GSSDP-1.0.gir
