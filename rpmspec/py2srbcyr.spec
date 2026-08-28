%global         srcname py2srbcyr

Name:           python3-%{srcname}
Version:        %{_version}
Release:        1%{?dist}
Summary:        Python module that transliterates text from Croatian Latin to Serbian Cyrillic alphabet

License:        LGPLv3+
URL:            https://github.com/strn/py2srbcyr
Source0:        %{srcname}-%{version}.tar.gz
Source1:        %{srcname}-%{version}-py3-none-any.whl
Source2:        %{srcname}.py

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
mkdir -p %{buildroot}%{_bindir} %{buildroot}/usr/lib64/gedit/plugins/%{srcname}
cp %{srcname}.py %{buildroot}%{_bindir}/%{srcname}
cp py2crolat.py %{buildroot}%{_bindir}/py2crolat
%{__python3} -m pip install --target %{buildroot}%{python3_sitelib} %{srcname}-%{_version}-py3-none-any.whl
# Copy Gedit plugin files
cp plugin-gedit/%{srcname}.plugin %{buildroot}/usr/lib64/gedit/plugins/
cp plugin-gedit/__init__.py %{buildroot}/usr/lib64/gedit/plugins/%{srcname}
%{__python3} -m compileall %{buildroot}/usr/lib64/gedit/plugins/%{srcname}/__init__.py
# Copy Sigil plugin files

%files
%defattr(644, root, root, 755)
%{python3_sitelib}/%{srcname}/__init__.py
%{python3_sitelib}/%{srcname}/*.txt
%{python3_sitelib}/%{srcname}/__pycache__/__init__*pyc
%{python3_sitelib}/%{srcname}-%{version}.dist-info/*
%attr(755, root, root) %{_bindir}/%{srcname}
%attr(755, root, root) %{_bindir}/py2crolat

%package -n python3-%{srcname}-plugin-gedit
Summary:        gEdit plugin for transliteration of text written in Croatian Latin script into Serbian Cyrillic script
BuildRequires:  python3-devel
Requires:       python3-%{srcname}
%{?python_provide:%python_provide python3-%{srcname}-plugin-gedit}

%description -n python3-%{srcname}-plugin-gedit
gEdit plugin. Croatian Latin script to Serbian Cyrillic script transliterator.

%files -n python3-%{srcname}-plugin-gedit
%defattr(644, root, root, 755)
/usr/lib64/gedit/plugins/%{srcname}.plugin
/usr/lib64/gedit/plugins/%{srcname}/*

%package -n python3-%{srcname}-plugin-sigil
Summary:        Sigil plugin for transliteration of text written in Croatian Latin script into Serbian Cyrillic script
BuildRequires:  python3-devel
Requires:       python3-%{srcname}
%{?python_provide:%python_provide python3-%{srcname}-plugin-sigil}

%description -n python3-%{srcname}-plugin-sigil
Sigil plugin. Croatian Latin script to Serbian Cyrillic script transliterator.

%files -n python3-%{srcname}-plugin-sigil
%defattr(644, root, root, 755)

%changelog
* Fri Aug 28 2026 Strana <zcprog+git> - 1.1.3-1
- Added Gedit plugin package

* Fri Aug 28 2026 Strana <zcprog+git> - 1.1.3-1
- Added command line scripts

* Sun Aug 02 2026 Strana <zcprog+git> - 1.1.2-1
- Initial package
