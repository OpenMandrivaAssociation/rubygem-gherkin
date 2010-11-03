%define oname gherkin

Summary:    Fast Gherkin lexer/parser
Name:       rubygem-%{oname}
Version:    1.0.30
Release:    %mkrel 1
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/aslakhellesoy/gherkin
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(trollop) >= 1.16.2
Requires:   rubygem(rspec) >= 1.3.0
Requires:   rubygem(cucumber) >= 0.7.2
Requires:   rubygem(rake-compiler) >= 0.7.0
BuildRequires: rubygems
BuildRequires: ruby-devel
Provides:   rubygem(%{oname}) = %{version}

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.

%prep

%build
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
cp -a .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ -name ".git*" -exec rm {} \;
rm %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.mailmap

# install the sofiles in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/*.so %{buildroot}%{ruby_sitearchdir}

# install executables
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/gherkin
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/ikvm/
%{ruby_gemdir}/gems/%{oname}-%{version}/java/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/ragel/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/tasks/
%{ruby_gemdir}/gems/%{oname}-%{version}/cucumber.yml
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION.yml
%{ruby_sitearchdir}/%{oname}*.so
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
