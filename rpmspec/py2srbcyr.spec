%global version 1.1.2

Name:           python3-py2srbcyr
Version:        %{version}
Release:        1%{?dist}
Summary:        Python module that transliterates text from Croatian Latin to Serbian Cyrillic alphabet

License:        LGPL-3.0
URL:            https://github.com/strn/py2srbcyr
Source:         %{url}/archive/v%{version}/...-%{version}.tar.gz / %{pypi_source ...}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Python module that transliterates text from Croatian Latin to Serbian Cyrillic alphabet.
The module is Python implementation of great Javascript Ћирилизатор - Cyrillizer.


%prep
%autosetup -p1 -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x... / -g... / -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ...


%check
%pytest


%files -n %{name} -f %{pyproject_files}
%doc README.*
%{_bindir}/dummy


%changelog
* Sun Aug 02 2026 Simone Caronni <negativo17@gmail.com> - 1.1.2-1
- Initial package
