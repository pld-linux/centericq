Summary:	Console ncurses based IM (ICQ, Yahoo!, MSN, AIM, IRC) client
Summary(es):	CenterICQ es un cliente ICQ basado en ncurses para el modo texto
Summary(pl):	Klient IM (ICQ, Yahoo!, MSN, AIM, IRC) w wersji tekstowej
Summary(pt_BR):	O centerICQ é um cliente ICQ baseado em ncurses para o modo texto
Name:		centericq
Version:	4.7.5
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://konst.org.ua/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-acfix.patch
URL:		http://konst.org.ua/centericq/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigc++-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	centerICQ

%description
centericq is a text mode menu- and window-driven IM interface.
Currently ICQ2000, Yahoo!, MSN, AIM TOC and IRC protocols are
supported. It allows you to send, receive, and forward messages, URLs
and, SMSes, mass message send, search for users (including extended
"whitepages search"), view users' details, maintain your contact list
directly from the program (including non-icq contacts), view the
messages history, register a new UIN and update your details, be
informed on receiving email messages, automatically set away after the
defined period of inactivity (on any console), and have your own
ignore, visible and invisible lists. It can also associate events with
sounds, has support for Hebrew and Arabic languages and allows to
arrange contacts into groups.

%description -l es
CenterICQ es un cliente ICQ basado en ncurses para el modo texto.

%description -l pl
CenterICQ to tekstowy, sterowany za pomoc± menu i okien interfejs do
protoko³ów IM. Aktualnie obs³uguje protoko³y ICQ2000, Yahoo!, MSN, AIM
TOC oraz IRC. Pozwala na wysy³anie, odbiór oraz przesy³anie dalej
wiadomo¶ci, adresów i kontaktów, wysy³anie wielu wiadomo¶ci na raz,
przegl±danie informacji o innych u¿ytkownikach, rejestracjê nowego
UINu oraz uzupe³nianie swoich informacji, informowanie o nadej¶ciu
nowej poczty, w³±czanie automatycznego stanu Away po wybranym czasie
nieaktywno¶ci (na dowolnej konsoli!), posiadanie w³asnej listy osób
ignorowanych. Mo¿e tak¿e powi±zaæ zdarzenia z d¼wiêkami.

%description -l pt_BR
O centerICQ é um cliente ICQ baseado em ncurses para o modo texto.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
for i in kkstrtext-0.1 kksystr-0.1 kkconsui-0.1 libyahoo-0.1 libmsn-0.1\
	libicq2000-0.6 firetalk-0.1; do
	cd $i
	rm -f missing
	aclocal
	%{__autoconf}
	%{__automake}
	cd ..
done
CXXFLAGS="-I%{_includedir}/ncurses %{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog FAQ TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*.wav
%{_mandir}/man?/*
