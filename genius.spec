Summary:	General tool for mathematics
Summary(pl):	Rozbudowane narz�dzie matematyczne
Name:		genius
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	95de70b99cedebef73a90123de84647e
Patch0:		%{name}-am.patch
Patch1:		%{name}-termcap.patch
Patch2:		%{name}-locale-names.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gmp-devel
BuildRequires:	gtksourceview-devel >= 0.3.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	popt-devel
BuildRequires:	vte-devel >= 0.8.19
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	shared-mime-info
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

mv po/{no,nb}.po

%build
rm -f missing acinclude.m4
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
update-mime-database %{_datadir}/mime

%postun
/sbin/ldconfig
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

%files devel
%defattr(644,root,root,755)
# Do we really need this la and so files?
%{_libdir}/genius/libtestplugin.so
%{_libdir}/genius/libtestplugin.la
%{_includedir}/genius
