# -*- rpm-spec -*-
%global gem_name bunny

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

Summary: Synchronous Ruby AMQP 0.9.1 client
Name: rubygem-%{gem_name}
Version: 0.8.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/ruby-amqp/bunny
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby 
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
%{!?el6:BuildRequires: rubygems-devel}
# Disabled for now; tests disabled due to need for running rabbitmq server
#BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A synchronous Ruby AMQP client that enables interaction with AMQP-compliant
brokers.


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

# clean up a bunch of un-needed files:
# See https://github.com/ruby-amqp/bunny/issues/55
rm -f .%{gem_instdir}/{.gitignore,.rspec,.travis.yml,.yardopts}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
# Disabled check - requires a running rabbitmq server
#pushd %{buildroot}%{gem_instdir}
#rspec -Ilib spec/spec_09/*_spec.rb
#popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/ext
%{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.textile
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/spec
# Extraneous file, see https://github.com/ruby-amqp/bunny/issues/55
%exclude %{gem_instdir}/bunny.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/Rakefile

%changelog
* Tue Oct 23 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.8.0-1
- Upgrade to 0.8.0

* Mon Apr 30 2012  <rpms@courteau.org> - 0.7.9-1
- Initial package
- Submitted https://github.com/ruby-amqp/bunny/issues/55 upstream to remove dot-files
- Disabled test, requires a running rabbitmq server with a specific config
