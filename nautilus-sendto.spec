Summary:	Nautilus context menu for sending files
Name:		nautilus-sendto
Version:	3.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus-sendto/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	d0d2464b5d200ec914e127640c316ecb
URL:		http://www.es.gnome.org/~telemaco/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nautilus-sendto provides a Nautilus context menu for sending
files via other desktop applications.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g'		\
    configure.in

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ug}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.*

