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
URL:		http://konst.org.ua/centericq/
Obsoletes:	centerICQ
BuildRequires:	ncurses-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libsigc++-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
CPPFLAGS="-I%{_includedir}/ncurses"; export CPPFLAGS
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.1 \
   $RPM_BUILD_ROOT%{_mandir}/man1

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
