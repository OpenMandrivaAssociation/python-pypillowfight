%define module pypillowfight
%define oname libpillowfight

Name:		python-pypillowfight
Summary:	Library containing various image processing algorithms
Version:	0.3.1
Release:	1
License:	GPL-2.0-or-later
Group:		Development/Python
URL:		https://gitlab.gnome.org/World/OpenPaperwork/libpillowfight
Source0:	%{URL}/-/archive/%{version}/libpillowfight-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	make
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(nose)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Library containing various image processing algorithms.

%prep
%autosetup -n %{oname}-%{version} -p1
echo "#define INTERNAL_PILLOWFIGHT_VERSION \"%{version}\"" > src/pillowfight/_version.h

%files
%doc README.md
%license LICENSE
%{python_sitearch}/pillowfight
%{python_sitearch}/%{module}-%{version}*.*-info
