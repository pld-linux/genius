# TODO: where is "euclidian geometry tool"? Maybe drgeo-obsoletes is false
Summary:	General tool for mathematics
Summary(pl.UTF-8):	Rozbudowane narzędzie matematyczne
Name:		genius
Version:	1.0.23
Release:	1
License:	GPL v3+
Group:		Applications/Math
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/genius/1.0/%{name}-%{version}.tar.xz
# Source0-md5:	7fa8a2850b3245acd1b1d6514f2eb9e1
URL:		http://www.jirka.org/genius.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gmp-devel >= 2.3.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtksourceview2-devel >= 2.0.2
BuildRequires:	intltool >= 0.21
BuildRequires:	libtool
BuildRequires:	mpfr-devel >= 2.3.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	vte0-devel >= 0.26.0
BuildRequires:	xz >= 1:4.999.7
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	glib2 >= 1:2.16.0
Requires:	gmp >= 2.3.0
Requires:	gtk+2 >= 2:2.18.0
Requires:	gtksourceview2 >= 2.0.2
Requires:	mpfr >= 2.3.0
Requires:	vte0 >= 0.26.0
Obsoletes:	drgenius
Obsoletes:	drgeo
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genius is a general tool for mathematics, including a mathematical
programming language and evaluator, an euclidian geometry tool, a
2D/3D function grapher and a console calculator. The console
calculator handles multiple precision floating point numbers, infinite
precision integers, complex numbers and matrixes.

%description -l pl.UTF-8
Genius to narzędzie do rozwiązywania problemów matematycznych. Zawiera
ono matematyczny język programowania, narzędzie do geometrii
euklidesowej, narzędzie do generowania wykresów 2D/3D oraz konsolowy
kalkulator. Kalkulator obsługuje liczby zmiennoprzecinkowe wysokiej
precyzji, liczby całkowite, zespolone oraz macierze.

%package devel
Summary:	genius header files
Summary(pl.UTF-8):	Pliki nagłówkowe genius
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.16.0
Requires:	gmp-devel >= 2.3.0
Requires:	mpfr-devel >= 2.3.0

%description devel
Genius header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe genius.

%prep
%setup -q

%{__sed} -i 's@AM_BINRELOC@#AM_BINRELOC@' configure.ac

%build
%{__rm} acinclude.m4
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--enable-gtksourceview \
	--enable-gnome \
	--disable-update-mimedb

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Obsoleted GNOME mime-info stuff
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/genius/libtestplugin.{so,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/genius
%attr(755,root,root) %{_bindir}/gnome-genius
%dir %{_libdir}/genius
%attr(755,root,root) %{_libdir}/genius-readline-helper-fifo
%dir %{_datadir}/genius
%{_datadir}/genius/examples
%{_datadir}/genius/gel
%{_datadir}/genius/genius-graph.png
%{_datadir}/genius/genius.txt
%{_datadir}/genius/gtksourceview
%dir %{_datadir}/genius/help
%{_datadir}/genius/help/C
%lang(cs) %{_datadir}/genius/help/cs
%lang(de) %{_datadir}/genius/help/de
%lang(el) %{_datadir}/genius/help/el
%lang(es) %{_datadir}/genius/help/es
%lang(fr) %{_datadir}/genius/help/fr
%lang(pt_BR) %{_datadir}/genius/help/pt_BR
%lang(ru) %{_datadir}/genius/help/ru
%lang(sv) %{_datadir}/genius/help/sv
%{_datadir}/genius/plugins
%{_datadir}/mime/packages/genius.xml
%{_desktopdir}/gnome-genius.desktop
%{_iconsdir}/hicolor/*x*/apps/genius-stock-plot.png
%{_iconsdir}/hicolor/*x*/apps/gnome-genius.png
%{_iconsdir}/hicolor/scalable/apps/gnome-genius.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/genius
