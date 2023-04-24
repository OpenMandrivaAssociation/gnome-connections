# Exclude private libraries from autogenerated provides and requires
%global __provides_exclude_from ^%{_libdir}/gnome-connections/
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/gnome-connections/ -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
 
%global tarball_version %%(echo %{version} | tr '~' '.')
%global url_ver %%(echo %{version} | cut -d. -f1)
 
Name:       gnome-connections
Version:    44.1
Release:    1
Summary:    A remote desktop client for the GNOME desktop environment

License:    GPLv3+
URL:        https://gitlab.gnome.org/gnome/connections/-/wikis/home
Source0:    https://download.gnome.org/sources/gnome-connections/%{url_ver}/gnome-connections-%{tarball_version}.tar.xz
 
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  appstream-util
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  gtk-update-icon-cache
BuildRequires:  pkgconfig(gtk-vnc-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-1)
 
Requires:       hicolor-icon-theme

Provides:       connections = %{version}-%{release}
 
%description
Gnome-Connections is a remote desktop client for the GNOME desktop environment.
 
%prep
%autosetup -p1 -n gnome-connections-%{tarball_version}
 
%build
%meson
%meson_build

%install
%meson_install

%find_lang gnome-connections --with-gnome
 
# Remove unneeded development files
rm -rf %{buildroot}%{_includedir}/gnome-connections/
rm -rf %{buildroot}%{_libdir}/gnome-connections/girepository-1.0/
rm -rf %{buildroot}%{_libdir}/gnome-connections/pkgconfig/
rm -rf %{buildroot}%{_datadir}/gnome-connections/gir-1.0/
rm -rf %{buildroot}%{_datadir}/gnome-connections/vapi/

 
%files -f gnome-connections.lang
%license COPYING
%doc README.md NEWS
%{_bindir}/gnome-connections
%{_libdir}/gnome-connections/
%{_datadir}/metainfo/org.gnome.Connections.appdata.xml
%{_datadir}/applications/org.gnome.Connections.desktop
%{_datadir}/dbus-1/services/org.gnome.Connections.service
%{_datadir}/glib-2.0/schemas/org.gnome.Connections.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Connections.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Connections-symbolic.svg
%{_datadir}/mime/packages/org.gnome.Connections.xml
