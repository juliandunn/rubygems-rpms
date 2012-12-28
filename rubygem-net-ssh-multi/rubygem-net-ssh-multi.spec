# Generated from net-ssh-multi-1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh-multi

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

Summary: Control multiple Net::SSH connections via a single interface
Name: rubygem-%{gem_name}
Version: 1.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/net-ssh/net-ssh-multi
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: rubygem(net-ssh) >= 2.1.4
Requires: rubygem(net-ssh-gateway) >= 0.99.0
%{!?el6:BuildRequires: rubygems-devel}
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(net-ssh)
BuildRequires: rubygem(net-ssh-gateway)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Control multiple Net::SSH connections via a single interface.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local \
  --install-dir $(pwd)%{gem_dir} \
  --force --rdoc \
   %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd %{buildroot}%{gem_instdir}
testrb -Ilib test
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Rakefile

%changelog
* Thu Dec 27 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.1-2
- Unified EPEL and Fedora builds

* Sat Apr 14 2012  <rpms@courteau.org> - 1.1-1
- Initial package
