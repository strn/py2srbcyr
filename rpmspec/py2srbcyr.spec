%global         srcname py2srbcyr

Name:           python3-%{srcname}
Version:        %{_version}
Release:        1%{?dist}
Summary:        Python module that transliterates text from Croatian Latin to Serbian Cyrillic alphabet

License:        LGPLv3+
URL:            https://github.com/strn/py2srbcyr
Source0:        %{srcname}-%{version}.tar.gz    

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3
Provides:       python3-%{srcname}

%description
Python module that transliterates text from Croatian Latin to Serbian Cyrillic alphabet.
The module is Python implementation of great Javascript Ћирилизатор - Cyrillizer.

%prep
%autosetup -n %{srcname}-%{_version}

%build
unset RPM_BUILD_ROOT
%{__python3} -m compileall .
ls -lR

%check
cd "%{_builddir}/%{srcname}-%{_version}"
unset RPM_BUILD_ROOT
%{__python3} -m pytest

%files -n %{name} -f %{pyproject_files}
%doc README.*
%{_bindir}/dummy


%changelog
* Sun Aug 02 2026 Strana <zcprog+git> - 1.1.2-1
- Initial package
