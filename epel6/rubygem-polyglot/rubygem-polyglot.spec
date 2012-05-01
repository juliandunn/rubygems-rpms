%global gem_name polyglot

%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global rubyabi 1.8

Summary:        Allow hooking of language loaders for specified extensions into require
Name:           rubygem-%{gem_name}
Version:        0.3.1
Release:        4%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://polyglot.rubyforge.org
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:       ruby(rubygems)
Requires:       ruby(abi) = %{rubyabi}
BuildRequires:  ruby(rubygems)
BuildRequires:  ruby(abi) = %{rubyabi}
BuildRequires(check):  rubygem(minitest)
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}

%description
This Ruby GEM allows custom language loaders for specified file extensions
to be hooked into require.


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
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
pushd %{buildroot}%{gem_instdir}
testrb -I. test
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/License.txt
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/test


%changelog
* Sun Apr 22 2012 Jonas Courteau <rpms@courteau.org> - 0.3.1-4
- Ported to EPEL 6.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 0.3.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.3.1-1
- Updated to the latest upstream version.
- Tests enabled.
- Documentation moved into separate package.
- Remove unnecessary Hoe runtime dependency.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.2.5-3
- Get rid of duplicate files

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.2.5-2
- Bring tests back
- Depend on ruby(abi)
- Replace defines with globals
- Don't delete the world-writable file, fix permissions instead

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.2.5-1
- Package generated by gem2rpm
- Remove log directory
- Don't ship tests
- Fix up License