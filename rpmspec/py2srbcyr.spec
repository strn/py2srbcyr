%global         srcname py2srbcyr

Name:           python3-%{srcname}
Version:        %{_version}
Release:        1%{?dist}
Summary:        Python module that transliterates text from Croatian Latin to Serbian Cyrillic alphabet

License:        LGPLv3+
URL:            https://github.com/strn/py2srbcyr
Source0:        %{srcname}-%{version}.tar.gz
Source1:        %{srcname}-%{version}-py3-none-any.whl

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3
Provides:       python3-%{srcname}

%description
Python module that transliterates text from Croatian Latin to Serbian Cyrillic alphabet.
The module is Python implementation of great Javascript Ћирилизатор - Cyrillizer.

%prep
%autosetup -n %{srcname}-%{_version}

%check
cd "%{_builddir}/%{srcname}-%{_version}"
unset RPM_BUILD_ROOT
%{__python3} -m pytest

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir %{buildroot}
cd "%{_sourcedir}"
ls -l
%{__python3} -m pip install --target %{buildroot}%{python3_sitelib} %{srcname}-%{_version}-py3-none-any.whl

%files
%{python3_sitelib}/%{srcname}/__init__.py
%{python3_sitelib}/%{srcname}/*.txt
%{python3_sitelib}/%{srcname}/__pycache__/__init__*pyc
%{python3_sitelib}/%{srcname}-%{version}.dist-info/*

%changelog
* Sun Aug 02 2026 Strana <zcprog+git> - 1.1.2-1
- Initial package
