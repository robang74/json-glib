Name:           json-glib
Summary:        Library for JavaScript Object Notation format
Version:        1.6.0
Release:        1
License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/JsonGlib
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  meson >= 0.52.0
BuildRequires:  gettext
BuildRequires:  python3-base
BuildRequires:  pkgconfig(gio-2.0) >= 2.54.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.54.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
Obsoletes:      libjson-glib
Conflicts:      libjson-glib

%description
JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

This package contains development files needed to develop with the
json-glib library.

%package tests
Summary:        Tests for the %{name} package
Requires:       %{name} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify the
functionality of the installed %{name} package.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%meson -Dgtk_doc=disabled -Dman=false
%meson_build

%install
%meson_install
%find_lang %{name}-1.0

%check
%meson_test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc NEWS README.md
%{_bindir}/json-glib-format
%{_bindir}/json-glib-validate
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_libdir}/girepository-1.0/Json-1.0.typelib

%files tests
%defattr(-,root,root,-)
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/
