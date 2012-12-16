# Generated from moneta-0.6.0.gem by gem2rpm -*- rpm-spec -*-

%global gem_name moneta
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

Summary: A unified interface to key/value stores
Name: rubygem-%{gem_name}
Version: 0.6.0
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/wycats/moneta
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests:
# git clone https://github.com/wycats/moneta.git && cd moneta
# git checkout 0.6.0
# tar -czf rubygem-moneta-0.6.0-specs.tgz spec/
Source1: %{name}-%{version}-specs.tgz
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
%{!?el6:BuildRequires: rubygem(rspec)}
%{!?el6:BuildRequires: rubygems-devel}
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Moneta provides a standard interface for interacting with various kinds of
key/value stores including Memcache, Redis, CouchDB, Berkeley DB and many more.

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

# Unpack the tests
tar zxvf %{SOURCE1}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
# Note: Tests are disabled because the ones bundled with this version are
# too old to run (they're RSpec 1.x tests). The ones in master are fine,
# but haven't been released; if/when they do, uncomment the following:
# %if %{!?el6}1
# cp -pr spec/ .%{gem_instdir}
# pushd ./%{gem_instdir}
# rspec -Ilib spec/moneta_basic_file_spec.rb spec/moneta_file_spec.rb
# rm -rf spec
# popd
# %endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/TODO
%{gem_instdir}/Rakefile

%changelog
* Thu Dec 13 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.6.0-3
- Update spec after review

* Sat Nov 24 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.6.0-2
- Undeprecate package, rebuild with conditional ABI macros

* Tue Mar 16 2010 Matthew Kent <mkent@magoazul.com> - 0.6.0-1
- Initial package
