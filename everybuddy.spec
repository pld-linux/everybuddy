Summary:	A Universal Instant Messanging Client 
Summary(pl):	Uniwersalny Klient Natychmiastowych Wiadomo¶ci
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
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	ORBit-devel
BuildRequires:	esound-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm missing
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
