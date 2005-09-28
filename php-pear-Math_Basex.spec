%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Basex
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Base X conversion class
Summary(pl):	%{_class}_%{_subclass} - klasa konwersji miêdzy systemami liczenia Base X
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	2.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4cfe8184e596c0d2fb399581e457d4ce
URL:		http://pear.php.net/package/Math_Basex/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple class for converting base set of numbers with a customize
character base set.

In PEAR status of this package is: %{_status}.

%description -l pl
Prosta klasa do konwersji liczb miêdzy ró¿nymi systemami liczenia z
konfigurowalnym zestawem cyfr.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
