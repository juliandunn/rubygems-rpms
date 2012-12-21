# Generated from mixlib-log-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-log
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

Summary: Ruby mix-in for log functionality
Name: rubygem-%{gem_name}
Version: 1.4.1
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-log
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem

Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
%{!?el6:BuildRequires: rubygem(rspec)}
%{!?el6:BuildRequires: rubygems-devel}
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A gem that provides a simple mix-in for log functionality.

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
pushd ./%{gem_instdir}
rspec
popd
%endif

%files
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/NOTICE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/.gemtest
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec

%changelog
* Fri Dec 21 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.4.1-1
- Rebuilt with 1.4.1, specs are bundled

* Sun Apr 29 2012 Jonas Courteau <rpms@courteau.org> - 1.3.0-1
- Repackaged for fc17
- New upstream version
- Removed check patch
- Modified check - pull tests manually as they've been removed from gem

* Wed Jun 9 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-3
- New patch to enable check again.

* Tue Jun 8 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-2
- Disable check for now.

* Tue Mar 23 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-1
- New upstream version - moves to jeweler for gem creation.

* Mon Oct 5 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-3
- Missing complete source url (#526181).
- Remove unused ruby_sitelib macro (#526181).
- Remove redundant doc Requires on rubygems (#526181).

* Sun Oct 4 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-2
- Remove redundant path in doc package (#526181).
- Use global over define (#526181).

* Mon Sep 28 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-1
- Initial package
