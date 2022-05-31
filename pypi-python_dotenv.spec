#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_dotenv
Version  : 0.19.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/49/62/4f25667e10561303a34cb89e3187c35985c0889b99f6f1468aaf17fbb03e/python-dotenv-0.19.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/62/4f25667e10561303a34cb89e3187c35985c0889b99f6f1468aaf17fbb03e/python-dotenv-0.19.2.tar.gz
Summary  : Read key-value pairs from a .env file and set them as environment variables
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-python_dotenv-bin = %{version}-%{release}
Requires: pypi-python_dotenv-license = %{version}-%{release}
Requires: pypi-python_dotenv-python = %{version}-%{release}
Requires: pypi-python_dotenv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(bumpversion)
BuildRequires : pypi(click)
BuildRequires : pypi(flake8)
BuildRequires : pypi(ipython)
BuildRequires : pypi(mock)
BuildRequires : pypi(py)
BuildRequires : pypi(sh)
BuildRequires : pypi(tox)
BuildRequires : pypi(twine)
BuildRequires : pypi(types_mock)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# python-dotenv
[![Build Status][build_status_badge]][build_status_link]
[![PyPI version][pypi_badge]][pypi_link]

%package bin
Summary: bin components for the pypi-python_dotenv package.
Group: Binaries
Requires: pypi-python_dotenv-license = %{version}-%{release}

%description bin
bin components for the pypi-python_dotenv package.


%package license
Summary: license components for the pypi-python_dotenv package.
Group: Default

%description license
license components for the pypi-python_dotenv package.


%package python
Summary: python components for the pypi-python_dotenv package.
Group: Default
Requires: pypi-python_dotenv-python3 = %{version}-%{release}

%description python
python components for the pypi-python_dotenv package.


%package python3
Summary: python3 components for the pypi-python_dotenv package.
Group: Default
Requires: python3-core
Provides: pypi(python_dotenv)

%description python3
python3 components for the pypi-python_dotenv package.


%prep
%setup -q -n python-dotenv-0.19.2
cd %{_builddir}/python-dotenv-0.19.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641551898
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_dotenv
cp %{_builddir}/python-dotenv-0.19.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_dotenv/36fe354f4526001c781c4c99847c059ebc00878c
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dotenv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_dotenv/36fe354f4526001c781c4c99847c059ebc00878c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*