Summary:	Genius advanced calculator
Name:		genius
Version:	0.4.2
Release:	2
Copyright:	GPL
Group:		X11/Applications
Source:		http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
URL:		http://www.5z.com/jirka/linux.html#genius
BuildPrereq:	gmp-devel
BuildPrereq:	gnome-libs-devel
BuildPrereq:	gtk+-devel
BuildPrereq:	imlib-devel
BuildPrereq:	ncurses-devel
BuildPrereq:	readline-devel
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.

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


%changelog
* Mon Jun 07 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [0.4.2-2]
- spec cleanup
- added find_lang macro

* Fri May  7 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.4.1-1]
- changed install prefix to /usr/X11R6,
- added BuildPrereq rules,
- added gzipping %doc,
- removed COPYING from %doc (copyright statment is in Copyright field),

* Tue Apr 20 1999 Erik Walthinsen <omega@cse.ogi.edu>
- added spec.in file, changes to makefiles as approrpiate
