%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	3
%define libname	%mklibname %{name} %{api} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname %{name} -d

Summary:	Implements resource discovery and announcement over SSDP
Name:		gssdp
Version:	0.14.6
Release:	2
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gssdp/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:  vala-tools

%description
GSSDP implements resource discovery and announcement over SSDP.

%package -n %{libname}
Summary:	Main library for gssdp
Group:		System/Libraries
Obsoletes:	%{mklibname gssdp 2} < 0.10.0
Conflicts:	%mklibname %{name} %{api} 2

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gssdp.

%package -n %{girname}
Summary:	GObject Introspection interface description for GSSDP
Group:		System/Libraries
Conflicts:	%{_lib}gssdp1.0_3 < 0.12.1-2

%description -n %{girname}
GObject Introspection interface description for GSSDP.

%package -n %{devname}
Summary:	Headers for developing programs that will use gssdp
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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
%makeinstall_std

%files
%doc AUTHORS README ChangeLog NEWS
%{_bindir}/gssdp-device-sniffer
%{_datadir}/%{name}/*.ui

%files -n %{libname}
%{_libdir}/libgssdp-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GSSDP-%{api}.typelib

%files -n %{devname}
%{_includedir}/gssdp-%{api}/lib%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/gssdp*.pc
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/GSSDP-%{api}.gir
%{_datadir}/vala/vapi/*

