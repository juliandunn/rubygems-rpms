# Generated from mixlib-authentication-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-authentication

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

Summary: Simple per-request authentication
Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/opscode/mixlib-authentication
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(mixlib-log)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: ruby(abi) = %{rubyabi}
# Needed to run checks:
%{!?el6:BuildRequires: rubygem(rspec)}
%{!?el6:BuildRequires: rubygems-devel}
%{!?el6:BuildRequires: rubygem(mixlib-log)}
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Mixlib::Authentication provides a class-based header signing authentication
object.

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
rspec -Ilib spec/mixlib/authentication/
popd
%endif

%files
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NOTICE
%dir %{gem_instdir}
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%doc %{gem_docdir}

%changelog
* Sun Dec 23 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.3.0-1
- Upgrade to 1.3.0
- Drop rubygem-mixlib-authentication-1.1.4-spec.patch

* Sun Apr 29 2012 Jonas Courteau <rpms@courteau.org> - 1.1.4-1
- Repackaged for fc17
- New upstream version
- Patch to fix broken spec (fixed in upstream commit fe5cd0116)

* Fri Mar 19 2010 Matthew Kent <matt@bravenet.com> - 1.1.2-2
- Let check phase fail.
- Fix duplicate inclusion of Rakefile.

* Wed Mar 17 2010 Matthew Kent <matt@bravenet.com> - 1.1.2-1
- Initial package
