Summary:	Library containing various image processing algorithms
Name:		python-pypillowfight
Version:	0.3.0
Release:	1
License:	GPLv2
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pypillowfight/pypillowfight-%{version}.tar.gz
URL:		https://pypi.org/project/pypillowfight/
BuildRequires:	python%{pyver}dist(nose)
BuildRequires:	python%{pyver}dist(pip)

%description
Library containing various image processing algorithms

%files
%{py_platsitedir}/pillowfight
%{py_platsitedir}/pypillowfight-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n pypillowfight-%{version}

%build
%py_build

%install
%py_install

