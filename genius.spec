Summary:	Genius advanced calculator
Summary(pl):	Zaawansowany kalkulator Genius
Name:		genius
Version:	0.4.2
Release:	2
Copyright:	GPL
Group:		X11/Applications
Source:		http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
URL:		http://www.5z.com/jirka/linux.html#genius
BuildRequires:	gmp-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6

%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.

%description -l pl
Genius jest zaawansowanym kalkulatorem i jêzykiem programowania matematycznego.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
%configure \
	--enable-gnome \
	--without-included-gettext
make

gzip -9nf README AUTHORS NEWS TODO ChangeLog

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	datadir=$RPM_BUILD_ROOT/%{_datadir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/share/genius
/usr/X11R6/share/apps/Utilities/*
