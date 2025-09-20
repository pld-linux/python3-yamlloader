Summary:	Ordered YAML loader and dumper for PyYAML
Summary(pl.UTF-8):	Moduł dla PyYAML-a do wczytywania i zapisywania YAML-a z zachowaniem porządku
Name:		python3-yamlloader
Version:	1.5.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/yamlloader/
Source0:	https://files.pythonhosted.org/packages/source/y/yamlloader/yamlloader-%{version}.tar.gz
# Source0-md5:	c806c13b6d85c2b87063dcbc37678066
URL:		https://pypi.org/project/yamlloader/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides loaders and dumpers for PyYAML. Currently, an
OrderedDict loader/dumper is implemented, allowing to keep items order
when loading resp. dumping a file from/to an OrderedDict (or regular
dict in Python 3.7+).

%description -l pl.UTF-8
Ten moduł udostępnia funkcje do wczytywania i zapisywania dla
PyYAML-a. Obecnie obsługiwane są struktury OrderedDict, pozwalające na
zachowanie kolejności między wczytaniem a zrzucaniem (dla Pythona 3.7+
obsługiwane są także zwykłe słowniki).

%prep
%setup -q -n yamlloader-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/yamlloader
%{py3_sitescriptdir}/yamlloader-%{version}.dist-info
