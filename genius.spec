Summary:	Genius advanced calculator
Summary(pl):	Zaawansowany kalkulator Genius
Name:		genius
Version:	0.4.6
Release:	6
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
Patch0:		%{name}-applnk.patch
Patch1:		%{name}-termlib.patch
URL:		http://www.5z.com/jirka/genius.html
BuildRequires:	gmp-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Genius is an advanced calculator and a mathematical programming
language. It handles multiple precision floating point numbers,
infinite precision integers, complex numbers and matrixes.

%description -l pl
Genius jest zaawansowanym kalkulatorem i jêzykiem programowania
matematycznego. Mo¿na go u¿yæ do obliczeñ wykorzystuj±cych liczby
zmiennoprzecinkowe, liczby ca³kowite o nieskoñczonej precyzji, liczby
zespolone oraz macierze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
automake
gettextize --copy --force
CFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS} -I/usr/include/ncurses"
%configure \
	--enable-gnome \
	--disable-static \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS NEWS TODO ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/genius/*
%{_datadir}/genius
%{_applnkdir}/Utilities/*
