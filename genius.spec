Summary:	Genius advanced calculator
Summary(pl):	Zaawansowany kalkulator Genius
Name:		genius
Version:	0.4.6
Release:	2
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source:		http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
Patch0:		genius-applnk.patch
Patch1:		genius-termlib.patch
URL:		http://www.5z.com/jirka/genius.html
BuildRequires:	gmp-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	XFree86-devel
BuildRequires:	gettext-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_applnkdir	%{_datadir}/applnk

%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.

%description -l pl
Genius jest zaawansowanym kalkulatorem i jêzykiem programowania
matematycznego.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
automake
gettextize --copy --force
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure \
	--enable-gnome \
	--disable-static \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/genius/lib*so

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
