%define api 1.0
%define major 3
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define develname %mklibname %{name} -d

Summary:	Implements resource discovery and announcement over SSDP
Name:		gssdp
Version:	0.12.2
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gupnp.org/sources/gssdp/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	libsoup-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gobject-introspection-devel

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
Conflicts:	gir-repository < 0.6.5-11
Conflicts:	%{_lib}gssdp1.0_3 < 0.12.1-2

%description -n %{girname}
GObject Introspection interface description for GSSDP.

%package -n %{develname}
Summary:	Headers for developing programs that will use gssdp
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	gir-repository < 0.6.5-11

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
%makeinstall_std
find %{buildroot} -name '*.la' | xargs rm -f

%files
%doc AUTHORS README ChangeLog NEWS
%{_bindir}/gssdp-device-sniffer
%{_datadir}/%{name}/*.ui

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GSSDP-%{api}.typelib

%files -n %{develname}
%{_includedir}/gssdp-%{api}/lib%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/gssdp*.pc
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/GSSDP-%{api}.gir



%changelog
* Fri Apr 15 2011 Funda Wang <fwang@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 653168
- new version 0.10.0

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 0.7.2-4
+ Revision: 650928
- rebuild for updated libsoup libtool archive

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 0.7.2-3mdv2011.0
+ Revision: 577923
- rebuild for new g-i

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.7.2-2mdv2011.0
+ Revision: 563303
- rebuild for new gobject-introspection

* Mon Apr 12 2010 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2010.1
+ Revision: 533727
- new version
- add introspection support

* Mon Jan 18 2010 Funda Wang <fwang@mandriva.org> 0.7.1-2mdv2010.1
+ Revision: 492939
- add BRs

* Fri Dec 04 2009 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 473524
- update to new version 0.7.1

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-1mdv2010.0
+ Revision: 445305
- Update to new version 0.7.0 (new major)
- Use gtkbuilder instead of glade now
- Package ui file in gssdp package instead of devel package

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6.4-2mdv2010.0
+ Revision: 425051
- rebuild

* Thu Mar 05 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.4-1mdv2009.1
+ Revision: 349315
- New version 0.6.4
- drop P1 (fixed upstream)

* Thu Jan 08 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.3-1mdv2009.1
+ Revision: 327272
- New version 0.6.3
- diff P0 to fix str fmt

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 0.6.2-2mdv2009.1
+ Revision: 309154
- rebuild to get rid of libtasn1 dep

* Mon Sep 01 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.2-1mdv2009.0
+ Revision: 278581
- update to new version 0.6.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-1mdv2009.0
+ Revision: 210590
- new version
- bump major
- do not re-define stuff
- update buildrequires
- spec file clean

  + Erwan Velu <erwan@mandriva.org>
    - Fixing stupid buildrequires

* Mon Feb 25 2008 Erwan Velu <erwan@mandriva.org> 0.4.2-1mdv2008.1
+ Revision: 174550
- Fixing wrong requires
- Adding glade dep
- import gssdp


