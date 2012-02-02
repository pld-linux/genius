# TODO: where is "euclidian geometry tool"? Maybe drgeo-obsolotes is false
Summary:	General tool for mathematics
Summary(pl.UTF-8):	Rozbudowane narzędzie matematyczne
Name:		genius
Version:	1.0.14
Release:	3
License:	GPL v3+
Group:		Applications/Math
Source0:	http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.xz
# Source0-md5:	6b4dd6a7b7ad893e76c8653e332e8ad6
Patch0:		%{name}-desktop.patch
URL:		http://www.jirka.org/genius.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtksourceview2-devel >= 2.0.2
BuildRequires:	intltool >= 0.21
BuildRequires:	libtool
BuildRequires:	mpfr-devel >= 2.2.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	vte0-devel >= 0.8.19
BuildRequires:	xz >= 1:4.999.7
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
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

%description devel
Genius header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe genius.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e 's#sr\@Latn#sr\@latin#' configure.in
%{__sed} -i 's@AM_BINRELOC@#AM_BINRELOC@' configure.in
mv po/sr\@{Latn,latin}.po

%build
rm -f acinclude.m4
%{__gnome_doc_common}
cp xmldocs.make help
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

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post
%update_mime_database
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/genius
%attr(755,root,root) %{_bindir}/gnome-genius
%dir %{_libdir}/genius
%attr(755,root,root) %{_libdir}/genius-readline-helper-fifo
%{_datadir}/genius
%{_datadir}/mime/packages/genius.xml
%{_desktopdir}/gnome-genius.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/genius
