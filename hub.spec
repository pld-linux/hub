Summary:	Command-line wrapper for git that makes you better at GitHub
Name:		hub
Version:	2.2.3
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	https://github.com/github/hub/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6675992ddd16d186eac7ba4484d57f5b
URL:		http://hub.github.com/
BuildRequires:	golang >= 1.5
BuildRequires:	bash
Requires:	git-core >= 1.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# go stuff
%define _enable_debug_packages 0

%description
hub is a command line tool that wraps git in order to extend it with
extra features and commands that make working with GitHub easier.

hub is best aliased as git, so you can type $ git <command> in the
shell and get all the usual hub features.

%prep
%setup -q

%build
bash -x ./script/build -o hub

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p hub $RPM_BUILD_ROOT%{_bindir}
cp -p man/hub.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md LICENSE
%attr(755,root,root) %{_bindir}/hub
%{_mandir}/man1/hub.1*
