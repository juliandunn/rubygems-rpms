# Generated from mixlib-cli-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-cli

# EPEL6 lacks rubygems-devel package that provides these macros
%if %{?el6}0
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%endif

%if %{?el6}0 || %{?fc16}0
%global rubyabi 1.8
%else
%global rubyabi 1.9.1
%endif

Summary: Simple Ruby mix-in for CLI interfaces
Name: rubygem-%{gem_name}
Version: 1.2.2
Release: 2%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-cli
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
%{!?el6:BuildRequires: rubygems-devel}
%{!?el6:BuildRequires: rubygem(rspec)}
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(rake)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A simple mix-in for CLI interfaces, including option parsing.

%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

mkdir -p .%{gem_dir}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
%if %{?el6}0
# spec on EL6 is too old; need RSpec2 
%else
pushd .%{gem_instdir}
rspec
#rspec -Ilib spec/mixlib/cli_spec.rb
popd
%endif

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec

%files doc
%{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/NOTICE
%{gem_instdir}/README.rdoc

%changelog
* Wed Dec 13 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.2.2-2
- Unify build on EPEL6 and Fedora

* Mon Apr 30 2012 Jonas Courteau <rpm@courteau.org> - 1.2.2-1
- Repackaged for fc17
- Changed check to avoid need for patch
- New upstream version

* Wed Jun 9 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-3
- New patch to enable check again.

* Tue Jun 8 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-2
- Disable check for now.

* Tue Mar 23 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-1
- New upstream version - moves to jeweler for gem creation.

* Mon Oct 5 2009 Matthew Kent <mkent@magoazul.com> - 1.0.4-3
- Remove unused ruby_sitelib macro (#526179).
- Remove redundant doc Requires on rubygems (#526179).

* Sun Oct 4 2009 Matthew Kent <mkent@magoazul.com> - 1.0.4-2
- Remove redundant path in doc package (#526179).
- Use global over define (#526179).

* Mon Sep 28 2009 Matthew Kent <mkent@magoazul.com> - 1.0.4-1
- Initial package
