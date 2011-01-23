%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Basex
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Base X conversion class
Summary(pl.UTF-8):	%{_class}_%{_subclass} - klasa konwersji między systemami liczenia Base X
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	80d0ba3e86fd857e281a474727dd00c3
URL:		http://pear.php.net/package/Math_Basex/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Math_Basex-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple class for converting base set of numbers with a customize
character base set.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Prosta klasa do konwersji liczb między różnymi systemami liczenia z
konfigurowalnym zestawem cyfr.

Ta klasa ma w PEAR status: %{_status}.

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
