Summary:	UDP-based Data Transfer library
Summary(pl.UTF-8):	UDT (UDP-based Data Transfer) - biblioteka transportu danych w oparciu o UDP
Name:		udt
Version:	4.11
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/udt/udt.sdk.%{version}.tar.gz
# Source0-md5:	30b1556e5cf0afe179e40a53a1371b08
URL:		http://udt.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UDT is a reliable UDP based application level data transport protocol
for distributed data intensive applications over wide area high-speed
networks. UDT uses UDP to transfer bulk data with its own reliability
control and congestion control mechanisms. The new protocol can
transfer data at a much higher speed than TCP does. UDT is also a
highly configurable framework that can accommodate various congestion
control algorithms. 

%description -l pl.UTF-8
UDT to oparty na UDP wiarygodny protokół transportowy działający na
poziomie aplikacji przeznaczony dla aplikacji rozproszonych z dużą
ilością danych używających szybkich sieci o dużym zasięgu. UDT
wykorzystuje UDP do przesyłania danych z własną kontrolą niezawodności
i mechanizmami kontroli wysycenia. Nowy protokół jest w stanie
przesyłać dane o wiele szybciej niż TCP. UDT jest też szkieletem o
dużej konfigurowalności, potrafiącym obsłużyć różne algorytmy kontroli
wysycenia.

%package devel
Summary:	Header files for UDT library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki UDT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for UDT library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki UDT.

%package static
Summary:	Static UDT library
Summary(pl.UTF-8):	Statyczna biblioteka UDT
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static UDT library.

%description static -l pl.UTF-8
Statyczna biblioteka UDT.

%package apidocs
Summary:	UDT API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki UDT
Group:		Documentation

%description apidocs
API documentation for UDT library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki UDT.

%prep
%setup -q -n udt4

%{__sed} -i -e '/^CCFLAGS/s/ -O3/ %{rpmcxxflags}/;s/^C++ = .*/C++ = %{__cxx}/' src/Makefile app/Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install src/{libudt.so,libudt.a} $RPM_BUILD_ROOT%{_libdir}
cp -p src/udt.h $RPM_BUILD_ROOT%{_includedir}
ln $RPM_BUILD_ROOT%{_includedir}/udt.h $RPM_BUILD_ROOT%{_includedir}/udt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt RELEASE_NOTES.txt draft-gg-udt-xx.txt
%attr(755,root,root) %{_libdir}/libudt.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/udt.h
%{_includedir}/udt

%files static
%defattr(644,root,root,755)
%{_libdir}/libudt.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/*
