Summary:	General tool for mathematics
Summary(pl.UTF-8):	Rozbudowane narzędzie matematyczne
Name:		genius
Version:	1.0.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
# Source0-md5:	8c17ac90dab4f586e07627b6148c39b6
Patch0:		%{name}-termcap.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-link.patch
URL:		http://www.jirka.org/genius.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gmp-devel
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gtksourceview-devel >= 0.3.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	mpfr-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	vte-devel >= 0.8.19
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Obsoletes:	drgenius
Obsoletes:	drgeo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genius is a general tool for mathematics, including a mathematical
programming language and evaluator, an euclidian geometry tool, a
2D/3D function grapher and a console calculator. The console
calculator handles multiple precision floating point numbers, infinite
precision integers, complex numbers and matrixes.

%description -l pl.UTF-8
Genius to narzędzie do rozwiązywania problemów matematycznych.
Zawiera ono matematyczny język programowania, narzędzie do geometrii
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
%patch1 -p1
%patch2 -p1

%build
rm -f missing acinclude.m4
gnome-doc-common
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
	--enable-gnome

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Thess files are autogenerated
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/{XMLnamespaces,aliases,globs,magic,mime.cache,subclasses}
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime/text

# Obsoleted GNOME mime-info stuff
rm -rf $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_mime_database
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor
%scrollkeeper_update_postun
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
%{_iconsdir}/hicolor/*/apps/gnome-genius.png
%{_omf_dest_dir}/%{name}

%files devel
%defattr(644,root,root,755)
# Do we really need this la and so files?
%attr(755,root,root) %{_libdir}/genius/libtestplugin.so
%{_libdir}/genius/libtestplugin.la
%{_includedir}/genius
