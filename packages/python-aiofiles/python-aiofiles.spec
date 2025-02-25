# Created by pyp2rpm-3.3.3
%global pypi_name aiofiles

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        File support for asyncio

License:        Apache 2.0
URL:            https://github.com/Tinche/aiofiles
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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
* Fri Jun 11 2021 Evgeni Golov 0.7.0-1
- Update to 0.7.0

* Thu Oct 29 2020 Evgeni Golov 0.6.0-1
- Update to 0.6.0

* Tue Apr 14 2020 Evgeni Golov 0.5.0-1
- Update to 0.5.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.4.0-1
- Initial package.
