%global debug_package %{nil}

Name: thefuck
Version: 3.32
Release: 1%{?dist}
Summary: App that corrects your previous console command
License: MIT
URL: https://github.com/nvbn/thefuck
ExclusiveArch: x86_64 aarch64
Source0: https://github.com/nvbn/%{name}/archive/%{version}.tar.gz

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-psutil
BuildRequires: python%{python3_pkgversion}-pip
BuildRequires: python%{python3_pkgversion}-six
BuildRequires: python%{python3_pkgversion}-decorator
BuildRequires: python%{python3_pkgversion}-pytest
BuildRequires: python%{python3_pkgversion}-mock
BuildRequires: python%{python3_pkgversion}-colorama
Requires: python3
Requires: python%{python3_pkgversion}-psutil
Requires: python%{python3_pkgversion}-six
Requires: python%{python3_pkgversion}-colorama

%description
This application corrects your previous console command.
If you use BASH, you should add these lines to your .bashrc:
alias fuck='eval $(thefuck $(fc -ln -1)); history -r'
alias FUCK='fuck'
For other shells please check /usr/share/doc/thefuck/README.md

%prep
%autosetup -p1
sed -i -e '/^#!\//, 1d' *.py
find -type f -executable -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%{_bindir}/thefuck
%{_bindir}/fuck
%{python3_sitelib}/thefuck-%{version}-*egg-info
%{python3_sitelib}/thefuck
%doc README.md
%license LICENSE.md

%changelog
* Sat Jul 05 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.32-1
- Verified 3.32 is latest upstream release; project dead since 2022
- Verified Source0 downloadable

* Thu Jul 03 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.32-1
- Add ExclusiveArch: x86_64 aarch64; %%autosetup -p1

* Fri May 22 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.32-1
- Fix spec violations: use %{buildroot}, %global for constants

* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.32-1
- Update to 3.32

* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 3.15-7
- Modernize for AlmaLinux 10: drop RHEL7 conditionals, python3 only

* Sun Jun 02 2019 Casjays Developments <rpm-devel@casjaysdev.pro> - 3.15-6
- Fixes for RHEL 8 and fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.15-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Matias Kreder <delete@fedoraproject.org> 3.15-1
- Updated to thefuck 3.15

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Matias Kreder <delete@fedoraproject.org> 3.2-3
- Added buildrequires

* Wed Nov 18 2015 Matias Kreder <delete@fedoraproject.org> 3.2-1
- Updated to thefuck 3.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python2.5

* Thu Jul 2 2015 Matias Kreder <delete@fedoraproject.org> 1.46-1
- Initial spec
