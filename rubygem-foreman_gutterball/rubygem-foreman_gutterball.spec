%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_gutterball

Summary: Gutterball plugin for Foreman and Katello
Name: 	 %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.1
Release: 2%{?dist}
Group:   Development/Languages
License: GPLv3
URL:     http://katello.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
Requires: gutterball
Requires: %{?scl_prefix}rubygem-katello
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: foreman-plugin >= 1.8

%description
Gutterball plugin for Foreman and Katello.

%prep
%setup -q -c -T
%{__install} --directory .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
# it's recommended to clean your buildroot first
%{__rm} --recursive --force %{buildroot}

%{__install} --directory %{buildroot}%{gem_dir}
%{__cp} --archive .%{gem_dir}/cache %{buildroot}%{gem_dir}/
%{__cp} --archive .%{gem_dir}/doc %{buildroot}%{gem_dir}/
%{__cp} --archive .%{gem_dir}/gems %{buildroot}%{gem_dir}/
%{__cp} --archive .%{gem_dir}/specifications %{buildroot}%{gem_dir}/

%{__install} --directory %{buildroot}%{foreman_bundlerd_dir}

%foreman_bundlerd_file

%clean
%{__rm} --recursive --force %{buildroot} .%{gem_dir}

%files
%defattr(644, root, foreman, -)
%{gem_instdir}/Rakefile
%{gem_instdir}/LICENSE
%{gem_instdir}/README.md
%{gem_instdir}/app/
%{gem_instdir}/lib/
%{gem_instdir}/config/
%{gem_instdir}/test/
%{gem_spec}
%{gem_cache}
%{foreman_bundlerd_plugin}

%changelog
* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.1-2
- new package built with tito

* Wed Dec 03 2014 Adam Price <komidore64@gmail.com> - 0.0.1-1
- Initial package