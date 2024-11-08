%global srcname dasbus

Name:           python-%{srcname}
Version:        1.7
Release:        1
Summary:        DBus library in Python 3
License:        LGPL-2.1-or-later
URL:            https://pypi.python.org/pypi/dasbus
Source0:        https://files.pythonhosted.org/packages/source/d/dasbus/dasbus-%{version}.tar.gz
Group:          Development/Libraries/Python
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-gobject3


%description
Dasbus is a DBus library written in Python 3, based on
GLib and inspired by pydbus. It is designed to be easy
to use and extend.}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.md
%{python_sitelib}/%{srcname}-*.egg-info/
%{python_sitelib}/%{srcname}/
