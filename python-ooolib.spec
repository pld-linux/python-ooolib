%define 	module	ooolib
Summary:	Python module for creating OpenDocument documents (sp.sheet/text)
Name:		python-%{module}
Version:	0.0.17
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/ooolib/ooolib-python-%{version}.tar.gz
# Source0-md5:	938245d947b2aca05a9d52a2b8be9af5
URL:		http://ooolib.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ooolib is a python module to be used to create simple OpenDocument
spreadsheet and text documents.

%prep
%setup -q -n ooolib-python-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
        --root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README  examples/*example*.py
%attr(755,root,root) %{py_sitescriptdir}/ooolib/*.py[co]
%{py_sitescriptdir}/*.egg-info
