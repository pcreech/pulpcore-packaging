%{?python_disable_dependency_generator}
%global pypi_name opentelemetry_instrumentation

Name:           python-%{pypi_name}
Version:        0.40b0
Release:        1%{?dist}
Summary:        Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/opentelemetry-instrumentation/
Source:         https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-opentelemetry-api >= 1.4
Requires:       python%{python3_pkgversion}-opentelemetry-api < 2
Requires:       python%{python3_pkgversion}-setuptools >= 16.0
Requires:       python%{python3_pkgversion}-opentelemetry-wrapt >= 1.0.0
Requires:       python%{python3_pkgversion}-opentelemetry-wrapt < 2.0.0

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/opentelemetry/instrumentation
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{_bindir}/opentelemetry-bootstrap
%{_bindir}/opentelemetry-instrument

%changelog
* Wed Jul 26 2023 Odilon Sousa - 0.40b0-1
- Initial package.