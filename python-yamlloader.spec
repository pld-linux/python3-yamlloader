#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Ordered YAML loader and dumper for PyYAML
Summary(pl.UTF-8):	Moduł dla PyYAML-a do wczytywania i zapisywania YAML-a z zachowaniem porządku
Name:		python-yamlloader
Version:	0.5.5
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/yamlloader/
Source0:	https://files.pythonhosted.org/packages/source/y/yamlloader/yamlloader-%{version}.tar.gz
# Source0-md5:	2e0750ace81235f750c072833d79c4c3
URL:		https://pypi.org/project/yamlloader/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
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

%package -n python3-yamlloader
Summary:	Ordered YAML loader and dumper for PyYAML
Summary(pl.UTF-8):	Moduł dla PyYAML-a do wczytywania i zapisywania YAML-a z zachowaniem porządku
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-yamlloader
This module provides loaders and dumpers for PyYAML. Currently, an
OrderedDict loader/dumper is implemented, allowing to keep items order
when loading resp. dumping a file from/to an OrderedDict (or regular
dict in Python 3.7+).

%description -n python3-yamlloader -l pl.UTF-8
Ten moduł udostępnia funkcje do wczytywania i zapisywania dla
PyYAML-a. Obecnie obsługiwane są struktury OrderedDict, pozwalające na
zachowanie kolejności między wczytaniem a zrzucaniem (dla Pythona 3.7+
obsługiwane są także zwykłe słowniki).

%prep
%setup -q -n yamlloader-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/yamlloader
%{py_sitescriptdir}/yamlloader-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-yamlloader
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/yamlloader
%{py3_sitescriptdir}/yamlloader-%{version}-py*.egg-info
%endif
