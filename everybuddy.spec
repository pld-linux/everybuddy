Summary:	A Universal Instant Messanging Client 
Summary(pl):	Uniwersalny Klient Natychmiastowych Wiadomo¶ci
Summary(pt_BR):	Um cliente universal para mensagens instantâneas
Name:		everybuddy
Version:	0.2.1beta6
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://www.everybuddy.com/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-zephyr.patch
URL:		http://www.everybuddy.com/
BuildRequires:	ORBit-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	esound-devel
BuildRequires:	libtool
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	perl
Prereq:		/sbin/ldconfig
Requires:	applnk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_mandir		%{_prefix}/man

%description
Everybuddy is designed to become a Universal Instant Messaging client
desigend to seamlessly integrate all existing Instant Messaging
clients and provide a single consistant user interface. Currently,
Everybuddy supports sending and reciveing messages in AOL, ICQ, Yahoo,
MSN and Jabber. IRC support is possibly planned to be incorporated in
future releases.

%description -l pl
Everybuddy jest zaprojektowany tak by móc staæ siê Uniwersalnym
Klientem Natychmiastowych Wiadomo¶ci (Instant Messaging). Zosta³ on
zaprojektowany tak by udostêpniæ us³ugi AOL, ICQ, Yahoo, MSN oraz
Jabber przez zunifikowany i jednolity interfejs u¿ytkownika.

%description -l pt_BR
O everybuddy é projetado para tornar-se um cliente universal para
mensagens instantâneas e para integrar facilmente todos os clientes
deste tipo existentes, fornecendo uma única interface consistente com
o usuário. Atualmente suporta o envio e recebimento de mensagens nas
redes AOL, ICQ, Yahoo e MSN. Suporte a IRC possivelmente seja
incorporado em versões futuras.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal -I m4
autoconf
automake -a -c
%configure \
	--enable-gnome \
	--enable-panel \
	--enable-zephyr \
	--disable-arts \
	--disable-krb4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	AUtilitiesdir=%{_applnkdir}/Network/Communications
	
gzip -9nf AUTHORS NEWS README TODO \
	doc/{CREDITS,FAQ,NOMENCLATURE,README*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {*,doc/*}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/*
%{_applnkdir}/Network/Communications/*.desktop
%{_pixmapsdir}/*
%{_datadir}/sounds/%{name}
