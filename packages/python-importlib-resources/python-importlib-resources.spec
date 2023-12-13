%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name importlib-resources

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        5.4.0
Release:        7%{?dist}
Summary:        Read resources from Python packages

License:        Apache2
URL:            https://github.com/python/importlib_resources
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_resources-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools-scm >= 3.4.1


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-zipp >= 3.1.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n importlib_resources-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Force setuptools_scm usage for older setuptools
sed -i 's/setuptools.setup.*/setuptools.setup(use_scm_version=True)/' setup.py
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/importlib_resources
%{python3_sitelib}/importlib_resources-*-py%{python3_version}.egg-info


%changelog
* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 5.4.0-7
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 5.4.0-6
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 5.4.0-5
- Build against python 3.11

* Mon Aug 08 2022 Odilon Sousa <osousa@redhat.com> - 5.4.0-4
- Force setuptools_scm usage for older setuptools

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 5.4.0-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 5.4.0-1
- Release python-importlib-resources 5.4.0

* Wed Sep 08 2021 Evgeni Golov - 5.0.0-2
- Build against Python 3.8

* Tue Jul 13 2021 Evgeni Golov - 5.0.0-1
- Initial package.
