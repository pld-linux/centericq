Summary:	Text mode ICQ client
Summary(pl):	Klient ICQ w wersji tekstowej
Name:		centericq
Version:	4.5.0
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://konst.org.ua/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
URL:		http://konst.org.ua/centericq/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libsigc++-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	centerICQ

%description
CenterICQ is a text mode menu- and window-driven ICQ interface. It
allows you to send, receive and forward messages, URLs and contacts,
mass message send, search for users, view users' details, maintain
your contact list directly from the program, view messages history,
register a new UIN and update your details, be informed on receiving
e-mail messages, automatically set away after the defined period of
inactivity (on any console!), and have your own ignore list. It can
also associate events with sounds.

%description -l pl
CenterICQ to tekstowy, sterowany za pomoc± menu i okien interfejs do
ICQ. Pozwala na wysy³anie, odbiór oraz przesy³anie dalej wiadomo¶ci,
adresów i kontaktów, wysy³anie wielu wiadomo¶ci na raz, przegl±danie
informacji o innych u¿ytkownikach, rejestracjê nowego UINu oraz
uzupe³nianie swoich informacji, informowanie o nadej¶ciu nowej poczty,
w³±czanie automatycznego stanu Away po wybranym czasie nieaktywno¶ci
(na dowolnej konsoli!), posiadanie w³asnej listy osób ignorowanych.
Mo¿e tak¿e powi±zaæ zdarzenia z d¼wiêkami.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
for i in kkstrtext-0.1 kksystr-0.1 kkconsui-0.1 libyahoo-0.1 libmsn-0.1\
	libicq2000-0.2; do
	cd $i
	rm -f missing
	aclocal
	autoconf
	automake -a -c
	cd ..
done
CXXFLAGS="-I%{_includedir}/ncurses %{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog FAQ TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
