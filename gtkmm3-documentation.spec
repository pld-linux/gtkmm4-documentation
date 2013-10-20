%define		glibmm_ver	2.36.0
%define		gtkmm3_ver	3.10.0
Summary:	Documentation and examples for gtkmm - C++ API for GTK+
Summary(pl.UTF-8):	Dokumentacja i przykłady do gtkmm - API C++ dla GTK+
Name:		gtkmm3-documentation
Version:	3.9.1
Release:	1
License:	FDL v1.2+ (documentation), GPL v2 (examples)
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm-documentation/3.9/gtkmm-documentation-%{version}.tar.xz
# Source0-md5:	596fc99a53711df73576a059178ee31a
URL:		http://www.gtkmm.org/
#BuildRequires:	autoconf >= 2.59
#BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd45-xml
BuildRequires:	glibmm-devel >= %{glibmm_ver}
BuildRequires:	gnome-doc-utils >= 0.9.0
BuildRequires:	gtkmm3-devel >= %{gtkmm3_ver}
BuildRequires:	libstdc++-devel >= 5:3.3.1
BuildRequires:	mm-common
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtkmm3-apidocs >= %{gtkmm3_ver}
Suggests:	glibmm-devel >= %{glibmm_ver}
Suggests:	gtkmm3-devel >= %{gtkmm3_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the documentation and example programs for
gtkmm 3.x - C++ API for GTK+ 3.x.

%description -l pl.UTF-8
Ten pakiet zawiera dokumentację oraz programy przykładowe do
gtkmm 3.x - API C++ dla GTK+ 3.x.

%prep
%setup -q -n gtkmm-documentation-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/gtkmm3-%{version}
cp -pr examples/{book,others,README} $RPM_BUILD_ROOT%{_examplesdir}/gtkmm3-%{version}

%find_lang gtkmm-tutorial --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gtkmm-tutorial.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_docdir}/gtkmm-3.0/tutorial
%{_examplesdir}/gtkmm3-%{version}
