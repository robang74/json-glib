Name:           json-glib
Version:        1.4.4
Release:        1
Summary:        Library for JavaScript Object Notation format
License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/JsonGlib
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  gettext

%description
JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

%package -n libjson-glib
Summary:        Library for JavaScript Object Notation format
Provides:       %{name} = %{version}

%description -n libjson-glib
JSON is a lightweight data-interchange format. It is comparatively
easy for humans to read and write, and for machines to parse and generate.

JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

%package devel
Summary:        Development files for libjson-glib
Requires:       libjson-glib = %{version}

%description devel
JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

This package contains development files needed to develop with the
json-glib library.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%meson 
%meson_build

%install
%meson_install
%find_lang %{name}-1.0

%post -n libjson-glib -p /sbin/ldconfig
%postun -n libjson-glib -p /sbin/ldconfig

%files -n libjson-glib -f %{name}-1.0.lang
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc NEWS README.md
%{_bindir}/json-glib-format
%{_bindir}/json-glib-validate
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/installed-tests
%dir %{_libexecdir}/installed-tests
%{_datadir}/installed-tests/json-glib-1.0/
%{_libexecdir}/installed-tests/json-glib-1.0/
%{_libdir}/girepository-1.0/Json-1.0.typelib
