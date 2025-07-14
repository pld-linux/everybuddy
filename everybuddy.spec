Summary:	A Universal Instant Messanging Client
Summary(pl.UTF-8):	Uniwersalny Klient Natychmiastowych Wiadomości
Summary(pt_BR.UTF-8):	Um cliente universal para mensagens instantâneas
Name:		everybuddy
Version:	0.2.1beta6
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://www.everybuddy.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	f9f020a184459a9289fbdd9b62cf0bfb
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Everybuddy is designed to become a Universal Instant Messaging client
desigend to seamlessly integrate all existing Instant Messaging
clients and provide a single consistant user interface. Currently,
Everybuddy supports sending and reciveing messages in AOL, ICQ, Yahoo,
MSN and Jabber. IRC support is possibly planned to be incorporated in
future releases.

%description -l pl.UTF-8
Everybuddy jest zaprojektowany tak by móc stać się Uniwersalnym
Klientem Natychmiastowych Wiadomości (Instant Messaging). Został on
zaprojektowany tak by udostępnić usługi AOL, ICQ, Yahoo, MSN oraz
Jabber przez zunifikowany i jednolity interfejs użytkownika.

%description -l pt_BR.UTF-8
O everybuddy é projetado para tornar-se um cliente universal para
mensagens instantâneas e para integrar facilmente todos os clientes
deste tipo existentes, fornecendo uma única interface consistente com
o usuário. Atualmente suporta o envio e recebimento de mensagens nas
redes AOL, ICQ, Yahoo e MSN. Suporte a IRC possivelmente seja
incorporado em versões futuras.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO doc/{CREDITS,FAQ,NOMENCLATURE,README*}
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/*
%{_applnkdir}/Network/Communications/*.desktop
%{_pixmapsdir}/*
%{_datadir}/sounds/%{name}
