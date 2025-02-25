# Created by pyp2rpm-3.3.3
%global pypi_name aiodns

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Simple DNS resolver for asyncio

License:        MIT
URL:            https://github.com/saghul/aiodns
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pycares >= 4.0.0

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jun 11 2021 Evgeni Golov 3.0.0-1
- Update to 3.0.0

* Thu Nov 05 2020 Evgeni Golov - 2.0.0-3
- Fix License tag in spec file

* Wed Apr 01 2020 Evgeni Golov - 2.0.0-2
- Add python3-typing to Requires

* Wed Mar 18 2020 Samir Jha - 2.0.0-1
- Initial package.
