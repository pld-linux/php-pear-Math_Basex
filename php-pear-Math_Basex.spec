%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Basex
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Base X conversion class
Summary(pl):	%{_class}_%{_subclass} - klasa konwersji mi�dzy systemami liczenia Base X
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4cfe8184e596c0d2fb399581e457d4ce
URL:		http://pear.php.net/package/Math_Basex/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple class for converting base set of numbers with a customize
character base set.

In PEAR status of this package is: %{_status}.

%description -l pl
Prosta klasa do konwersji liczb mi�dzy r�nymi systemami liczenia z
konfigurowalnym zestawem cyfr.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests
%{php_pear_dir}/%{_class}/*.php
