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
Requires: ruby 
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
%{!?el6:BuildRequires: rubygems-devel}
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A unified interface to key/value stores

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

# Unneeded file
rm .%{gem_instdir}/TODO

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/LICENSE
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile

%changelog
* Sat Nov 24 2012 Julian C. Dunn <jdunn@aquezada.com> - 0.6.0-3
- Undeprecate package, rebuild with conditional ABI macros
