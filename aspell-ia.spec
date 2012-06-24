Summary:	Interlingua dictionary for aspell
Summary(pl):	S�ownik interlingua dla aspella
Name:		aspell-ia
Version:	0.50
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/ia/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	36846c747a4cb7874b00f37752e83f25
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interlingua dictionary (i.e. word list) for aspell.

%description -l pl
S�ownik (lista s��w) interlingua dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
