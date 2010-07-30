%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Implements resource discovery and announcement over SSDP
Name:		gssdp
Version:	0.7.2
Release:	%mkrel 2
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gssdp/
Source0:	http://www.gupnp.org/sources/gssdp/%{name}-%{version}.tar.gz
BuildRequires:	libsoup-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gobject-introspection-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GSSDP implements resource discovery and announcement over SSDP.

%package -n %{libname}
Summary:	Main library for gssdp
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname gssdp 1} < 0.6.1
Conflicts: gir-repository < 0.6.5-11

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
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS
%{_bindir}/gssdp-device-sniffer
%{_datadir}/%{name}/*.ui

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
%_libdir/girepository-1.0/GSSDP-1.0.typelib

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/pkgconfig/gssdp*.pc
%{_includedir}/gssdp-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_datadir}/gtk-doc/html/*
%_datadir/gir-1.0/GSSDP-1.0.gir
