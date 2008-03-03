# TODO
# - WARNING: No GPG support in Jabber, since GPGME library not found or its setup not ok
Summary:	Console ncurses based IM (ICQ, Yahoo!, MSN, AIM, IRC) client
Summary(es.UTF-8):	CenterICQ es un cliente ICQ basado en ncurses para el modo texto
Summary(pl.UTF-8):	Klient IM (ICQ, Yahoo!, MSN, AIM, IRC) w wersji tekstowej
Summary(pt_BR.UTF-8):	O centerICQ é um cliente ICQ baseado em ncurses para o modo texto
Name:		centericq
Version:	4.21.0
Release:	8
License:	GPL
Group:		Applications/Communications
Source0:	http://konst.org.ua/download/%{name}-%{version}.tar.bz2
# Source0-md5:	82e426f2b4f6f2ab799c28807f36ade6
Patch0:		%{name}-no_libgnutls.patch
Patch1:		%{name}-icq-short-read.patch
Patch2:		%{name}-memory-handling.patch
Patch3:		%{name}-amd64jabber.patch
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
BuildRequires:	perl-base
Obsoletes:	centerICQ
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
CenterICQ to tekstowy, sterowany za pomocą menu i okien interfejs do
protokołów IM. Aktualnie obsługuje protokoły ICQ2000, Yahoo!, MSN, AIM
TOC oraz IRC. Pozwala na wysyłanie, odbiór oraz przesyłanie dalej
wiadomości, adresów i kontaktów, wysyłanie wielu wiadomości naraz,
przeglądanie informacji o innych użytkownikach, rejestrację nowego
UINu oraz uzupełnianie swoich informacji, informowanie o nadejściu
nowej poczty, włączanie automatycznego stanu Away po wybranym czasie
nieaktywności (na dowolnej konsoli!), posiadanie własnej listy osób
ignorowanych. Może także powiązać zdarzenia z dźwiękami.

%description -l pt_BR.UTF-8
O centerICQ é um cliente ICQ baseado em ncurses para o modo texto.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/{zh_TW.Big5,zh_TW}.po
%{__sed} -i -e 's/zh_TW\.Big5/zh_TW/' configure.in

%build
install /usr/share/gettext/config.rpath .
%{__aclocal}
%{__autoconf}
%{__automake}
for i in kkstrtext-0.1 kksystr-0.1 kkconsui-0.1 libyahoo2-0.1 \
	libicq2000-0.1 firetalk-0.1 libjabber-0.1 connwrap-0.1 \
	libgadu-0.1 libmsn-0.1; do
	cd $i
	install /usr/share/gettext/config.rpath .
	%{__aclocal}
	%{__autoconf}
	%{__automake}
	cd -
done

%{__sed} -i -e 's,@MKINSTALLDIRS@,/usr/share/automake/mkinstalldirs,' src/hooks/Makefile.in src/Makefile.in misc/Makefile.in share/Makefile.in Makefile.in
%{__sed} -i -e 's,@MKINSTALLDIRS@,/usr/share/automake/mkinstalldirs,' po/Makefile.in.in intl/Makefile.in

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
