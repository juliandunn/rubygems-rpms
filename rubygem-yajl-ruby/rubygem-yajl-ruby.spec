# Generated from yajl-ruby-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name yajl-ruby

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

Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library
Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/brianmario/yajl-ruby
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby-devel
%{!?el6:BuildRequires: rubygem(rspec)}
%{!?el6:BuildRequires: rubygems-devel}
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local \
  --install-dir $(pwd)%{gem_dir} \
  -V \
  --force --rdoc \
   %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext
# Remove other cruft from the gem
rm %{buildroot}%{gem_instdir}/.gitignore \
   %{buildroot}%{gem_instdir}/.travis.yml 
# Move C extension to extdir:
mkdir -p %{buildroot}%{gem_extdir}/lib/yajl
mv %{buildroot}%{gem_instdir}/lib/yajl/yajl.so %{buildroot}%{gem_extdir}/lib/yajl/

# Fix permissions
# https://github.com/brianmario/yajl-ruby/issues/103
chmod -x %{buildroot}%{gem_instdir}/benchmark/subjects/unicode.json

%check
%if %{?el6}0
# spec on EL6 is too old; need RSpec2 
%else
pushd .%{gem_instdir}
rspec
popd
%endif

%files
%doc %{gem_instdir}/MIT-LICENSE
%dir %{gem_instdir}
%{gem_extdir}
%{gem_libdir}
%{gem_spec}
# https://github.com/brianmario/yajl-ruby/issues/103
%exclude %{gem_instdir}/.rspec
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/benchmark
%{gem_instdir}/examples
%{gem_instdir}/spec
%{gem_instdir}/tasks
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/README.md
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Tue Dec 25 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.1.0-2
- Unify EPEL and Fedora builds. Correct defects from review, bz#823351

* Mon Apr 30 2012  <rpms@courteau.org> - 1.1.0-1
- Initial package
