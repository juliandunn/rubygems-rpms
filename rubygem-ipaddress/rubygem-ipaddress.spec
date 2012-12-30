# Generated from ipaddress-0.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ipaddress

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

Summary: IPv4/IPv6 addresses manipulation library
Name: rubygem-%{gem_name}
Version: 0.8.0
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/bluemonk/ipaddress
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
%{!?el6:BuildRequires: rubygems-devel}
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
IPAddress is a Ruby library designed to make manipulation
of IPv4 and IPv6 addresses both powerful and simple. It maintains
a layer of compatibility with Ruby's own IPAddr, while 
addressing many of its issues.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

# Remove un-needed file
# See https://github.com/bluemonk/ipaddress/issues/23
rm .%{gem_instdir}/.document

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
testrb -Ilib test/ipaddress_test.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/README.rdoc
%{gem_instdir}/VERSION
%{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Rakefile

%changelog
* Sat Dec 29 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-3
- Correct duplicate LICENSE file

* Thu Dec 27 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-2
- Revised per review in bz#823340

* Mon Apr 30 2012 Jonas Courteau <rpms@courteau.org> - 0.8.0-1
- Initial package
- Submitted https://github.com/bluemonk/ipaddress/issues/23 upstream to remove extra file from gem
