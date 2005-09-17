Summary:	General tool for mathematics
Summary(pl):	Rozbudowane narz�dzie matematyczne
Name:		genius
Version:	0.7.2
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	69944ec93ad62cc4c3dc4ba35d4c2944
Patch0:		%{name}-am.patch
Patch1:		%{name}-termcap.patch
Patch2:		%{name}-locale-names.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-term_mpfr_fix.patch
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
BuildRequires:	libmpfr-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	scrollkeeper
BuildRequires:	vte-devel >= 0.8.19
Requires(post,postun):	/sbin/ldconfig
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

%description -l pl
Genius to narz�dzie do rozwi�zywania problem�w matematycznych.
Zawiera ono matematyczny j�zyk programowania, narz�dzie do geometrii
euklidesowej, narz�dzie do generowania wykres�w 2D/3D oraz konsolowy
kalkulator. Kalkulator obs�uguje liczby zmiennoprzecinkowe wysokiej
precyzji, liczby ca�kowite, zespolone oraz macierze.

%package devel
Summary:	genius header files
Summary(pl):	Pliki nag��wkowe genius
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Genius header files.

%description devel -l pl
Pliki nag��wkowe genius.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv po/{no,nb}.po

%build
rm -f missing acinclude.m4
gnome-doc-common
cp xmldocs.make help
%{__libtoolize}
glib-gettextize --copy --force
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
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


# This files are autogenerated
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/{XMLnamespaces,globs,magic}

%find_lang %{name} --with-gnome --all-name

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update
update-mime-database %{_datadir}/mime ||:

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update
update-mime-database %{_datadir}/mime

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
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
%{_datadir}/mime/packages/*
%{_datadir}/mime/text/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/*.png
%{_omf_dest_dir}/%{name}

%files devel
%defattr(644,root,root,755)
# Do we really need this la and so files?
%{_libdir}/genius/libtestplugin.so
%{_libdir}/genius/libtestplugin.la
%{_includedir}/genius
