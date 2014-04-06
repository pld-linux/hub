Summary:	hub makes git better with github
Name:		hub
Version:	1.12.0
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://github.com/github/hub/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	87d6ba3ffd513814dedf6a6b6e07e41f
URL:		http://hub.github.com/
Requires:	git-core >= 1.7.3
Requires:	ruby >= 1:1.8.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hub is a command line tool that wraps git in order to extend it with
extra features and commands that make working with GitHub easier.

hub is best aliased as git, so you can type $ git <command> in the
shell and get all the usual hub features.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
rake install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md LICENSE
%attr(755,root,root) %{_bindir}/hub
%{_mandir}/man1/hub.1*
