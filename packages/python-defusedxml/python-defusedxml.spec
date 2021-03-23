# Created by pyp2rpm-3.3.3
%global pypi_name defusedxml

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        1%{?dist}
Summary:        XML bomb protection for Python stdlib modules

License:        PSFL
URL:            https://github.com/tiran/defusedxml
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%doc README.html README.md README.txt other/README.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 0.7.1-1
- Update to 0.7.1

* Tue Apr 28 2020 Evgeni Golov - 0.6.0-1
- Initial package.
