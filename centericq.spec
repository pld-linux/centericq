Summary:	Console ncurses based IM (ICQ, Yahoo!, MSN, AIM, IRC) client
Summary(es):	CenterICQ es un cliente ICQ basado en ncurses para el modo texto
Summary(pl):	Klient IM (ICQ, Yahoo!, MSN, AIM, IRC) w wersji tekstowej
Summary(pt_BR):	O centerICQ é um cliente ICQ baseado em ncurses para o modo texto
Name:		centericq
Version:	4.21.0
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://konst.org.ua/download/%{name}-%{version}.tar.bz2
# Source0-md5:	82e426f2b4f6f2ab799c28807f36ade6
Patch0:		%{name}-no_libgnutls.patch
Patch1:		%{name}-icq-short-read.patch
Patch2:		%{name}-memory-handling.patch
URL:		http://thekonst.net/centericq/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	libsigc++1-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
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

%description -l pl
CenterICQ to tekstowy, sterowany za pomoc± menu i okien interfejs do
protoko³ów IM. Aktualnie obs³uguje protoko³y ICQ2000, Yahoo!, MSN, AIM
TOC oraz IRC. Pozwala na wysy³anie, odbiór oraz przesy³anie dalej
wiadomo¶ci, adresów i kontaktów, wysy³anie wielu wiadomo¶ci naraz,
przegl±danie informacji o innych u¿ytkownikach, rejestracjê nowego
UINu oraz uzupe³nianie swoich informacji, informowanie o nadej¶ciu
nowej poczty, w³±czanie automatycznego stanu Away po wybranym czasie
nieaktywno¶ci (na dowolnej konsoli!), posiadanie w³asnej listy osób
ignorowanych. Mo¿e tak¿e powi±zaæ zdarzenia z d¼wiêkami.

%description -l pt_BR
O centerICQ é um cliente ICQ baseado em ncurses para o modo texto.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv -f po/{zh_TW.Big5,zh_TW}.po
%{__perl} -pi -e 's/zh_TW\.Big5/zh_TW/' configure.in

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
for i in kkstrtext-0.1 kksystr-0.1 kkconsui-0.1 libyahoo2-0.1 \
	libicq2000-0.1 firetalk-0.1 libjabber-0.1 connwrap-0.1 \
	libgadu-0.1 libmsn-0.1; do
	cd $i
	%{__aclocal}
	%{__autoconf}
	%{__automake}
	cd ..
done
CXXFLAGS="-I/usr/include/ncurses %{rpmcflags}"
%configure \
	--with-openssl
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
%doc AUTHORS README ChangeLog FAQ TODO THANKS NEWS INSTALL
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.wav
%{_mandir}/man?/*
