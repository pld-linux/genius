Summary:	Genius advanced calculator
Name:		genius
Version:	0.4.1
Release:	1
Copyright:	GPL
Group:		X11/Applications
Source:		http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
URL:		http://www.5z.com/jirka/linux.html#genius
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--enable-gnome \
	--without-included-gettext
make

gzip -9nf README AUTHORS NEWS TODO ChangeLog

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/share/genius
/usr/X11R6/share/apps/Utilities/*

%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/genius.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/genius.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/genius.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/genius.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/genius.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/genius.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/genius.mo
%lang(ga) /usr/X11R6/share/locale/ga/LC_MESSAGES/genius.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/genius.mo

%changelog
* Fri May  7 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.4.1-1]
- changed install prefix to /usr/X11R6,
- removed COPYING from %doc (copyright statment is in Copyright field),

* Tue Apr 20 1999 Erik Walthinsen <omega@cse.ogi.edu>
- added spec.in file, changes to makefiles as approrpiate
