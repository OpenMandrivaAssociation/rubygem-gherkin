%define oname gherkin

Summary:    Fast Gherkin lexer/parser
Name:       rubygem-%{oname}
Version:    2.9.3
Release:    1
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/aslakhellesoy/gherkin
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
Requires:   rubygems
Requires:   rubygem(cucumber) >= 0.7.2
Requires:   rubygem(rake-compiler) >= 0.7.0
Requires:   rubygem(json) >= 1.4.6
Requires:   rubygem(term-ansicolor) >= 1.0.5
#Requires:   rubygem(awesome_print) >= 0.2.1
Requires:   rubygem(rspec) >= 2.0.0
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
mkdir -p %{buildroot}%{ruby_gemdir}
cp -a .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ -name ".git*" -exec rm {} \;
rm %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.mailmap

# install the sofiles in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/*.so %{buildroot}%{ruby_sitearchdir}

%files
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.rspec
%{ruby_gemdir}/gems/%{oname}-%{version}/.rvmrc
%{ruby_gemdir}/gems/%{oname}-%{version}/*.sh
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/ragel/
%{ruby_gemdir}/gems/%{oname}-%{version}/cucumber.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/.travis.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/js/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/tasks/
%{ruby_gemdir}/gems/%{oname}-%{version}/examples/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/.rbenv-gemsets
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/.yardopts
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_sitearchdir}/%{oname}*.so
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
