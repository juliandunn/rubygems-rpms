# Generated from mixlib-shellout-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-shellout
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

Summary: Run external commands on Unix or Windows
Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 2%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/opscode/mixlib-shellout
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests for this package are not in the gem. To update:
# git clone https://github.com/opscode/mixlib-shellout.git && cd mixlib-shellout
# git checkout 1.1.0
# tar czvf rubygem-mixlib-shellout-1.1.0-specs.tgz spec/
Source1: rubygem-%{gem_name}-%{version}-specs.tgz
# Patch for UsrMove, see http://tickets.opscode.com/browse/MIXLIB-6
Source2: mixlib-shellout-usrmove.patch
# Patch for removal of awesomeprint, see http://tickets.opscode.com/browse/MIXLIB-7
Source3: mixlib-shellout-awesomeprint-removal.patch

Requires: ruby(abi) > %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby(abi) = %{rubyabi}
%{!?el6:BuildRequires: rubygem(rspec)}
%{!?el6:BuildRequires: rubygems-devel}
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Run external commands on Unix or Windows

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

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar zxvf %{SOURCE1}
patch -p1 < %{SOURCE2}
patch -p1 < %{SOURCE3}
# One of the tests involves a fork && sleep 10 that may not finish before mock
rspec && sleep 10
popd

%files
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}

%changelog
* Tue Dec 18 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.1.0-2
- add patches for rspec test issues on Fedora

* Sun Oct 21 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.1.0-1
- rebuild with 1.1.0

* Sun Jun 17 2012 Jonas Courteau <rpms@courteau.org> - 1.0.0-3
- move all test-related operations into check
- excluding gem_cache

* Sun Jun 3 2012 Jonas Courteau <rpms@courteau.org> - 1.0.0-2
- exclude specs from final package
- link to upstream bug reports for missing specs, broken test

* Sat May 12 2012  Jonas Courteau <rpms@courteau.org> - 1.0.0-1
- Initial package
