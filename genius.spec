Summary:	General tool for mathematics
Summary(pl):	Rozbudowane narzêdzie matematyczne
Name:		genius
Version:	0.5.7.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/genius/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	9e2954d8c3c1a9cd3cee39d25c74eb32
Patch0:		%{name}-am.patch
Patch1:		%{name}-termcap.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gmp-devel
BuildRequires:	gtksourceview-devel >= 0.3.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	vte-devel >= 0.8.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genius is a general tool for mathematics, including a mathematical
programming language and evaluator, an euclidian geometry tool, a
2D/3D function grapher and a console calculator. The console
calculator handles multiple precision floating point numbers, infinite
precision integers, complex numbers and matrixes.

%description -l pl
Genius to narzêdzie do rozwi±zywania problemów matematycznych.
Zawiera ono matematyczny jêzyk programowania, narzêdzie do geometrii
euklidesowej, narzêdzie do generowania wykresów 2D/3D oraz konsolowy
kalkulator. Kalkulator obs³uguje liczby zmiennoprzecinkowe wysokiej
precyzji, liczby ca³kowite, zespolone oraz macierze.

%package devel
Summary:	genius header files
Summary(pl):	Pliki nag³ówkowe genius
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Genius header files.

%description devel -l pl
Pliki nag³ówkowe genius.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %dir %{_libdir}/genius
%attr(755,root,root) %{_libdir}/genius/libtestplugin.so.*.*.*
%attr(755,root,root) %{_libdir}/genius-readline-helper-fifo
%{_datadir}/genius
%{_desktopdir}/*.desktop

%files devel
%defattr(644,root,root,755)
# Do we really need this la and so files?
%{_libdir}/genius/libtestplugin.so
%{_libdir}/genius/libtestplugin.la
%{_includedir}/genius
