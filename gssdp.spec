%define name gssdp
%define version 0.4.2
%define release %mkrel 1
%define major 0
%define libname %mklibname %{name}  %{major}
%define develname %mklibname %{name} -d

Summary: Implements resource discovery and announcement over SSDP
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://www.gupnp.org/sources/gssdp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libsoup-2.2-devel
BuildRequires: libglade2-devel

%description
GSSDP implements resource discovery and announcement over SSDP

%package -n %{libname}

Summary:        Main library for gssdp
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gssdp.

%package -n     %{develname}
Summary:        Headers for developing programs that will use gssdp
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use gssdp

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%prep
%setup -q
%configure

%build
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/gssdp-device-sniffer

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/gssdp*.pc
%{_includedir}/gssdp-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_datadir}/%{name}/*glade
%{_datadir}/gtk-doc/html/*

